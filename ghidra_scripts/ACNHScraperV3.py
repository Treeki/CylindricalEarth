# this is where it gets truly w i l d

from ghidra.program.model.data import EnumDataType, CategoryPath
from ghidra.program.model.mem import MemoryAccessException
from ghidra.program.model.listing.Function import FunctionUpdateType
from ghidra.program.model.symbol import Namespace, SourceType
from ghidra.app.decompiler import DecompInterface
from ghidra.util.task import TaskMonitor
handler = ghidra.program.model.data.DataTypeConflictHandler.ConflictResolutionPolicy.RENAME_AND_ADD.handler
import json
import hashlib
import os
import re
import sys

DEBUG = False
ONLY_FUNC = None #toAddr(0x7100cb9470)

BCSV_PATH = '/Volumes/HFS/repos/switch/ac112upd/romfs/Bcsv'
EARTH = '/Volumes/HFS/repos/switch/CylindricalEarth'
if EARTH not in sys.path:
    sys.path.append(EARTH)

from bcsv import *
from build_specs import preset_names

CALL_KLUDGES = {
    # ItemParam's vf20 calls into this instead of just using memset...
    0x7100A42EC0: 0x5f
}

dtManager = currentProgram.dataTypeManager
symbolTable = currentProgram.symbolTable

bcsvNS = getNamespace(None, 'Bcsv')
enumNS = getNamespace(None, 'Enum')
enumCatPath = CategoryPath('/Enum')
enumCat = dtManager.getCategory(enumCatPath)
assert bcsvNS is not None
assert enumNS is not None
assert enumCat is not None

memcpy = toAddr('memcpy')
parseTextCS = toAddr('_ZN4sead8EnumUtil15getParseTextCS_Ev')
initValueCS = toAddr('_ZN4sead8EnumUtil20getInitValueArrayCS_Ev')
parseText = toAddr('_ZN4sead8EnumUtil10parseText_EPPcS1_i')
cxa_guard_release = toAddr('__cxa_guard_release')
ItemParamRow_resolveField = toAddr('ItemParamRow_resolveField')

# parseText's function signature should be committed with P
# char**, char*, int

boolDT = dtManager.getDataType('/bool')
charDT = dtManager.getDataType('/char')
charPtrDT = dtManager.getPointer(charDT)
charPtrPtrDT = dtManager.getPointer(charPtrDT)
intDT = dtManager.getDataType('/int')

def readStringLimited(addr, length):
    if isinstance(addr, long):
        addr = toAddr(addr)
    return ''.join([chr(getByte(addr.add(i))&0xff) for i in xrange(length)])

def readString(addr):
    if isinstance(addr, long):
        addr = toAddr(addr)
    bits = []
    while True:
        c = getByte(addr)
        if c == 0:
            return ''.join(bits).decode('utf-8')
        else:
            bits.append(chr(c&0xff))
        addr = addr.add(1)

def hashEnum(choices):
    return hashlib.md5(u'***'.join(choices).encode('utf-8')).hexdigest()[:12]


decompiler = None
def decompile(func):
    global decompiler
    if decompiler is None:
        decompiler = DecompInterface()
        decompiler.openProgram(currentProgram)
    results = decompiler.decompileFunction(func, 10, TaskMonitor.DUMMY)
    return results

def resolvePcodeOp(op):
    if DEBUG: print('trying to resolve op', op)
    mnemonic = op.mnemonic
    if mnemonic == 'CAST' or mnemonic == 'COPY':
        return resolveVarNode(op.inputs[0])
    #elif mnemonic == 'INDIRECT':
    #    return resolveVarNode(op.inputs[0])
    elif mnemonic == 'MULTIEQUAL':
        expected = resolveVarNode(op.inputs[0])
        for i in xrange(1, len(op.inputs)):
            assert resolveVarNode(op.inputs[i]) == expected
        return expected
    elif mnemonic == 'LOAD':
        target = resolveVarNode(op.inputs[1])
        if op.inputs[1].size == 8:
            try:
                return getLong(toAddr(target))
            except MemoryAccessException:
                return ('load', target)
        raise Exception('dunno how to load from {:x} for {}'.format(target, op))
    elif mnemonic == 'PTRADD':
        base = resolveVarNode(op.inputs[0])
        index = resolveVarNode(op.inputs[1])
        size = resolveVarNode(op.inputs[2])
        return base + index * size
    elif mnemonic == 'PTRSUB':
        base = resolveVarNode(op.inputs[0])
        index = resolveVarNode(op.inputs[1])
        return base + index
    else:
        raise Exception('dunno how to deal with {}'.format(op))

