# time for some fun
from ghidra.app.plugin.core.navigation.locationreferences import ReferenceUtils
from ghidra.program.model.symbol import SourceType

s_text = getMemoryBlock('.text')
s_init_array = getMemoryBlock('.init_array')
s_rodata = getMemoryBlock('.rodata.1') # not sure if it's .1 in all bins?
s_data = getMemoryBlock('.data')

def get_all_inits():
	addr = s_init_array.start
	while addr < s_init_array.end:
		yield getDataAt(addr).value
		addr = addr.add(8)


def do_all_inits():
	num = 0
	for ptr in get_all_inits():
		if getInstructionAt(ptr) is None:
			disassemble(ptr)
		if getFunctionAt(ptr) is None:
			createFunction(ptr, None)
		fn = getFunctionAt(ptr)
		if fn.name.startswith('FUN_'):
			fn.setName('Init%04d_130' % num, ghidra.program.model.symbol.SourceType.DEFAULT)
		num += 1



def remove_all_spurious_data():
	addr = s_text.start
	while addr < s_text.end:
		removeDataAt(addr)
		addr = addr.add(1)


def nops_following_ret(addr):
	if getInt(addr.subtract(4))&0xFFFFFFFF == 0xd65f03c0:
		while (addr.offset & 0xF) != 0:
			if getInt(addr)&0xFFFFFFFF != 0xd503201f:
				return False
			addr = addr.add(4)
		return True
	return False


# assume that the first fn is defined, probably at 7100000030
def locate_undefined_candidates(start):
	addr = start
	while addr < s_text.end:
		oaddr = addr
		c1 = getUndefinedDataAfter(addr).address
		c2 = getDataAfter(addr).address
		addr = c1 if (c1 < c2) else c2
		if addr >= s_text.end:
			break
		if (addr.offset & 0xF) != 0:
			# not aligned
			addrval = getInt(addr)&0xFFFFFFFF
			if addrval == 0xd61f0140:
				# br x10, for switch tables Ghidra fails to identify
				disassemble(addr)
				continue
			elif addrval == 0 or addrval == 0xE7FFDEFE or nops_following_ret(addr):
				addr = addr.add(0x10 - (addr.offset & 0xF))
			else:
				#print('found unaligned non-zeroes @ %r, what' % addr)
				#print('our old addr was %r, c1=%r, c2=%r' % (oaddr, c1, c2))
				#return oaddr
				disassemble(addr)


		if getInt(addr) == 0:
			print('found aligned zeroes @ %r' % addr)
			return
		else:
			if getInstructionAt(addr) == None:
				print('possible code @ %r' % addr)
				if getInt(addr)&0xFFFFFFFF == 0xE7FFDEFE:
					addr = addr.add(4)
				else:
					disassemble(addr)


def force_eliminate_data(addr, count):
	for i in xrange(count):
		d = getDataContaining(addr.add(i))
		if d is not None:
			removeData(d)

def is_pointer_at_addr(addr):
	data = getDataAt(addr)
	if data is None:
		return False
	else:
		return data.isPointer()

def scan_data_for_code_ptrs():
	found = 0
	addr = s_data.start
	end = s_data.end.subtract(7)
	ts, te = s_text.start.offset, s_text.end.offset
	while addr < end:
		val = getLong(addr)
		if val >= ts and val < te and not is_pointer_at_addr(addr):
			print('unreffed pointer into .text @ %r -> %x' % (addr, val))
			clearListing(addr, addr.add(7))
			createData(addr, ghidra.program.model.data.Pointer64DataType())
			found += 1
			#if found > 20: break
		addr = addr.add(8)

def findEvFlowVtable(ctor):
	body = getFunctionAt(ctor).body
	candidates = []
	for addr in body.getAddresses(True):
		for ref in getReferencesFrom(addr):
			rt = ref.referenceType
			if rt.data and not rt.read and not rt.write and ref.operandIndex == 0 and ref.isMemoryReference() and getDataAt(ref.toAddress).isPointer():
				return ref.toAddress


def find_init(addr):
	for check in inits:
		if addr < check:
			return check


vtables_to_names = {}
#missinga = open('/Users/ash/src/hashcat/missing_actions', 'w')
#missingq = open('/Users/ash/src/hashcat/missing_queries', 'w')
	

