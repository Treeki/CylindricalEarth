from ghidra.program.model.symbol import Namespace, SourceType
from ghidra.app.decompiler import DecompInterface
from ghidra.util.task import TaskMonitor
handler = ghidra.program.model.data.DataTypeConflictHandler.ConflictResolutionPolicy.RENAME_AND_ADD.handler

# a bad kludge
globalNS = getSymbol('memcpy', None).parentNamespace

def resolveIt(path):
	boundaries = []
	stk = 0
	for i in xrange(len(path) - 1):
		c = path[i]
		if c == '<':
			stk += 1
		elif c == '>':
			stk -= 1
		elif c == ':' and path[i+1] == ':' and stk == 0:
			boundaries.append(i)

	bound = 0
	bits = []
	for b in boundaries:
		bits.append(path[bound:b])
		bound = b + 2
	bits.append(path[bound:])
	print(bits)
	
	symName = bits.pop(-1)
	ns = globalNS
	for bit in bits:
		ns_ = getNamespace(ns, bit)
		if ns_ is None:
			ns_ = currentProgram.symbolTable.createNameSpace(ns, bit, SourceType.USER_DEFINED)
		ns = ns_
	return (ns, symName)


DEBUG = False

dtManager = currentProgram.dataTypeManager
symbolTable = currentProgram.symbolTable

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



def findAllProfiles():
    profileCtor = getSymbol('ctor', getNamespace(None, 'ActorProfile')).address
    profileCtorFn = getFunctionAt(profileCtor)
    inits = set(profileCtorFn.getCallingFunctions(TaskMonitor.DUMMY))
    print('scanning %d inits' % len(inits))
    n = 0

    for init in inits:
        dec = decompile(init)
        assert dec.decompileCompleted()
        highFunc = dec.highFunction
        stackvars = {}

        for op in highFunc.pcodeOps:
            if op.mnemonic == 'COPY' and op.output.space == 53:
                dst = op.output
                src = op.inputs[0]
                stackvars[dst.offset] = src
            if op.mnemonic == 'CALL' and op.inputs[0].offset == profileCtor.offset:
                if DEBUG: print('found ActorProfile call')
                profile = resolveVarNode(op.inputs[1])
                if DEBUG: print('profile = %x' % profile)
                actorID = resolveVarNode(op.inputs[2])&0xffffffff
                if DEBUG: print('id = %x' % actorID)
                buildAddr = resolveVarNode(op.inputs[3])
                if DEBUG: print('buildAddr = %x' % buildAddr)
                actorSize = resolveVarNode(op.inputs[4])
                if DEBUG: print('size = %x' % actorSize)
                opx = op.inputs[6].def
                assert str(opx.inputs[0]) == '(register, 0x8, 8)'
                actorName = resolveVarNode(stackvars[opx.inputs[1].offset + 8])
                if DEBUG: print('thingy = %x' % actorName)
                opx = op.inputs[5].def
                if opx.mnemonic == 'CAST': opx = opx.inputs[0].def
                assert str(opx.inputs[0]) == '(register, 0x8, 8)'
                actorSubName = resolveVarNode(stackvars[opx.inputs[1].offset + 8])
                yield actorID, profile, buildAddr, actorSize, readString(actorName), readString(actorSubName)
                n += 1
        #if n >= 5: break



def varnodeIsActually(vn, check):
    if vn == check:
        return True
    op = vn.def
    if op is None:
        return False
    if op.mnemonic == 'INDIRECT' or op.mnemonic == 'CAST':
        return varnodeIsActually(op.inputs[0], check)
    if op.mnemonic == 'PTRSUB' and str(op.inputs[1]) == '(const, 0x0, 8)':
        return varnodeIsActually(op.inputs[0], check)
    if DEBUG: print(op)
    return False


stack = []
def processBuildFunc(addr, arg=False):
    if addr in stack:
        return

    stack.append(addr)

    func = getFunctionAt(addr)
    dec = decompile(func)
    assert dec.decompileCompleted()
    highFunc = dec.highFunction
    baseBuf = None
    vtable = None
    didCtor = False
    if arg:
        baseBuf = highFunc.localSymbolMap.getParam(0).instances[0]

    for op in highFunc.pcodeOps:
        if op.mnemonic == 'CALL':
            if baseBuf is None:
                baseBuf = op.output
                if DEBUG: print('found base @ %r' % baseBuf)
            else:
                if len(op.inputs) > 1 and vtable is None and not didCtor and varnodeIsActually(op.inputs[1], baseBuf):
                    didCtor = True
                    if DEBUG: print('calling base ctor %r' % op.inputs[0])
                    vtable = processBuildFunc(toAddr(op.inputs[0].offset), True)
                    if DEBUG: print('--base ctor returned %r' % vtable)
        #if op.output is not None and baseBuf is not None:
        #    if varnodeIsActually(op.output, baseBuf):
        #        print('maybe')
        #        print(op)
        if op.mnemonic == 'STORE':
            if varnodeIsActually(op.inputs[1], baseBuf):
                vtable = resolveVarNode(op.inputs[2])
                if DEBUG: print('vtable is %x' % vtable)

    stack.pop()
    return vtable


if False:
    DEBUG = True
    # shit = processBuildFunc(toAddr(0x7100e391e0))
    shit = processBuildFunc(toAddr(0x71000e9740))
    if shit is None:
        print('none')
    else:
        print('%x' % shit)
else:
    buildFuncMap = {}
    profiles = []
    for profile in sorted(findAllProfiles()):
        print('%03d | %x | %x | 0x%-5x | %-40s | %s' % profile)
        profiles.append(profile)
        aid, profile, buildAddr, structSize, name, subname = profile
        if buildAddr in buildFuncMap:
            assert buildFuncMap[buildAddr] == name
        else:
            buildFuncMap[buildAddr] = name


    # find all the vtables
    for func, name in sorted(buildFuncMap.iteritems()):
        print('%r %s...' % (func, name))
        vtable = processBuildFunc(toAddr(func))
        if vtable is None:
            print('failed to find VT for %x / %s' % (func, name))
        else:
            # print('VT reported for %x is %x' % (func, vtable))
            sym = getSymbolAt(toAddr(vtable))
            ns = sym.parentNamespace
            # print('%40s -> %s' % ('::'.join(ns.symbol.path).replace('Global::',''), name))
            print('%s -> %s' % ('::'.join(sym.path), name))

            newNSParent, newNSName = resolveIt(name)
            if ns.parentNamespace != newNSParent:
                ns.setParentNamespace(newNSParent)
            if ns.symbol.name != newNSName:
                ns.symbol.setName(newNSName, SourceType.USER_DEFINED)

            buildFuncSym = getSymbolAt(toAddr(func))
            if buildFuncSym.name != 'build' or buildFuncSym.parentNamespace != ns:
                buildFuncSym.setNameAndNamespace('build', ns, SourceType.USER_DEFINED)