def resolveVarNode(vn):
    if DEBUG: print('trying to resolve varnode', vn)
    if vn.constant:
        return vn.offset
    elif vn.address:
        # this is gonna be something in RAM
        if vn.size == 8:
            try:
                return getLong(toAddr(vn.offset))
            except MemoryAccessException:
                return ('load', vn.offset)
        else:
            raise Exception('dunno how to get {} from ram'.format(vn))
        # return toAddr(vn.offset)
    else:
        return resolvePcodeOp(vn.def)

def handleParseText(op, memcpys):
    # op is a PcodeOp representing the parseText_ call
    assert len(op.inputs) == 4
    if DEBUG: print('parseText output ::')
    outputArray = resolveVarNode(op.inputs[1])
    if DEBUG: print('parseText input ::')
    inputStr = resolveVarNode(op.inputs[2])
    if DEBUG: print('parseText count ::')
    count = resolveVarNode(op.inputs[3])

    # inputStr is going to be part of a SafeString
    # this gets built with memcpy, always
    inputStr = memcpys[inputStr]

    choices = readString(inputStr)
    choices = [c.strip() for c in choices.split(',')]
    if choices[-1] == '':
        del choices[-1]
    assert len(choices) == count

    return outputArray, choices
    # print('outputArray is at {:x}, inputStr is at {:x}, count is {}'.format(outputArray, inputStr, count))

def handleMemcpy(op):
    # op is a PcodeOp representing the memcpy call
    assert len(op.inputs) == 4
    if DEBUG: print('memcpy src ::')
    src = resolveVarNode(op.inputs[2])
    if DEBUG: print('memcpy dest ::')
    dest = resolveVarNode(op.inputs[1])
    # we don't pull out the count as it's the result of a condition
    # and that fucks things up
    return (dest, src)




def findAllEnums():
    enumInfo = {}
    count = 0
    functionsSeen = set()
    for ref in getReferencesTo(parseText):
        assert ref.referenceType.unConditional
        assert ref.referenceType.call
        fn = getFunctionContaining(ref.fromAddress)
        if ONLY_FUNC is not None and fn.entryPoint != ONLY_FUNC:
            continue
        if fn.entryPoint in functionsSeen:
            continue
        functionsSeen.add(fn.entryPoint)

        dec = decompile(fn)
        assert dec.decompileCompleted()
        highFunc = dec.highFunction
        memcpys = {}

        # scan 1: find memcpy
        for op in highFunc.pcodeOps:
            if op.mnemonic == 'CALL' and op.inputs[0].offset == memcpy.offset:
                print('found memcpy call: {}'.format(op))
                try:
                    result = handleMemcpy(op)
                    dest, src = result
                    memcpys[dest] = src
                except:
                    print('memcpy gen error in {}'.format(fn))
                    pass

        enumsThisFunc = []
        # scan 2: find parseText
        for op in highFunc.pcodeOps:
            if op.mnemonic == 'CALL' and op.inputs[0].offset == parseText.offset:
                print('found parseText call: {}'.format(op))
                arrayLoc, choices = handleParseText(op, memcpys)

                # look for the store
                blockOps = list(op.parent.getIterator())
                lastOp = blockOps[-1]
                if lastOp.mnemonic == 'STORE':
                    src = resolveVarNode(lastOp.inputs[2])
                    dest = resolveVarNode(lastOp.inputs[1])
                    assert src == arrayLoc
                elif lastOp.mnemonic == 'PTRSUB':
                    dest = resolveVarNode(lastOp.output)
                    offset = resolveVarNode(lastOp.inputs[0])
                    src = resolveVarNode(lastOp.inputs[1])
                    assert src == arrayLoc
                    assert dest[0] == 'load'
                    assert offset == 0
                    dest = dest[1]
                elif lastOp.mnemonic == 'CAST':
                    dest = resolveVarNode(lastOp.output)
                    src = resolveVarNode(lastOp.inputs[0])
                    assert src == arrayLoc
                    assert dest[0] == 'load'
                    dest = dest[1]
                else:
                    for op in blockOps:
                        print op
                    raise Exception('don\'t know where the enum is stored in {}'.format(fn))

                print('writes {:x} to {:x}'.format(src, dest))
                print('{:10x} -> {}'.format(dest, choices))

                key = hashEnum(choices)
                if key not in enumInfo:
                    enumInfo[key] = {'choices': choices, 'getters': [], 'locations': []}
                enumInfo[key]['locations'].append(dest)
                enumsThisFunc.append(key)

        if fn.body.numAddresses == 420 and ref.fromAddress.subtract(fn.entryPoint) == 116:
            assert len(enumsThisFunc) == 1
            print('func {} gets this enum'.format(fn))
            enumInfo[enumsThisFunc[0]]['getters'].append(fn.entryPoint.offset)
        else:
            print('COMPLEX REFERENCE SPOTTED @ {}'.format(fn))

        count += 1
    return enumInfo



