# expects String_EUen.sarc.zs

import json
import msbt
import sarc
import sys
import zstandard

def fixup(name):
	if name.startswith('\x0e2'):
		name = name[6:]
	name = name.replace('\x0en\x1e\0', '<name>')
	return name

data = open(sys.argv[1], 'rb').read()
data = zstandard.ZstdDecompressor().decompress(data)
data = sarc.SARC(data)

all_names = {}

for name in data.list_files():
	if 'STR_ItemName' in name:
		m = msbt.MSBT()
		m.load(data.get_file_data(name))

		for label, index in m.labels.items():
			if not label.endswith('_pl'):
				item_id = int(label[label.rfind('_') + 1:], 10)
				all_names[item_id] = fixup(m.strings[index])

with open('item_names.json', 'w') as f:
	json.dump(all_names, f, sort_keys=True, indent=4)

