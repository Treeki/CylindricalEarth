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
	if name.startswith('\x0e2'):
		name = name[6:]
	name = name.replace('\x0en\x1e\0', '<name>')
	return name

output = {}


# MESSAGES
data = open(messages_path + '/String_EUen.sarc.zs', 'rb').read()
data = zstandard.ZstdDecompressor().decompress(data)
msgArc = sarc.SARC(data)

output['items'] = {}
outfitGroup = {}

for name in sorted(msgArc.list_files()):
	if 'STR_ItemName' in name:
		m = msbt.MSBT()
		m.load(msgArc.get_file_data(name))
		for label, index in m.labels.items():
			if not label.endswith('_pl'):
				item_id = int(label[label.rfind('_') + 1:], 10)
				output['items'][item_id] = fixup(m.strings[index])
	if 'STR_OutfitGroupColor' in name:
		m = msbt.MSBT()
		m.load(msgArc.get_file_data(name))
		for label, index in m.labels.items():
			key = label[:label.rfind('_')]
			item_id = int(label[label.rfind('_') + 1:], 10)
			try:
				outfitGroup[key].append((item_id, fixup(m.strings[index])))
			except KeyError:
				outfitGroup[key] = [(item_id, fixup(m.strings[index]))]
	if 'STR_OutfitGroupName' in name:
		m = msbt.MSBT()
		m.load(msgArc.get_file_data(name))
		key2 = name[name.rfind('_')+1:name.rfind('.')]
		for label, index in m.labels.items():
			key1 = label
			name = fixup(m.strings[index])
			for iid, col in outfitGroup[f'{key1}_{key2}']:
				output['items'][iid] = f'{col} {name}'



m = msbt.MSBT()
m.load(msgArc.get_file_data('Npc/STR_NNpcName.msbt'))
species = 'ant,bea,brd,bul,cat,cbr,chn,cow,crd,der,dog,duk,elp,flg,goa,gor,ham,hip,hrs,kal,kgr,lon,mnk,mus,ocp,ost,pbr,pgn,pig,rbt,rhn,shp,squ,tig,wol'.split(',')
output['villagerNames'] = [{} for z in species]

for label, index in m.labels.items():
	a = species.index(label[:3])
	b = int(label[3:])
	output['villagerNames'][a][b] = fixup(m.strings[index])

# dual stuff for these
justnames = (
	('STR_HouseWallName.msbt', 'houseWallNames', 'StructureHouseWallParam', StructureHouseWallParam),
	('STR_HouseDoorName.msbt', 'houseDoorNames', 'StructureHouseDoorParam', StructureHouseDoorParam),
	('STR_HouseRoofName.msbt', 'houseRoofNames', 'StructureHouseRoofParam', StructureHouseRoofParam),
)
for msbt_name, json_key, fname, rowclass in justnames:
	output[json_key] = {}

	f = bcsv.File(rowclass)
	f.load(open(bcsv_path + '/' + fname + '.bcsv', 'rb').read())
	for row in f.rows:
		output[json_key][row.id] = row._39b5a93d

	m = msbt.MSBT()
	m.load(msgArc.get_file_data(msbt_name))
	for label, index in m.labels.items():
		output[json_key][int(label)] = fixup(m.strings[index])



output['fg'] = {}
f = bcsv.File(FgMainParam)
f.load(open(bcsv_path + '/FgMainParam.bcsv', 'rb').read())
for row in f.rows:
	output['fg'][row.id] = {'name': row.name, 'item': row._f4678f13}


output['outsideParts'] = {}
f = bcsv.File(FieldOutsideParts)
f.load(open(bcsv_path + '/FieldOutsideParts.bcsv', 'rb').read())
for row in f.rows:
	output['outsideParts'][row.id] = row._39b5a93d


output['terrainUnits'] = {}
f = bcsv.File(FieldLandMakingUnitModelParam)
f.load(open(bcsv_path + '/FieldLandMakingUnitModelParam.bcsv', 'rb').read())
for row in f.rows:
	output['terrainUnits'][row.id] = row._39b5a93d


evflags = (
	('EventFlagsAocParam', EventFlagsAocParam, 'aoc', None),
	('EventFlagsBcatParam', EventFlagsBcatParam, 'bcat', None),
	('EventFlagsHouseParam', EventFlagsHouseParam, 'house', '_344b17d7'),
	('EventFlagsLandParam', EventFlagsLandParam, 'land', '_344b17d7'),
	('EventFlagsLandTempParam', EventFlagsLandTempParam, 'landTemp', '_0110b14c'),
	('EventFlagsNpcMemoryParam', EventFlagsNpcMemoryParam, 'npcMemory', '_bd7682f5'),
	('EventFlagsNpcSaveParam', EventFlagsNpcSaveParam, 'npcSave', '_344b17d7'),
	('EventFlagsNpcTempParam', EventFlagsNpcTempParam, 'npcTemp', '_0110b14c'),
	('EventFlagsPlayerActivityParam', EventFlagsPlayerActivityParam, 'playerActivity', None),
	('EventFlagsPlayerParam', EventFlagsPlayerParam, 'player', '_344b17d7'),
	('EventFlagsPlayerTempParam', EventFlagsPlayerTempParam, 'playerTemp', '_0110b14c'),
	('EventFlagsPlayerVisitParam', EventFlagsPlayerVisitParam, 'playerVisit', '_0110b14c'),
	('EventFlagsLifeSupportAchievementParam', EventFlagsLifeSupportAchievementParam, 'miles', '_1be772f0'),
	('EventFlagsLifeSupportDailyParam', EventFlagsLifeSupportDailyParam, 'milesPlus', None),
)

output['eventFlags'] = {}
for (fname, rowclass, key, maxkey) in evflags:
	f = bcsv.File(rowclass)
	f.load(open(bcsv_path + '/' + fname + '.bcsv', 'rb').read())
	output['eventFlags'][key] = []
	for row in f.rows:
		output['eventFlags'][key].append({
			'id': row.id,
			'enName': row.name_en,
			'jpName': row.name_jp,
		})
		if maxkey:
			output['eventFlags'][key][-1]['maximum'] = getattr(row, maxkey)


json.dump(output, open('gameData.json', 'w'), indent=4, sort_keys=True)
