# Remember to make sure ALL the bcsv classes are defined
# search for xrefs to .bcsv
# find the function that returns the name
# find the vtable containing it
# expand the function 2 entries after that

memcpy = toAddr('memcpy')
cxa_guard_release = toAddr('__cxa_guard_release')

results = {}

def readStr(addr):
	bits = []
	while True:
		c = getByte(addr)
		if c == 0:
			return ''.join(bits)
		else:
			bits.append(chr(c&0xFF))
			addr = addr.add(1)

def track_jpe_cond_call(jpe_call_addr):
	print(jpe_call_addr)
	jpe_call = getInstructionAt(jpe_call_addr)
	after = jpe_call.getNext()
	print(after)
	if after.mnemonicString == 'tbz':
		# points to JP
		jp = find_enum(getInstructionAt(after.getOpObjects(2)[0]))
		en = find_enum(after.getNext())
	elif after.mnemonicString == 'tbnz':
		# points to EN
		en = find_enum(getInstructionAt(after.getOpObjects(2)[0]))
		jp = find_enum(after.getNext())
	else:
		raise '???'
	print('EN STR: %r / JP STR: %r' % (en, jp))

	jpe_call_fn = getFunctionContaining(jpe_call_addr)
	bignums = []
	for i in currentProgram.getListing().getCodeUnits(jpe_call_fn.getBody(), True):
		if i.mnemonicString == 'movk':
			reg = i.getRegister(0).name
			prev = i.getPrevious()
			assert prev.mnemonicString == 'mov'
			assert prev.getRegister(0).name == reg
			hi_val = i.getOpObjects(1)[0].value
			lo_val = prev.getOpObjects(1)[0].value
			val = lo_val | (hi_val << 16)
			bignums.append(val)
	assert len(bignums) == 1

	bcsv_name = search_bcsv_name(jpe_call_fn.getBody().getMinAddress())
	if bcsv_name is None:
		bcsv_name = '_UNKNOWN_'
	else:
		bcsv_name = readStr(bcsv_name)

	key = bignums[0]
	strs = (readStr(en).decode('utf-8').rstrip(',').split(','), readStr(jp).decode('utf-8').rstrip(',').split(','))
	if bcsv_name not in results:
		results[bcsv_name] = {}
	if key in results[bcsv_name]:
		assert results[bcsv_name][key] == strs
	else:
		results[bcsv_name][key] = strs

def search_bcsv_name(func_start):
	for ref in getReferencesTo(func_start):
		t = None
		if getInstructionAt(ref.fromAddress):
			print('search %r' % ref)
			fn = getFunctionContaining(ref.fromAddress)
			if fn:
				t = search_bcsv_name(fn.getBody().getMinAddress())
			else:
				# find start of fn manually
				i = getInstructionAt(ref.fromAddress)
				while True:
					prev = i.getPrevious()
					diff = i.address.subtract(prev.address)
					if diff > 4:
						# this must be the start
						t = search_bcsv_name(i.address)
						break
					i = prev
		else:
			t = parse_bcsv_vfunc(ref.fromAddress.subtract(16))
		if t:
			return t
	print('failed!!')

def parse_bcsv_vfunc(addr):
	print('found vfunc reffed by %r' % addr)
	addr = toAddr(getDataAt(addr).getLong(0))
	i = getInstructionAt(addr)
	assert i.mnemonicString == 'adrp'
	i = i.getNext()
	assert i.mnemonicString == 'ldr'
	i = i.getNext()
	assert i.mnemonicString == 'ldr'
	assert i.getNext().mnemonicString == 'ret'
	return getReferencesFrom(i.address)[-1].toAddress

def find_enum(call_start):
	if call_start.mnemonicString == 'b':
		call_start = getInstructionAt(call_start.getOpObjects(0)[0])
	print('ENUM EXPECTED AT %r' % call_start.address)
	assert call_start.mnemonicString == 'mov'
	mov_x1 = call_start.getNext()
	assert mov_x1.mnemonicString == 'mov'
	bl = mov_x1.getNext()
	assert bl.mnemonicString == 'bl'

	return handle_enum_splitter(getFunctionAt(bl.getOpObjects(0)[0]))

def handle_enum_splitter(fn):
	print('ENUM SPLITTER AT %r' % fn)
	bls_seen = []
	for insn in currentProgram.getListing().getCodeUnits(fn.getBody(), True):
		if insn.mnemonicString == 'bl':
			bls_seen.append(insn.getOperandReferences(0)[0].toAddress)
	print(bls_seen)
	for i, f in enumerate(bls_seen):
		if f == cxa_guard_release:
			return handle_enum_getter(getFunctionAt(bls_seen[i + 1]))
	print('FAILED TO FIND ENUM GETTER')

def handle_enum_getter(fn):
	print('ENUM GETTER AT %r' % fn)
	for insn in currentProgram.getListing().getCodeUnits(fn.getBody(), True):
		if insn.mnemonicString == 'bl' and insn.getOperandReferences(0)[0].toAddress == memcpy:
			print('FOUND MEMCPY @ %r' % insn.address)
			add_x1 = insn.getPrevious().getPrevious().getPrevious()
			assert add_x1.mnemonicString == 'add'
			assert add_x1.getRegister(0).name == 'x1'
			return getReferencesFrom(add_x1.address)[0].toAddress
	print('FAILED TO FIND MEMCPY')

for ref in getReferencesTo(toAddr('BcsvHeader_isJPEnums')):
	track_jpe_cond_call(ref.fromAddress)

import json
with open('bcsv_enum_results.json', 'w') as f:
	json.dump(results, f, indent=4, sort_keys=True)