def name_eventflow_classes(path):
	'''import json
	with open(path, 'r') as f:
		data = json.load(f)
	queries, actions = {}, {}
	for ac in data.values():
		for q,k in ac['queries'].iteritems(): queries[k] = q
		for a,k in ac['actions'].iteritems(): actions[k] = a'''
	path = '/Users/ash/src/hashcat'
	queries, actions = {}, {}
	for line in open(path+'/actions_cracked', 'r'):
		line = line.strip()
		if line:
			a,b,c = line.split(':')
			actions[int(a,16)] = c
	for line in open(path+'/queries_cracked', 'r'):
		line = line.strip()
		if line:
			a,b,c = line.split(':')
			queries[int(a,16)] = c

	for names,baseaddr,what in ((queries,'eventFlowQueryMap','Query'), (actions,'eventFlowActionMap','Action')):
		in_exec = set()
		missing = set()
		qmap = getDataAt(toAddr(baseaddr))
		count = qmap.length//16
		#count = 3
		for i in xrange(count):
			key = getInt(qmap.address.add(i * 16)) & 0xFFFFFFFF
			if key in names:
				#print('found %s' % names[key])
				in_exec.add(key)
				name = names[key]
			else:
				#print('missing %08x!' % key)
				missing.add(key)
				name = 'EventFlow%s%08X' % (what, key)
				if what == 'Query':
					missingq.write('%08x:00000000\n' % key)
				else:
					missinga.write('%08x:00000000\n' % key)
			addr = toAddr(getLong(qmap.address.add(i * 16 + 8)))
			#getFunctionAt(addr).setName(name + '_build', ghidra.program.model.symbol.SourceType.DEFAULT)

			# find ctor
			ctor = getReferencesFrom(addr.add(0x24))[0].toAddress
			#print('ctor %s = %r' % (name, ctor))
			#getFunctionAt(ctor).setName(name + '_ctor', ghidra.program.model.symbol.SourceType.DEFAULT)

			# find vtable
			vt = findEvFlowVtable(ctor)
			#createLabel(vt, name+'_vtable', True)
			vtables_to_names[vt.offset] = name
			vtsym = getSymbolAt(vt)
			vtns = vtsym.parentNamespace
			#print('vt %r is %r' % (name,vtns))

			if vtns.name != name:
				print('would rename %r to %r' % (vtns,name))
				vtns.symbol.setName(name, SourceType.ANALYSIS)

			init = find_init(ctor)
			#print('%r goes with %r' % (vtns, getFunctionAt(init)))
			initmap[init].append(vtns)

		#in_json = set(names.keys())
		#noted = in_json - in_exec
		#for n in noted:
		#	print('missing %s from exec table but in json: %s' % (what, names[n]))


# STEP 1: mark all init functions
#do_all_inits()
# STEP 2: remove all spurious data from the .text section
#remove_all_spurious_data()
# STEP 3: disassemble all code
#locate_undefined_candidates(getFirstFunction().entryPoint)
# STEP 4: set all code ptrs (vtables, etc) to actual references
scan_data_for_code_ptrs()
# STEP 5: use the FindInstructionsNotInsideFunctionScript and CreateFunctionsFromSelection scripts

'''
inits = list(get_all_inits())
addr = s_init_array.start
for i in xrange(len(inits) - 1):
	a = inits[i]
	b = inits[i + 1]
	delta = getFunctionAt(b).body.minAddress.subtract(getFunctionAt(a).body.maxAddress) - 1
	if delta < 0x10:
		setEOLComment(addr.add(8 + i * 8), '-')
	else:
		setEOLComment(addr.add(8 + i * 8), '0x%x' % delta)

initmap = {}
for init in inits:
	initmap[init] = []
'''

# STEP 6: set up some eventflow stuff
#name_eventflow_classes('/Volumes/HFS/repos/switch/CylindricalEarth/evfl/evflActors120.json')
#import json
#with open('/Volumes/HFS/repos/switch/CylindricalEarth/evfl/eventflow_vtables.json', 'w') as f:
#	json.dump(vtables_to_names, f)

'''
for init in inits:
	if len(initmap[init]) > 1:
		print(getFunctionAt(init))
		for i in initmap[init]:
			print(i)
	elif len(initmap[init]) == 1:
		ns = initmap[init][0]
		initsym = getSymbolAt(init)
		if initsym.name != 'STATIC_INIT_':
			initsym.setNameAndNamespace('STATIC_INIT_', ns, SourceType.USER_DEFINED)
'''

#missingq.close()
#missinga.close()

#addr = getFirstFunction().entryPoint
#while True:
#	new_addr = locate_undefined_candidates(getFirstFunction().entryPoint)
#	if new_addr is None:
#		print('all done?')
#		break
#	if new_addr == addr:
#		print('might\'ve fucked it')
#		break
#	addr = new_addr
#	print('wait...')
#	analyzeChanges(currentProgram)
