import bcsv
import json
import os
import sys

print('from bcsv import *')
print()

type_overrides = {
	# StructureFacilityModel
	0x88ff5893: 'Float',
	0x6efc082c: 'Float',
}

preset_names = {
	0x54706054: 'id',
	0x87bf00e8: 'name',
	0x85cf1615: 'name_jp',
	0x45f320f2: 'name_en',

	# mystery tours
	0x7a09986c: 'item_param_id',
	0x72573f73: 'field_param_id',
	0xe23c6453: 'insect_param_id',
	0xb1f384dc: 'fish_param_id',
	0xbc5f2a7b: 'item_req_1',
	0x813f03cb: 'item_req_2',
	0x4e5cd9fc: 'player_flag_req',
	0x88bd09c2: 'player_flag_set',
	0x7215b154: 'land_req',
	0xd89a0db0: 'chance',

	# field outside template
	0xd094759a: 'nw',
	0x1ed42314: 'n1',
	0x7bb31852: 'n2',
	0xd41a5598: 'n3',
	0xb17d6ede: 'n4',
	0x5039c84d: 'n5',
	0xfa9ca833: 'ne',
	0xef18bb10: 'w1',
	0x8a7f8056: 'w2',
	0x25d6cd9c: 'w3',
	0x40b1f6da: 'w4',
	0x19a9348c: 'se',
	0x4038a881: 'e1',
	0x255f93c7: 'e2',
	0x8af6de0d: 'e3',
	0xef91e54b: 'e4',
	0x33a1e925: 'sw',
	0xfde1bfab: 's1',
	0x988684ed: 's2',
	0x372fc927: 's3',
	0x5248f261: 's4',
	0xb30c54f2: 's5',

	# appear params
	0x20cb67bc: 'insect_id',
	0x655e327e: 'apr0816',
	0x57d5055c: 'apr1617',
	0x10757f8c: 'apr1719',
	0x77c808ae: 'apr2304',
	0x93a0aeb8: 'apr0408',
	0xd420d79d: 'apr1923',
	0xf588704d: 'aug0816',
	0xe895b208: 'aug1617',
	0xaf35c8d8: 'aug1719',
	0xc888bffa: 'aug2304',
	0x0376ec8b: 'aug0408',
	0x8d40260e: 'aug1923',
	0x995763a6: 'dec0816',
	0xdf2156eb: 'dec1617',
	0x98812c3b: 'dec1719',
	0xff3c5b19: 'dec2304',
	0x6fa9ff60: 'dec0408',
	0xdd1caee7: 'dec1923',
	0x4026fbe1: 'feb0816',
	0x3740f340: 'feb1617',
	0x70e08990: 'feb1719',
	0x175dfeb2: 'feb2304',
	0xb6d86727: 'feb0408',
	0x78a12603: 'feb1923',
	0x65270095: 'jan0816',
	0x600d479e: 'jan1617',
	0x27ad3d4e: 'jan1719',
	0x40104a6c: 'jan2304',
	0x93d99c53: 'jan0408',
	0x3a737394: 'jan1923',
	0x813dbbdc: 'jul0816',
	0x6fe9a411: 'jul1617',
	0x2849dec1: 'jul1719',
	0x4ff4a9e3: 'jul2304',
	0x77c3271a: 'jul0408',
	0x4f6db088: 'jul1923',
	0xe873aeea: 'jun0816',
	0xa03a7f9d: 'jun1617',
	0xe79a054d: 'jun1719',
	0x8027726f: 'jun2304',
	0x1e8d322c: 'jun0408',
	0x2a93682f: 'jun1923',
	0x06bcf848: 'mar0816',
	0x980c720f: 'mar1617',
	0xdfac08df: 'mar1719',
	0xb8117ffd: 'mar2304',
	0xf042648e: 'mar0408',
	0x7c00c111: 'mar1923',
	0xaebc09bc: 'may0816',
	0x227444fb: 'may1617',
	0x65d43e2b: 'may1719',
	0x02694909: 'may2304',
	0x5842957a: 'may0408',
	0x8feba08a: 'may1923',
	0x1538c8ac: 'nov0816',
	0x3f78d05e: 'nov1617',
	0x78d8aa8e: 'nov1719',
	0x1f65ddac: 'nov2304',
	0xe3c6546a: 'nov0408',
	0x6c66ea56: 'nov1923',
	0xa09fb609: 'oct0816',
	0x99712047: 'oct1617',
	0xded15a97: 'oct1719',
	0xb96c2db5: 'oct2304',
	0x56612acf: 'oct0408',
	0xdac2c157: 'oct1923',
	0x9ebf2c04: 'sep0816',
	0xe7fe7c60: 'sep1617',
	0xa05e06b0: 'sep1719',
	0xc7e37192: 'sep2304',
	0x6841b0c2: 'sep0408',
	0x339772b5: 'sep1923',
	0x137dd804: 'hemisphere',
}
preset_enum_names = {
	0x9b7aa0a0: 'enum_GroundedItemType',
	0x19a9348c: 'enum_OuterMapChunkType',
	0xd5a8bf7e: 'enum_CompassNESW',
	0x7dcd5be1: 'enum_NoneHighNormalLow',
	0x64330cb0: 'enum_CompassNS',
	0xf80e9fee: 'enum_GenderBias',
	0xdda5d566: 'enum_TwoGenders',
}

