import bcsv
import msbt
import json
import sarc
import sys
import zstandard
from specs import *

messages_path = sys.argv[1]
bcsv_path = sys.argv[2]

def fixup(name):
	bits = []
	for bit in name.parse():
		if isinstance(bit, str):
			bits.append(bit)
	return ''.join(bits)

item_names = {}


# MESSAGES
data = open(messages_path + '/String_EUen.sarc.zs', 'rb').read()
data = zstandard.ZstdDecompressor().decompress(data)
msgArc = sarc.SARC(data)

outfitGroup = {}

for name in sorted(msgArc.list_files()):
	if 'STR_ItemName' in name:
		m = msbt.MSBT()
		m.load(msgArc.get_file_data(name))
		for label, msg in m.data.items():
			if not label.endswith('_pl'):
				item_id = int(label[label.rfind('_') + 1:], 10)
				item_names[item_id] = fixup(msg)
	if 'STR_OutfitGroupColor' in name:
		m = msbt.MSBT()
		m.load(msgArc.get_file_data(name))
		for label, msg in m.data.items():
			key = label[:label.rfind('_')]
			item_id = int(label[label.rfind('_') + 1:], 10)
			try:
				outfitGroup[key].append((item_id, fixup(msg)))
			except KeyError:
				outfitGroup[key] = [(item_id, fixup(msg))]
	if 'STR_OutfitGroupName' in name:
		m = msbt.MSBT()
		m.load(msgArc.get_file_data(name))
		key2 = name[name.rfind('_')+1:name.rfind('.')]
		for label, msg in m.data.items():
			key1 = label
			name = fixup(msg)
			for iid, col in outfitGroup[f'{key1}_{key2}']:
				item_names[iid] = f'{col} {name}'




output = {}

f = bcsv.File(ItemParam)
f.load(open(bcsv_path + '/ItemParam.bcsv', 'rb').read())
for row in f.rows:
	if row.UniqueID in item_names:
		output[row.UniqueID] = f'{row.Label} ({item_names[row.UniqueID]})'
	else:
		output[row.UniqueID] = row.Label

json.dump(output, open('item_hints.json', 'w'), indent=4, sort_keys=True)