SAFE_REGEX = re.compile('^[A-Za-z_][A-Za-z0-9_]+$')

def isEnumSafe(choices):
    for c in choices:
        if SAFE_REGEX.match(c) is None:
            return False
    return True

def scanEnums():
    # scan the existing ones
    for dt in enumCat.dataTypes:
        if dt.description.startswith('hash '):
            key = dt.description[5:5+16]
            enumTypeMap[key] = dt
            enumNames[key] = dt.name
        if dt.description.startswith('hashU16 '):
            key = dt.description[8:8+16]
            enumTypeMapU16[key] = dt


def syncEnums():
    if not enumNames:
        scanEnums()

    # sync all the stuff up
    n = 0
    for key, enum in enumInfo.iteritems():
        if key not in enumTypeMap:
            if isEnumSafe(enum['choices']):
                # gotta throw this one in!
                name = 'Enum' + key
                dt = EnumDataType(enumCatPath, name, 4, dtManager)
                dt.description = 'hash ' + key
                for i, choice in enumerate(enum['choices']):
                    try:
                        dt.add(choice, i)
                    except:
                        dt.add(choice + ('__%d'%i), i)
                dtManager.addDataType(dt, handler)
                enumTypeMap[key] = dt
                enumNames[key] = name
            else:
                print('{} is not safe'.format(enum))

        if key in enumTypeMap and 'needsU16Variant' in enum:
            name = enumNames[key] + '_u16'
            if key not in enumTypeMapU16:
                dt = EnumDataType(enumCatPath, name, 2, dtManager)
                dt.description = 'hashU16 ' + key
                for i, choice in enumerate(enum['choices']):
                    try:
                        dt.add(choice, i)
                    except:
                        dt.add(choice + ('__%d'%i), i)
                dtManager.addDataType(dt, handler)
                enumTypeMapU16[key] = dt
            else:
                if enumTypeMapU16[key].name != name:
                    enumTypeMapU16[key].name = name


        # poke the enum's text array
        for i, addrValue in enumerate(enum['locations']):
            addr = toAddr(addrValue)
            sym = getSymbolAt(addr)

            # is there a name we can pull, for data-type-less enums?
            if key not in enumNames and not sym.dynamic and sym.parentNamespace == enumNS:
                enumNames[key] = sym.name
            # if not, make sure we have one
            if key not in enumNames:
                enumNames[key] = 'Enum' + key

            # either way, give this enum the name it needs
            nameToUse = enumNames[key]
            if i > 0:
                nameToUse += '_%d' % i
            if sym.parentNamespace != enumNS or sym.name != nameToUse:
                sym.setNameAndNamespace(nameToUse, enumNS, SourceType.DEFAULT)

        # poke the enum's getters
        for i, addrValue in enumerate(enum['getters']):
            addr = toAddr(addrValue)
            sym = getSymbolAt(addr)
            fn = getFunctionAt(addr)

            # it's easier here, as we've already picked a canonical name
            nameToUse = enumNames[key]
            if nameToUse.startswith('e'):
                nameToUse = nameToUse[1:]
            nameToUse = 'get' + nameToUse
            if sym.name != nameToUse:
                sym.setNameAndNamespace(nameToUse, enumNS, SourceType.DEFAULT)

            # give the function the correct signature too
            if fn.returnType.name == 'undefined':
                fn.setReturnType(charPtrPtrDT, SourceType.DEFAULT)
                fn.setCallingConvention('__cdecl')

        n += 1


