import random
from ghidra.program.model.symbol import Namespace, SourceType

BASE_PATH = '/Volumes/HFS/repos/switch/CylindricalEarth/ghidra_scripts/'

wordPrefixes = [w.strip() for w in open(BASE_PATH + 'wordPrefixes.txt')]
wordSuffixes = [w.strip() for w in open(BASE_PATH + 'wordSuffixes.txt')]
usedNames = set()
for w in open(BASE_PATH + 'usedWords.txt'):
    w = w.strip()
    if w:
        usedNames.add(w)

def generateName():
    while True:
        name = random.choice(wordPrefixes)
        if random.randint(0, 8) == 0:
            name += random.choice(wordPrefixes)
        name += random.choice(wordSuffixes)
        if name not in usedNames:
            usedNames.add(name)
            with open(BASE_PATH + 'usedWords.txt', 'a') as f:
                f.write(name + '\n')
            return name

def resolveSym(symname):
    ns = None
    bits = symname.split('::')
    for bit in bits[:-1]:
        ns = getNamespace(ns, bit)
    return getSymbol(bits[-1], ns)

dtManager = currentProgram.dataTypeManager
symbolTable = currentProgram.symbolTable
rodata = getMemoryBlock('.rodata.1')
data = getMemoryBlock('.data')
text = getMemoryBlock('.text')
external = getMemoryBlock('EXTERNAL')

def lookForPotentialVtables():
    addr = data.start
    endAt = data.end #addr.add(0x2000)

    vtables = []
    curVtable = None

    while addr < endAt:
        what = getLong(addr)
        isText = what >= text.start.offset and what <= text.end.offset
        isExternal = what >= external.start.offset and what <= external.end.offset
        if curVtable is None:
            # maybe start here?
            if (isText or isExternal) and getLong(addr.subtract(8)) == 0 and getLong(addr.subtract(16)) == 0:
                curVtable = addr
        else:
            # maybe end here?
            if not isText and not isExternal:
                vtables.append((curVtable, addr.subtract(curVtable)))
                curVtable = None
        addr = addr.add(8)

    return vtables


potentialVtables = lookForPotentialVtables()
print('found %d potential vtables' % len(potentialVtables))

# where does each function show up?
funcUsageCount = {}
for vtable, vtableSize in potentialVtables:
    for i in xrange(0, vtableSize, 8):
        addr = getLong(vtable.add(i))
        if addr not in funcUsageCount:
            funcUsageCount[addr] = 1
        else:
            funcUsageCount[addr] += 1

# give all vtables a name if they don't have one already
vtNamespaces = {}



for vtable, vtableSize in potentialVtables:
    vtSym = getSymbolAt(vtable)
    if vtSym is None:
        # this isn't gonna be a vtable
        continue
    if vtSym.dynamic:
        name = 'CQ' + generateName()
        ns = symbolTable.createNameSpace(None, name, SourceType.ANALYSIS)
        vtSym.setNameAndNamespace('vtable', ns, SourceType.ANALYSIS)
    else:
        # there's something already
        ns = vtSym.parentNamespace
    vtNamespaces[vtable] = ns

    # name the methods
    for i in xrange(0, vtableSize, 8):
        addrInVT = vtable.add(i)
        what = getLong(addrInVT)
        isText = what >= text.start.offset and what <= text.end.offset
        isExternal = what >= external.start.offset and what <= external.end.offset
        if isText:
            whatAddr = toAddr(what)
            if getFunctionAt(whatAddr) is None:
                createFunction(whatAddr, None)
            if funcUsageCount[what] == 1:
                methSym = getSymbolAt(whatAddr)
                if methSym.name.startswith('FUN_'):
                    methSym.setNameAndNamespace('vf%02x' % i, ns, SourceType.ANALYSIS)


# introspect all RTTI stuff

# RTTI in sead:
#   sead::RuntimeTypeInfo::Root vtable contains isDerived method
#     cmp x0,x1; cset w0,eq; ret
#   




