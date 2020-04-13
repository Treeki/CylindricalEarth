from capstone import *
from capstone.arm64 import *
from debug_tools import *

NODE_SIZE = 0x38

import sys
import json
with open(sys.argv[1], 'r') as f:
    schema = json.load(f)

savemgr = ptr(0x710373c1f8)
savemgr_vt = ptr(savemgr)
assert(savemgr_vt == 0x710320ead8)

print('found the SaveMgr at %x' % savemgr)

size_cache = {}
def workOutSize(vtbl):
    if vtbl in size_cache:
        return size_cache[vtbl]
    print('getting size for %x (%d)' % (vtbl, len(size_cache)))
    fn = ptr(vtbl + 0x18)
    code = read(fn, 0x20)
    md = Cs(CS_ARCH_ARM64, CS_MODE_ARM)
    md.detail = True
    w0 = None
    for insn in md.disasm(code, 0):
        # print(insn.mnemonic, insn.op_str)
        if insn.mnemonic == 'movz':
            assert insn.operands[0].type == ARM64_OP_REG and insn.operands[0].reg == ARM64_REG_W0
            assert insn.operands[1].type == ARM64_OP_IMM
            w0 = insn.operands[1].imm
        elif insn.mnemonic == 'movk':
            assert insn.operands[0].type == ARM64_OP_REG and insn.operands[0].reg == ARM64_REG_W0
            assert insn.operands[1].type == ARM64_OP_IMM
            w0 |= (insn.operands[1].imm << insn.operands[1].shift.value)
        elif insn.mnemonic == 'orr':
            assert insn.operands[0].type == ARM64_OP_REG and insn.operands[0].reg == ARM64_REG_W0
            assert insn.operands[1].type == ARM64_OP_REG and insn.operands[1].reg == ARM64_REG_WZR
            assert insn.operands[2].type == ARM64_OP_IMM
            w0 = insn.operands[2].imm
        elif insn.mnemonic == 'ret':
            # print('returning %r' % w0)
            size_cache[vtbl] = w0
            return w0
        else:
            raise ValueError('dunno what %r is at %x' % (insn, fn))
    raise ValueError('reached end at vtbl=%x / fn=%x / code=%r' % (vtbl, fn, code))


knownToBeALeaf = {}

def extractNode(node, expectedBuffer=None, depth=0):
    info = []
    while node > 0:
        nx_vtbl, nx_buf, offset, nx_child, nx_next = struct.unpack('<QQQQQ', read(node, 0x28))
        vtbl = nx_to_re(nx_vtbl)
        buf = nx_to_re(nx_buf)
        if expectedBuffer is not None:
            assert buf == expectedBuffer
        size = workOutSize(vtbl)
        child = nx_to_re(nx_child)
        info.append([node, vtbl, offset, size, child])
        node = nx_to_re(nx_next)
    info.reverse()
    for n in info:
        node, vtbl, offset, size, child = n
        if vtbl in knownToBeALeaf:
            assert(knownToBeALeaf[vtbl] == (child == 0))
            n[-1] = None
        else:
            knownToBeALeaf[vtbl] = (child == 0)
            n[-1] = extractNode(child, buf, depth + 1)
    return info


output = {}

def readNode(addr):
    nx_vtbl, nx_buf, offset, nx_child, nx_next = struct.unpack('<QQQQQ', read(addr, 0x28))
    vtbl = nx_to_re(nx_vtbl)
    buf = nx_to_re(nx_buf)
    size = workOutSize(vtbl)
    child = nx_to_re(nx_child) if nx_child > 0 else 0
    nextNode = nx_to_re(nx_next) if nx_next > 0 else 0
    return (vtbl, buf, offset, size, child, nextNode)

def captureRoot(node, typeSpec):
    if isinstance(typeSpec, tuple):
        typeID, dup1, dup2 = typeSpec
    else:
        typeID = typeSpec
        dup1, dup2 = 1, 1
    typ = schema['types'][str(typeID)]

    # read this parent node
    vtbl, buf, offset, size, child, nextNode = readNode(node)
    print(f'expecting root {typeID:x} ({typ["name"]}) of size 0x{typ["size"]:x}, got size 0x{size:x}')
    assert offset == 0
    assert size == (typ['size'] * dup1 * dup2)

    # now handle the children...
    if child > 0:
        captureTypeFields(typeID, typ, node, vtbl, child)

    assert nextNode == 0