def scrapeBcsvStaticTableFromVf20(fn):
    # let's do this shit
    dec = decompile(fn)
    assert dec.decompileCompleted()
    highFunc = dec.highFunction
    assert len(highFunc.basicBlocks) == 28

    block = highFunc.basicBlocks[18]
    if DEBUG: print(block.start)
    if DEBUG: print(block.stop)
    ops = list(block.iterator)

    baseAddr = None
    maxAddr = None

    if DEBUG: print('*!*!*!* START *!*!*!*')
    for z in ops:
        if DEBUG: print(z)
        if z.mnemonic == 'STORE':
            # here we expect to see either 1, or FFs
            dest = resolveVarNode(z.inputs[1])
            src = resolveVarNode(z.inputs[2])
            if DEBUG: print('*** STORE ***')
            if DEBUG: print(dest, src)
            if src == -1:
                # FFFFFFFFFFFFFFFF -> writing 8 bytes
                addr = dest+4
                if maxAddr is None or addr > maxAddr:
                    if DEBUG: print('maxAddr <- %x' % addr)
                    maxAddr = addr
            elif src == 0xFFFFFFFF:
                # FFFFFFFF -> writing 4 bytes
                if maxAddr is None or dest > maxAddr:
                    if DEBUG: print('maxAddr <- %x' % dest)
                    maxAddr = dest
            elif src == 1:
                if DEBUG: print('baseAddr <- %x' % dest)
                baseAddr = dest
            else:
                raise Exception('I don\'t know what\'s going on here... %r' % z)
        elif z.mnemonic == 'CALL':
            if z.inputs[0].offset == toAddr('memset').offset:
                dest = resolveVarNode(z.inputs[1])
                value = resolveVarNode(z.inputs[2])
                count = resolveVarNode(z.inputs[3])
                assert dest == (baseAddr + 4)
                assert value == 0xFF
                return (baseAddr, count // 4)
            elif z.inputs[0].offset in CALL_KLUDGES:
                return (baseAddr, CALL_KLUDGES[z.inputs[0].offset])

    fieldCount = (maxAddr - baseAddr + 3) // 4
    return (baseAddr, fieldCount)


def stripTypeFromName(name):
    if ' ' in name:
        return name[:name.find(' ')]
    else:
        return name


def declareBcsvOffsets(bcsvNames):
    for bcsvName in bcsvNames:
        if bcsvName == 'CalendarEventCountryParam': continue
        if bcsvName == 'CalendarEventRegionParam': continue
        if bcsvName == 'SoundAmbientPlacementParam': continue
        if bcsvName == 'SoundMaterialType': continue
        if bcsvName == 'WeatherPatternParam': continue
        vtable = toAddr(bcsvName + '_vtable')

        namespace = getNamespace(bcsvNS, bcsvName)
        if namespace is None:
            namespace = symbolTable.createNameSpace(bcsvNS, bcsvName, SourceType.USER_DEFINED)

        # step 1, we want to scrape vf20 for stuff
        vf20addr = toAddr(getLong(vtable.add(0x20)))
        vf20fn = getFunctionAt(vf20addr)
        size = vf20fn.body.numAddresses
        print('%s has vf20 of size %d %% %r' % (bcsvName, size, vf20fn.entryPoint))

        initFlagAddrValue, fieldCount = scrapeBcsvStaticTableFromVf20(vf20fn)
        print('%x , %d fields' % (initFlagAddrValue, fieldCount))

        # make the data we have match this
        bcsv = File(Row)
        with open(BCSV_PATH + '/' + bcsvName + '.bcsv', 'rb') as f:
            bcsv.load(f.read())

        assert len(bcsv.fields) == fieldCount

        initFlagAddr = toAddr(initFlagAddrValue)
        sym = getSymbolAt(initFlagAddr)
        flagName = 'offsetArrayInitFlag'
        if sym.name != flagName:
            removeDataAt(initFlagAddr)
            createData(initFlagAddr, boolDT)
            sym.setNameAndNamespace(flagName, namespace, SourceType.DEFAULT)
        for i,(key,field) in enumerate(bcsv.fields.iteritems()):
            addr = toAddr((initFlagAddrValue + (i * 4) + 4) & ~3)
            sym = getSymbolAt(addr)
            if key in preset_names:
                name = 'offset' + stripTypeFromName(preset_names[key])
            else:
                name = 'offset_%08x' % key
            if sym is None:
                removeDataAt(addr)
                createData(addr, intDT)
                symbolTable.createLabel(addr, name, namespace, SourceType.USER_DEFINED)
            elif sym.name != name:
                removeDataAt(addr)
                createData(addr, intDT)
                sym.setNameAndNamespace(name, namespace, SourceType.USER_DEFINED)


def resolveEnumFromGetter(fn):
    addr = fn.entryPoint.offset
    for key,enum in enumInfo.iteritems():
        if addr in enum['getters']:
            return key


def resolveEnumFromCrcParse(callInsn):
    if callInsn.mnemonicString == 'b':
        callInsn = getInstructionAt(callInsn.getOpObjects(0)[0])
    assert callInsn.mnemonicString == 'mov'
    mov_x1 = callInsn.next
    assert mov_x1.mnemonicString == 'mov'
    bl = mov_x1.next
    assert bl.mnemonicString == 'bl'
    fn = getFunctionAt(bl.getOpObjects(0)[0])
    
    bls_seen = []
    for insn in currentProgram.getListing().getCodeUnits(fn.getBody(), True):
        if insn.mnemonicString == 'bl':
            bls_seen.append(insn.getOperandReferences(0)[0].toAddress)
    for i, f in enumerate(bls_seen):
        if f == cxa_guard_release:
            return resolveEnumFromGetter(getFunctionAt(bls_seen[i + 1]))




def defineBcsvEnumCaches():
    # step 1, sort xrefs into per-function buckets
    buckets = {}
    for ref in getReferencesTo(toAddr('BcsvHeader_usesJPEnums')):
        fn = getFunctionContaining(ref.fromAddress)
        if fn not in buckets: buckets[fn] = []
        buckets[fn].append(ref.fromAddress)

    # step 2, do the work on each one
    for fn, bucket in buckets.iteritems():
        # find out what enums they are
        jpeCall = getInstructionAt(bucket[0])
        after = jpeCall.next
        print(after)
        if after.mnemonicString == 'tbz':
            # points to JP
            jp = resolveEnumFromCrcParse(getInstructionAt(after.getOpObjects(2)[0]))
            en = resolveEnumFromCrcParse(after.next)
        elif after.mnemonicString == 'tbnz':
            # points to EN
            en = resolveEnumFromCrcParse(getInstructionAt(after.getOpObjects(2)[0]))
            jp = resolveEnumFromCrcParse(after.next)
        else:
            raise '???'

        print 'jp @', jp, 'en @', en

        # reuse the strategy from the last time I did this
        bignums = []
        whichBcsv = None
        whichArray = None
        for i in currentProgram.getListing().getCodeUnits(fn.getBody(), True):
            if i.mnemonicString == 'movk':
                reg = i.getRegister(0).name
                prev = i.previous
                assert prev.mnemonicString == 'mov'
                assert prev.getRegister(0).name == reg
                hi_val = i.getOpObjects(1)[0].value
                lo_val = prev.getOpObjects(1)[0].value
                val = lo_val | (hi_val << 16)
                bignums.append(val)
            if i.mnemonicString == 'strb':
                target = getSymbolAt(i.referencesFrom[0].toAddress)
                assert target.name == 'offsetArrayInitFlag'
                whichBcsv = target.parentNamespace.symbol.name
            if i.mnemonicString == 'bl':
                if i.getOpObjects(0)[0] == ItemParamRow_resolveField:
                    whichBcsv = 'ItemParam'
            if i.mnemonicString == 'strh':
                whichArray = i.previous.referencesFrom[0].toAddress
        assert len(bignums) == 1
        fieldKey = bignums[0]

        print('%s . %08x -> array %r' % (whichBcsv, fieldKey, whichArray))

        enum = enumInfo[jp]
        if 'jpBcsvFields' not in enum:
            enum['jpBcsvFields'] = []
        enum['jpBcsvFields'].append([whichBcsv, fieldKey])

        enum = enumInfo[en]
        enum['needsU16Variant'] = True
        if 'bcsvFields' not in enum:
            enum['bcsvFields'] = []
        enum['bcsvFields'].append([whichBcsv, fieldKey])

        namespace = getNamespace(bcsvNS, whichBcsv)

        if en in enumTypeMapU16:
            # define the array!
            removeDataAt(whichArray)
            createData(whichArray, dtManager.getPointer(enumTypeMapU16[en]))
            sym = getSymbolAt(whichArray)
            name = 'enumCache_%08x' % fieldKey
            if sym.name != name:
                sym.setNameAndNamespace(name, namespace, SourceType.DEFAULT)




# now let's get those 
#enumInfo = findAllEnums()
with open('enumData.json', 'r') as f:
    enumInfo = json.load(f)

enumTypeMap = {}
enumTypeMapU16 = {}
enumNames = {}

syncEnums()

defineBcsvEnumCaches()

# just gonna rely on the names I already put together
#bcsvNames = [x.replace('.bcsv', '') for x in os.listdir(BCSV_PATH) if x.endswith('.bcsv')]
#declareBcsvOffsets(bcsvNames)


with open('enumData.json', 'w') as f:
    json.dump(enumInfo, f, indent=4)

