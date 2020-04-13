# this should really be merged with BuildRTTIHierarchy.py

def identifyFunc(fn):
	# we need to figure out what sort of function this is
	firstInsn = getInstructionAt(fn.entryPoint)
	if firstInsn.mnemonicString == 'cmp':
		print('probably not what we want: %r' % fn)
		return ('', None)

	# so this could be isDerivedFrom, or getTypeInfo
	addr = fn.entryPoint
	chain = []
	while True:
		insn = getInstructionAt(addr)
		if insn is None:
			print('none insn?? in identifyFunc? %r' % addr)

		if insn.mnemonicString == 'ret':
			if chain:
				return ('derived', chain)
			elif insn.previous.previous.mnemonicString == 'ldr' and insn.previous.mnemonicString == 'ldp':
				info = getDataAt(insn.previous.previous.referencesFrom[0].toAddress).value
				return ('typeinfo', info)
			else:
				return ('', None) #bad news
		if insn.mnemonicString == 'cmp' and insn.previous.mnemonicString == 'ldr':
			refs = insn.previous.referencesFrom
			if not refs: return('', None)
			info = getDataAt(refs[0].toAddress).value
			chain.append(info)
		if insn.mnemonicString == 'b':
			return ('', None) #bad news

		addr = addr.add(4)



base_typeInfo = toAddr('BcsvReader_typeInfo')
baseName = 'BcsvReader'
identified = set()
used_names = set()
names = {}
vtables = {}
bases = {}
known_chains = []
classes_in_order = []

def pick_name(n):
	if n not in used_names:
		used_names.add(n)
		return n
	n += 'Sub'
	if n not in used_names:
		used_names.add(n)
		return n
	for i in xrange(1,100):
		candidate = '%s%d' % (n, i)
		if candidate not in used_names:
			used_names.add(candidate)
			return candidate


refs = getReferencesTo(base_typeInfo)
for ref in refs:
	if ref.referenceType.write:
		fn = getFunctionContaining(ref.fromAddress)
		what, details = identifyFunc(fn)
		if what == 'derived':
			# we have a chain
			known_chains.append(details)
		elif what == 'typeinfo':
			# we have a getTypeInfo function
			info = details
			gtiRefs = getReferencesTo(fn.entryPoint)
			assert(len(gtiRefs) == 1)
			vtables[info] = gtiRefs[0].fromAddress.subtract(8)
			names[info] = baseName
			identified.add(info)
			classes_in_order.append(info)

# now pull out names for as many as we can
for chain in known_chains:
	base = None
	for info in reversed(chain):
		bases[info] = base
		base = info
		if info in identified: continue

		# find the getTypeInfo function
		for ref in getReferencesTo(info):
			if ref.referenceType.write:
				fn = getFunctionContaining(ref.fromAddress)
				if identifyFunc(fn)[0] == 'typeinfo':
					gtiRefs = getReferencesTo(fn.entryPoint)
					#assert(len(gtiRefs) == 1)
					vtables[info] = gtiRefs[0].fromAddress.subtract(8)
					identified.add(info)
					classes_in_order.append(info)
					break

		vtable = vtables[info]
		#print('found vtable for %r at %r' % (info, vtable))

		getName = toAddr(getLong(vtable.add(0x30)))
		#print('getName is %r' % getName)
		assert(getInstructionAt(getName).mnemonicString == 'adrp')
		assert(getInstructionAt(getName.add(4)).mnemonicString == 'ldr')
		assert(getInstructionAt(getName.add(8)).mnemonicString == 'ldr')
		assert(getInstructionAt(getName.add(12)).mnemonicString == 'ret')
		strAddr = getInstructionAt(getName.add(8)).referencesFrom[0].toAddress
		strAddr = getDataAt(strAddr).value
		name = pick_name(getDataAt(strAddr).value.replace('.bcsv', ''))
		names[info] = name
		#print('addr is %r' % strAddr)
		#print('name is %s' % name)

# now print everything
for chain in known_chains:
	print(' -> '.join([names[info] for info in reversed(chain)]))

already_named = set()
def applyVtable(vtable, clsname, methnames):
	for i,name in enumerate(methnames):
		meth = getLong(vtable.add(i * 8))
		if meth == 0:
			break
		meth = toAddr(meth)
		if meth in already_named:
			continue
		#print(repr(meth))
		if getSymbolAt(meth).name == '__cxa_pure_virtual':
			continue
		fullname = '%s_%s' % (clsname, name)
		fn = getFunctionAt(meth)
		if (getInt(meth)&0xFFFFFFFF) != 0xE7FFDEFE:
			if fn is None:
				createFunction(meth, fullname)
			else:
				fn.setName(fullname, ghidra.program.model.symbol.SourceType.DEFAULT)
		already_named.add(meth)


dtmgr = currentProgram.dataTypeManager
category = ghidra.program.model.data.CategoryPath('/bcsv')

# and apply all these names
for info in classes_in_order:
	name = names[info]
	vtable = vtables[info]
	createLabel(info, '%s_typeInfo' % name, True)
	createLabel(vtable, '%s_vtable' % name, True)
	applyVtable(vtable, name, ('isDerivedFrom', 'getTypeInfo', 'dtor', 'dtorDeleting', 'vf20', 'vf28', 'getName', 'deallocBuffers', 'populateBuffers'))

	if dtmgr.getDataType(category, name) is None:
		print('Gonna add %s' % name)
		typ = ghidra.program.model.data.StructureDataType(category, name, 0, dtmgr)
		baseType = dtmgr.getDataType(category, names[bases[info]])
		typ.add(baseType, 0, 'base', '')
		handler = ghidra.program.model.data.DataTypeConflictHandler.ConflictResolutionPolicy.RENAME_AND_ADD.handler
		dtmgr.addDataType(typ, handler)


