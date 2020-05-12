from ghidra.program.model.symbol import SourceType

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

symbol = getSymbolAt(currentAddress)
if symbol:
	namespace = symbol.parentNamespace
	if not namespace.global:
		path = '::'.join(namespace.symbol.path)
		newPath = askString('new name', 'enter new name', path)
		if newPath != path:
			newParentNS, newSymName = resolveIt(newPath)
			print('sticking it into %r, %r' % (newParentNS, newSymName))
			if getNamespace(newParentNS, newSymName) != None:
				print('already exists')
			else:
				if newParentNS != namespace.parentNamespace:
					namespace.setParentNamespace(newParentNS)
				if namespace.symbol.name != newSymName:
					namespace.symbol.setName(newSymName, SourceType.USER_DEFINED)


