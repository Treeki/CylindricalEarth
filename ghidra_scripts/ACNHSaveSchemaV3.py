from ghidra.program.model.data import StructureDataType
from ghidra.program.model.data import ArrayDataType
handler = ghidra.program.model.data.DataTypeConflictHandler.ConflictResolutionPolicy.RENAME_AND_ADD.handler

import json
with open('/Volumes/HFS/repos/switch/CylindricalEarth/savefile/save_schema_120_109.json', 'r') as f:
	stuff = json.load(f)
with open('/Volumes/HFS/repos/switch/CylindricalEarth/savefile/save_io_structure.json', 'r') as f:
	sioData = json.load(f)


dtmgr = currentProgram.dataTypeManager

# build out everything
saveCatPath = ghidra.program.model.data.CategoryPath('/Save')
saveCat = dtmgr.getCategory(saveCatPath)

sioCatPath = ghidra.program.model.data.CategoryPath('/SaveIO')
sioCat = dtmgr.getCategory(sioCatPath)

typeMap = {}
sioMap = {}

# pull out all existing ones
for dt in saveCat.dataTypes:
	if dt.description.startswith('saveschema '):
		key = int(dt.description[11:19], 16)
		typeMap[key] = dt
for dt in sioCat.dataTypes:
	if dt.description.startswith('saveio '):
		key = int(dt.description[7:15], 16)
		sioMap[key] = dt
	if dt.description.startswith('sioarray '):
		key = int(dt.description[9:17], 16)
		sioMap[key] = dt

# populate primitives
primMap = {
	'bool': '/bool',
	's8': '/char',
	'u8': '/byte',
	's16': '/short',
	'u16': '/ushort',
	's32': '/int',
	'u32': '/uint',
	's64': '/longlong',
	'u64': '/ulonglong',
	'f32': '/float',
	'f64': '/double',
	'char16': '/char16',
	'V3f': '/V3f'
}

for key, primitive in stuff['primitives'].iteritems():
	key = int(key)
	print('key:%x -> prim:%r' % (key, primitive))
	if primitive['name'] in primMap:
		dt = dtmgr.getDataType(primMap[primitive['name']])
		assert dt != None
		assert dt.length == primitive['size']
		print('resolved to %r' % dt)
		typeMap[key] = dt
	elif key not in typeMap:
		print('creating type')
		dt = StructureDataType(saveCatPath, 'SP' + primitive['name'], primitive['size'], dtmgr)
		dt.description = 'saveschema %08x' % key
		dtmgr.addDataType(dt, handler)
		typeMap[key] = dt
	else:
		if typeMap[key].name != 'SP' + primitive['name']: typeMap[key].name = 'SP' + primitive['name']


for key, typ in stuff['types'].iteritems():
	key = int(key)
	print('key:%x -> struct:%s' % (key, typ['name']))
	name = typ['name']
	if name.startswith('::Game::Save'):
		name = 'GS' + name[12:]
	elif name.startswith('::Game::'):
		name = 'G' + name[8:]
	else:
		name = 'GSUnk' + name

	if key not in typeMap:
		print('creating struct type')
		dt = StructureDataType(saveCatPath, name, typ['size'], dtmgr)
		dt.description = 'saveschema %08x' % key
		dtmgr.addDataType(dt, handler)
		typeMap[key] = dt
	else:
		if typeMap[key].name != name: typeMap[key].name = name

# now all the types are IN
for key, typ in stuff['types'].iteritems():
	key = int(key)
	dt = typeMap[key]
	for field in typ['fields']:
		comp = dt.getComponentAt(field['offset'])
		print('checking field %s at %d' % (field['name'], field['offset']))
		if not comp.fieldName:
			print('replacing field %s' % field['name'])
			fdt = typeMap[field['type']]
			if field['length'][1] > 1:
				fdt = ArrayDataType(fdt, field['length'][1], 0, dtmgr)
			if field['length'][0] > 1:
				fdt = ArrayDataType(fdt, field['length'][0], 0, dtmgr)
			cmt = 'id=%08x ty=%08x' % (field['id'], field['type'])
			dt.replaceAtOffset(field['offset'], fdt, 0, field['name'], cmt)
		else:
			comp.fieldName = field['name'] # justin case,


# finally, generate all of the nodes
nodeDT = dtmgr.getDataType('ac114_try2/auto_structs/SaveNode')

for key, sioInfo in sioData.iteritems():
	try:
		name = stuff['types'][key]['name']
	except KeyError:
		name = stuff['primitives'][key]['name']
	key = int(key)

	if name.startswith('::Game::Save'):
		name = 'SIOS' + name[12:]
	elif name.startswith('::Game::'):
		name = 'SIO' + name[8:]
	else:
		name = 'SIOUnk' + name

	if key not in sioMap:
		print('creating SIO type')
		dt = StructureDataType(sioCatPath, name, sioInfo['size'], dtmgr)
		dt.description = 'saveio %08x vt=%10x' % (key, sioInfo['vtable'])
		dt.replaceAtOffset(0, nodeDT, 0, 'node', '')
		dtmgr.addDataType(dt, handler)
		sioMap[key] = dt
	else:
		if sioMap[key].name != name: sioMap[key].name = name

	# get that vtable named while we're at it
	vtAddr = toAddr(sioInfo['vtable'])
	vtSym = getSymbolAt(vtAddr)
	vtname = name + '_vtable'
	if vtSym.name != vtname:
		print('updating vtable name for %s' % vtname)
		vtSym.delete()
		createLabel(vtAddr, vtname, True)

# and fill those boys in with some fields
def findField(typ, id):
	for field in typ['fields']:
		if field['id'] == id:
			return field

def makeSioArray(fdt, length, vtbl):
	dt = StructureDataType(sioCatPath, 'SIOArray%10x' % vtbl, 0, dtmgr)
	dt.description = 'sioarray %10x' % vtbl
	dt.add(nodeDT, 0, 'node', '')
	if length[1] > 1:
		fdt = ArrayDataType(fdt, length[1], 0, dtmgr)
	if length[0] > 1:
		fdt = ArrayDataType(fdt, length[0], 0, dtmgr)
	dt.add(fdt, 0, 'elements', '')
	dtmgr.addDataType(dt, handler)
	sioMap[vtbl] = dt

for key, sioInfo in sioData.iteritems():
	if key in stuff['types']:
		typ = stuff['types'][key]
		key = int(key)
		dt = sioMap[key]

		for subnode in sioInfo['subnodes']:
			field = findField(typ, subnode['id'])
			comp = dt.getComponentAt(subnode['offset'])
			if not comp.fieldName:
				if 'arrayVtable' in subnode:
					if subnode['arrayVtable'] not in sioMap:
						makeSioArray(sioMap[field['type']], field['length'], subnode['arrayVtable'])
					subDT = sioMap[subnode['arrayVtable']]
				else:
					subDT = sioMap[field['type']]
				dt.replaceAtOffset(subnode['offset'], subDT, 0, field['name'], 'origOffset=%x, size=%x' % (field['offset'], field['size']))
			else:
				comp.fieldName = field['name'] # justin case, (2)