def print_enum(prefix, enum):
	en_names, jp_names = enum
	en_names = list(map(repr, en_names))
	jp_names = list(map(repr, jp_names))
	max_len = max(map(len, en_names))
	for e, j in zip(en_names, jp_names):
		print('%s(%s, %s),' % (prefix, e.ljust(max_len), j))

path = sys.argv[1]
files = os.listdir(path)

enum_uses = {}
shared_enums = []
shared_enum_names = []
enum_remaps = {}
assigned_names = set()

def assign_name(key):
	try:
		base = preset_enum_names[key]
	except KeyError:
		base = 'enum_%08x' % key
	if base not in assigned_names:
		assigned_names.add(base)
		return base
	else:
		for i in range(1, 1000):
			name = '%s_%03d' % (base, i)
			if name not in assigned_names:
				assigned_names.add(name)
				return name

with open('all_enums_v111.json', 'rb') as f:
	enums = json.load(f)
for filename, enum_list in enums.items():
	for key, enum in enum_list.items():
		key = int(key)
		enumkey = str(enum) # terrible hack
		if enumkey in enum_uses:
			if enum not in shared_enums:
				name = assign_name(key)
				shared_enums.append(enum)
				shared_enum_names.append(name)
				enum_remaps[enum_uses[enumkey]] = name
			enum_remaps[(filename, key)] = enum_remaps[enum_uses[enumkey]]
		else:
			enum_uses[enumkey] = (filename, key)

for name, enum in zip(shared_enum_names, shared_enums):
	print('%s = (' % name)
	print_enum('\t', enum)
	print(')')
	print()

for filename in sorted(files):
	if filename.endswith('.bcsv'):
		b = bcsv.File(bcsv.Row)
		print('class %s(Row):' % (filename[:-5]))
		with open('%s/%s' % (path, filename), 'rb') as f:
			b.load(f.read())
		for key, (offset, size) in b.fields.items():
			try:
				name = preset_names[key]
			except KeyError:
				name = '_%08x' % key
			if filename in enums and str(key) in enums[filename]:
				assert(size == 4)
				try:
					remap = enum_remaps[(filename, key)]
					print('\t%s = Enum(0x%08x, %s)' % (name, key, remap))
				except KeyError:
					print('\t%s = Enum(0x%08x, (' % (name, key))
					print_enum('\t\t', enums[filename][str(key)])
					print('\t))')
			else:
				# let's make some assumptions
				if key in type_overrides:
					print('\t%s = %s(0x%08x)' % (name, type_overrides[key], key))
				elif size == 1:
					print('\t%s = U8(0x%08x)' % (name, key))
				elif size == 2:
					print('\t%s = U16(0x%08x)' % (name, key))
				elif size == 4:
					print('\t%s = U32(0x%08x)' % (name, key))
				elif size > 8:
					print('\t%s = String(0x%08x)' % (name, key))
				else:
					print('\t%s = Field(0x%08x) # %d byte%s' % (name, key, size, '' if size == 1 else 's'))
		print()

print('lookup = {')
for filename in sorted(files):
	if filename.endswith('.bcsv'):
		print('\t%r: %s,' % (filename, filename[:-5]))
print('}')