def findFurthestSibling(node):
    while True:
        nextNode = ptr(node + 0x20)
        if nextNode == 0:
            return node
        else:
            node = nextNode

def captureTypeFields(typeID, typ, parentNode, parentVtable, firstChild, baseOffset=0):
    # placeholder
    output[typeID] = None
    ioNodes = []
    ioNodeSize = NODE_SIZE

    # first build a list in forwards order
    nodes = []
    node = firstChild
    while node > 0:
        vtbl, buf, offset, size, child, nextNode = readNode(node)
        nodes.insert(0, (node, vtbl, buf, offset, size, child))
        node = nextNode

    # now work through them
    for node, vtbl, buf, offset, size, child in nodes:
        nodeOffset = node - parentNode
        if ioNodeSize != nodeOffset:
            print(f'GAP IN OFFSET: {ioNodeSize:X} -> {nodeOffset:X}')
        print(f'n={node:x} noffs={nodeOffset:5x} vt={vtbl:x} buf={buf:x} @{offset:6x}:{size:6x} child={child:x}')

        # find matching field
        for field in typ['fields']:
            if field['offset'] == (offset - baseOffset) and (field['size'] * field['length'][0] * field['length'][1]) == size:
                print('found match! %r' % field)
                if field['length'][0] > 1:
                    # arrays are segregated into a sub-node
                    # these still need fixing, honestly x.x
                    assert(findFurthestSibling(child) == (node + NODE_SIZE))
                    e_vtbl, e_buf, e_offset, e_size, e_child, _e_nextNode = readNode(child)
                    print(f'element: n={child:x} vt={e_vtbl:x} buf={e_buf:x} @{e_offset:6x}:{e_size:6x} child={e_child:x}')
                    assert(field['size'] == e_size)
                    if field['type'] not in output:
                        if e_child > 0:
                            # we gotta recurse...
                            captureTypeFields(field['type'], schema['types'][str(field['type'])], child, e_vtbl, e_child, e_offset)
                        else:
                            # plain old leaf node
                            output[field['type']] = dict(size=NODE_SIZE, subnodes=[], vtable=e_vtbl)
                    ioNodeSize = max(ioNodeSize, nodeOffset + NODE_SIZE + (output[field['type']]['size'] * field['length'][0] * field['length'][1]))
                    ioNodes.append(dict(id=field['id'], offset=nodeOffset, arrayVtable=vtbl))
                else:
                    if field['type'] not in output:
                        if child > 0 and str(field['type']) in schema['types']:
                            # we gotta recurse...
                            captureTypeFields(field['type'], schema['types'][str(field['type'])], node, vtbl, child, offset)
                        else:
                            # plain old leaf node
                            output[field['type']] = dict(size=NODE_SIZE, subnodes=[], vtable=vtbl)
                    ioNodeSize = max(ioNodeSize, nodeOffset + output[field['type']]['size'])
                    ioNodes.append(dict(id=field['id'], offset=nodeOffset))
                break
        else:
            print('match NOT found')
            print(f'candidates: {typ["fields"]}')

    output[typeID] = dict(size=ioNodeSize, subnodes=ioNodes, vtable=parentVtable)



captureRoot(ptr(savemgr+0xc0),           0xb5ee3b70)          # ::Game::SaveMain
#skip this, it's included in the other structs anyway
#captureRoot(ptr(savemgr+0xc8),           (0x3e30a29e, 10, 1)) # ::Game::SaveAnimal
captureRoot(ptr(savemgr+0xd0),           0x6bdd2fbf)          # ::Game::SaveLandMyDesign
captureRoot(ptr(savemgr+0xe0),           0x6d45991c)          # ::Game::SavePlayer
captureRoot(ptr(savemgr+0xe0)+0x173e0,   0x038fa568)          # ::Game::SavePlayerOther
captureRoot(ptr(savemgr+0xf8),           0xe410534a)          # ::Game::SavePostBox
captureRoot(ptr(ptr(savemgr+0x50)+0x20), 0x6b11c0c5)          # ::Game::SavePhotoStudioIsland
captureRoot(ptr(ptr(savemgr+0x58)+0x20), 0x75ad3a68)          # ::Game::SaveProfile

with open('save_io_structure.json', 'w') as f:
    json.dump(output, f, indent=2)

