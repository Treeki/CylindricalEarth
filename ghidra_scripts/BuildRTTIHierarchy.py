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
			addr = insn.referencesFrom[0].toAddress
			continue
			#toWhere = insn.referencesFrom[0].toAddress
			#if getFunctionContaining(toWhere) == fn:
			#	addr = toWhere
			#	continue
			#else:
			#	return ('', None) #bad news

		addr = addr.add(4)


def nameStrategyBCSV(vtable):
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

import json
ct = 0
with open('/Volumes/HFS/repos/switch/CylindricalEarth/evfl/eventflow_vtables.json', 'r') as f:
	vtables_to_names = json.load(f)
def nameStrategyEVFLReceptor(vtable, is_info=False):
	if is_info:
		return ('EVFLReceptorMissingType%x' % vtable.offset)

	try:
		return vtables_to_names[str(vtable.offset)]
	except KeyError:
		symbol = getSymbolAt(vtable)
		if symbol and symbol.name.endswith('_vtable'):
			return symbol.name[:-7]
		else:
			global ct
			ct = ct + 1
			return ('EVFLReceptorUnk%d' % ct)

base_typeInfo = toAddr('EVFLReceptor_typeInfo')
baseName = 'EVFLReceptor'
nameStrategy = nameStrategyEVFLReceptor

vtableAppend = {
	'EVFLReceptor': ('isDerivedFrom', 'getTypeInfo', 'dtor', 'dtorDeleting', 'vf20', 'vf28'),
	'EVFLReceptorAction': ('actVf30r', 'actVf38r', 'actVf40', 'actVf48', 'actVf50', 'actVf58'),
	'EVFLReceptorQuery': ('queryVf30r',),
}

identified = set()
used_names = set()
names = {}
vtables = {}
bases = {}
children = {}
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


to_check = [base_typeInfo]
already_checked = set()
while to_check:
	reftarget = to_check.pop(0)
	already_checked.add(reftarget)
	refs = getReferencesTo(reftarget)
	for ref in refs:
		if ref.referenceType.write or (ref.referenceType.call and not ref.referenceType.computed):
			fn = getFunctionContaining(ref.fromAddress)
			what, details = identifyFunc(fn)
			#if fn.entryPoint == toAddr(0x710026cec0):
			#	print(what, details)
			if ref.fromAddress == toAddr(0x710024ed14):
				print('foundit2: %r,%r' % (what, details))
			if fn.entryPoint == toAddr(0x71002eba40):
				print('foundit2: %r,%r' % (what, details))
			if what == 'derived':
				# we have a chain
				known_chains.append(details)
				if fn.entryPoint not in already_checked:
					to_check.append(fn.entryPoint)
			elif what == 'typeinfo':
				# we have a getTypeInfo function
				info = details
				gtiRefs = getReferencesTo(fn.entryPoint)
				assert(len(gtiRefs) == 1)
				vtables[info] = gtiRefs[0].fromAddress.subtract(8)
				names[info] = baseName
				children[info] = []
				identified.add(info)
				classes_in_order.append(info)
			else:
				print('can\'t figure out %r <%r>' % (fn, ref))
		#if ref.referenceType.call:
		#	if ref.fromAddress not in already_checked:
		#		fn = getFunctionContaining(ref.fromAddress)
		#		if getInstructionAt(fn.entryPoint).mnemonicString == '

# now pull out names for as many as we can
for chain in known_chains:
	base = None
	for info in reversed(chain):
		#print(info)
		if info == toAddr(0x71034ff898):
			print('foundit')
		bases[info] = base
		base = info
		if info in identified: continue
		if bases[info]:
			children[bases[info]].append(info)
		children[info] = []

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

		if info in vtables:
			vtable = vtables[info]
			names[info] = nameStrategy(vtable)
			#print('found vtable for %r at %r <%s>' % (info, vtable, names[info]))
		else:
			print('!!! failed to find vtable for %r !!!' % info)
			names[info] = nameStrategy(info, True)
			createLabel(info, '%s_typeInfo' % names[info], True)
			identified.add(info)


# now print everything
#for chain in known_chains:
#	print(' -> '.join([names[info] for info in reversed(chain)]))

already_named = set()
def applyVtable(vtable, clsname, info):
	methnames = []
	while info:
		if names[info] in vtableAppend:
			methnames[:0] = vtableAppend[names[info]]
		info = bases[info]
	for i,name in enumerate(methnames):
		meth = getLong(vtable.add(i * 8))
		if meth == 0:
			break
		meth = toAddr(meth)
		if meth in already_named:
			continue
		#print(repr(meth))
		if not getDataAt(vtable.add(i * 8)).isPointer():
			break
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
category = ghidra.program.model.data.CategoryPath('/evfl')

# and apply all these names
for info in classes_in_order:
	name = names[info]
	vtable = vtables[info]
	createLabel(info, '%s_typeInfo' % name, True)
	createLabel(vtable, '%s_vtable' % name, True)
	applyVtable(vtable, name, info)

	#if dtmgr.getDataType(category, name) is None:
	#	print('Gonna add %s' % name)
	#	typ = ghidra.program.model.data.StructureDataType(category, name, 0, dtmgr)
	#	baseType = dtmgr.getDataType(category, names[bases[info]])
	#	typ.add(baseType, 0, 'base', '')
	#	handler = ghidra.program.model.data.DataTypeConflictHandler.ConflictResolutionPolicy.RENAME_AND_ADD.handler
	#	dtmgr.addDataType(typ, handler)

def print_tree(info, prefix=''):
	print('%s+ %s' % (prefix, names[info]))
	prefix += '  '
	for child in sorted(children[info]):
		print_tree(child, prefix)

print()
print()
print()
print_tree(base_typeInfo)

