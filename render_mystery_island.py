import bcsv
import byml
import json
import pbc
import sarc
import specs
import struct
import sys
import zlib
import zstandard
from PIL import Image

def bykey(s):
	return '%x' % zlib.crc32(s.encode('ascii'))

descriptions = {
	0: '''A fairly normal island which you can get on your first tour, with one cliff, native fruit, coconuts, a river and a pond.''',
	1: '''Practically the same as Island #0, but without the pond, and with a slightly bigger cliff.''',
	2: '''"Spiral Island". Somewhat more interesting in layout but it has nothing special about the resources you can get.''',
	4: '''"Fidget Spinner Island". The last of the four starter islands. No river, just a pond and the sea.''',
	6: '''"Mountain Island". Multiple levels, no river. The base level has regular trees, the middle level has your native fruit, and the top level has five rocks with materials.''',
	7: '''"Bells Island" or "Money Rock Island". Breaking the rock at the far north will let you vault over into the island with five money rocks on it.''',
	8: '''"Bamboo Island". Every tree on this island is bamboo and you can get to it at any time of year. The most common island you can get out of the 20, statistically.''',
	10: '''"Fruit Island". There are 19 fruit trees on this island and all will be your 'sister fruit'. This will be different from your native fruit - but every time you come here, it will be the same one.''',
	11: '''"Flower Island". This island has a pond surrounded by rare flowers and the only insects that will spawn are those that hang around flowers.''',
	12: '''"Money Rock Island 2". There are four small triangular cliffs, one in each corner, and the ground level is full of flowers and money rocks.''',
	13: '''"Tarantula Island". Yes, the infamous one. The only insects that spawn here are tarantulas (as long as it is night time in a Tarantula month), and the rocks have crafting materials if you can get to them. The river is thin enough that you can jump over it without a vaulting pole.''',
	14: '''"Tree Island". This island has no river or pond and has tons of hardwood and coconut trees, and the only insects that spawn are those that are associated with trees.''',
	16: '''"Big Fish Island". This island has rare hybrid flowers and the only fish available are larger ones, including some of the more rare ones.''',
	17: '''"Tree Island 2". This island is exactly the same as Bamboo Island but the trees are all just regular hardwood trees.''',
	18: '''"Curly River Island". There is one square cliff at the north east, a few flowers and rocks and a small amount of fruit trees. Only insects associated with water spawn here.''',
	19: '''"Big Fish Island 2". This rare island only spawns big fish. Otherwise it is quite normal, with less flowers and a lower chance of appearing than the other big fish island.''',
	20: '''"Trash Island". Everything you can fish here is trash. Only water-related insects spawn.''',
	21: '''"Fins Island". A rectangular pond with rectangular cliffs inside, the tallest one being too tall to climb up to. The only fish that spawn here are the largest finned fish.''',
	23: '''"Falls Island". Lots of cliffs, waterfalls and river forks. Normal resource spawns.''',
	24: '''"Gold Island". A very rare island with flowers, scorpions and a rectangular pond. If you climb up onto the cliff and climb down from the back, you can vault over to a tiny island in the middle and get 8 gold nuggets from a single rock.''',
}

romfs_path = sys.argv[1]

tour_param = bcsv.File(specs.MysteryTourParam)
tour_param.load(open(romfs_path + '/Bcsv/MysteryTourParam.bcsv', 'rb').read())

tour_field_param = bcsv.File(specs.MysteryTourFieldParam)
tour_field_param.load(open(romfs_path + '/Bcsv/MysteryTourFieldParam.bcsv', 'rb').read())

tour_fish_param = bcsv.File(specs.MysteryTourFishParam)
tour_fish_param.load(open(romfs_path + '/Bcsv/MysteryTourFishParam.bcsv', 'rb').read())

tour_insect_param = bcsv.File(specs.MysteryTourInsectParam)
tour_insect_param.load(open(romfs_path + '/Bcsv/MysteryTourInsectParam.bcsv', 'rb').read())

tour_field_param = bcsv.File(specs.MysteryTourFieldParam)
tour_field_param.load(open(romfs_path + '/Bcsv/MysteryTourFieldParam.bcsv', 'rb').read())

fish_status_param = bcsv.File(specs.FishStatusParam)
fish_status_param.load(open(romfs_path + '/Bcsv/FishStatusParam.bcsv', 'rb').read())

insect_status_param = bcsv.File(specs.InsectStatusParam)
insect_status_param.load(open(romfs_path + '/Bcsv/InsectStatusParam.bcsv', 'rb').read())
insect_status_param.rows.sort(key=lambda k: k.id) # IMPORTANT! This took me hours of debugging

item_param = bcsv.File(specs.ItemParam)
item_param.load(open(romfs_path + '/Bcsv/ItemParam.bcsv', 'rb').read())

chunk_defs = bcsv.File(specs.FieldOutsideParts)
chunk_defs.load(open(romfs_path + '/Bcsv/FieldOutsideParts.bcsv', 'rb').read())

tile_defs = bcsv.File(specs.FieldLandMakingUnitModelParam)
tile_defs.load(open(romfs_path + '/Bcsv/FieldLandMakingUnitModelParam.bcsv', 'rb').read())

structure_info = bcsv.File(specs.StructureInfoParam)
structure_info.load(open(romfs_path + '/Bcsv/StructureInfoParam.bcsv', 'rb').read())

facility_models = bcsv.File(specs.StructureFacilityModel)
facility_models.load(open(romfs_path + '/Bcsv/StructureFacilityModel.bcsv', 'rb').read())

bridge_defs = bcsv.File(specs.StructureBridgeParam)
bridge_defs.load(open(romfs_path + '/Bcsv/StructureBridgeParam.bcsv', 'rb').read())

slope_defs = bcsv.File(specs.StructureSlopeParam)
slope_defs.load(open(romfs_path + '/Bcsv/StructureSlopeParam.bcsv', 'rb').read())

item_names = json.load(open('item_names.json', 'r'))

fish_categories = {}
for fish in fish_status_param.rows:
	if fish._3dc49bc2 > 0:
		size = fish._ac0ebe24[0]
		if size not in fish_categories: fish_categories[size] = []
		fish_categories[size].append(item_names[str(fish.insect_id)])


def load_single_pbc(name):
	arc = open(romfs_path + '/Model/' + name + '_pbc.Nin_NX_NVN.zs', 'rb').read()
	arc = zstandard.ZstdDecompressor().decompress(arc)
	arc = sarc.SARC(arc)
	return pbc.PBC(arc.get_file_data(name + '.pbc'))

tile_pbcs = {}
def import_pbc_arc(filename):
	arc = open(romfs_path + '/Model/' + filename, 'rb').read()
	arc = zstandard.ZstdDecompressor().decompress(arc)
	arc = sarc.SARC(arc)
	for name in arc.list_files():
		tile_pbcs[name] = pbc.PBC(arc.get_file_data(name))

for arc_name in ('', 'Cliff', 'Fall', 'River'):
	import_pbc_arc('FldUnit%s_pbc.Nin_NX_NVN.zs' % arc_name)
for arc_name in ('Brick', 'DarkSoil', 'FanPattern', 'MyDesign', 'Sand', 'Soil', 'Stone', 'Tile', 'Wood'):
	import_pbc_arc('FldUnitRoad%s_pbc.Nin_NX_NVN.zs' % arc_name)
for arc_name in ('Bricks', 'Iron', 'Japanese', 'Log', 'Red', 'Reserved', 'Stone', 'Suspension', 'Wood'):
	import_pbc_arc('Bridge%s_pbc.Nin_NX_NVN.zs' % arc_name)



mapping = {
	0:  ( 70, 120,  64, 255), # Grass
	1:  (128, 215, 195, 255), # River
	3:  (192, 192, 192, 255), # Stone
	4:  (240, 230, 170, 255), # Sand
	5:  (128, 215, 195, 255), # Sea
	6:  (255, 128, 128, 255), # Wood
	7:  (0  ,   0,   0,   0), # Null
	8:  (32 ,  32,  32, 255), # Building
	9:  (255,   0,   0, 255), # ??
	10: (48 ,  48,  48, 255), # Door
	12: (128, 215, 195, 255), # Water at mouths of river
	15: (128, 215, 195, 255), # Strip of water between river mouth and river
	22: (190,  98,  98, 255), # Wood (thin)
	28: (255,   0,   0, 255), # ?? this one isn't even in ColGroundAttributeParam...
	29: (232, 222, 162, 255), # Edge of beach, next to sea
	41: (118, 122, 132, 255), # Rocks at top of map
	42: (128, 133, 147, 255), # Taller regions, rocks at top of map
	44: ( 62, 112,  56, 255), # Edge connecting grass and beach
	45: (118, 122, 132, 255), # Some kind of rock
	46: (120, 207, 187, 255), # Edge of sea, next to beach
	47: (128, 128,   0, 255), # Sandstone
	49: (190,  98,  98, 255), # Pier
	51: (32 , 152,  32, 255), # "Grass-growing building"??
}

def blit_pbc(pix, base_x, base_y, pbc, rot=0, level=0):
	w = pbc.width * 2
	h = pbc.height * 2
	# base_x += pbc.offset_x * 2
	# base_y += pbc.offset_y * 2
	for y in range(h):
		for x in range(w):
			value = pbc.data[(y * w) + x]
			if value != 7:
				col = mapping[value]
				if level > 0:
					factor = (1, 1.2, 1.4, 1.6)[level]
					col = (int(factor * col[0]), int(factor * col[1]), int(factor * col[2]), col[3])
				try:
					if rot == 0:
						pix[base_x+x, base_y+y] = col
					elif rot == 1:
						pix[base_x+y, base_y+h-1-x] = col
					elif rot == 2:
						pix[base_x+w-1-x, base_y+h-1-y] = col
					elif rot == 3:
						pix[base_x+w-1-y, base_y+x] = col
				except IndexError:
					pass


rock_counts = {}
fruit_tree_counts = {}

for tour in tour_param.rows:
	field_byml = byml.Byml(open('../Param/Field/MysteryTourIslandPreset/Preset%d_Field.byml' % tour.field_param_id, 'rb').read()).parse()
	item_byml = byml.Byml(open('../Param/Field/MysteryTourIslandPreset/Preset%d_Item.byml' % tour.item_param_id, 'rb').read()).parse()
	field_data = field_byml[bykey('Preset%d_Field' % tour.field_param_id)]['652d644c']
	items = item_byml[bykey('Preset%d_Item' % tour.item_param_id)][bykey('mItemList[]')]

	img = Image.new('RGBA', (3 * 32 * 2, 3 * 32 * 2))
	pix = img.load()

	json_stuff = {}

	# place down our own map tiles
	seen = [set() for i in range(7)]
	for y in range(16 * 3):
		for x in range(16 * 3):
			offset = ((y * 16 * 3) + x) * 14
			base_id,b,base_rot,d,e,f,level = struct.unpack_from('<HHHHHHH', field_data, offset)
			col = tile_pbcs['col%s.pbc' % tile_defs.by_id[base_id]._39b5a93d]
			blit_pbc(pix, x*4, y*4, col, base_rot, level)
			seen[0].add(base_id)
			seen[1].add(b)
			seen[2].add(base_rot)
			seen[3].add(d)
			seen[4].add(e)
			seen[5].add(f)
			seen[6].add(level)


	# draw the chunks
	river_kind = tour_field_param.by_id[tour.field_param_id]._e8fa8b93[0]
	c00 = 'FldOutNWStone00'
	c01 = 'FldOutNStone00'
	c02 = 'FldOutNEStone00'
	c10 = 'FldOutWRiver00' if river_kind == 'WestRiver' else 'FldOutW00'
	c12 = 'FldOutERiver00' if river_kind == 'EastRiver' else 'FldOutE00'
	c20 = 'FldOutSW00'
	c21 = 'FldOutSBridge01'
	c22 = 'FldOutSE00'
	blit_pbc(pix, 0 * 32 * 2, 0 * 32 * 2, load_single_pbc(c00))
	blit_pbc(pix, 1 * 32 * 2, 0 * 32 * 2, load_single_pbc(c01))
	blit_pbc(pix, 2 * 32 * 2, 0 * 32 * 2, load_single_pbc(c02))
	blit_pbc(pix, 0 * 32 * 2, 1 * 32 * 2, load_single_pbc(c10))
	blit_pbc(pix, 2 * 32 * 2, 1 * 32 * 2, load_single_pbc(c12))
	blit_pbc(pix, 0 * 32 * 2, 2 * 32 * 2, load_single_pbc(c20))
	blit_pbc(pix, 1 * 32 * 2, 2 * 32 * 2, load_single_pbc(c21))
	blit_pbc(pix, 2 * 32 * 2, 2 * 32 * 2, load_single_pbc(c22))


	# throw in the items
	json_stuff['items'] = []
	json_stuff['width'] = 32 * 3
	json_stuff['height'] = 32 * 3
	rock_count = 0
	fruit_tree_count = 0
	for item in items:
		layer = item[bykey('mItemLayerID.u8')]
		x = item[bykey('mHalfUnitX.s32')]
		y = item[bykey('mHalfUnitZ.s32')]
		param = item[bykey('mItemSaveParam')][bykey('mItemNameParam.u64')]
		typ,rot,a,b,c,d = struct.unpack('<HBBHBB', struct.pack('<Q', param))
		if typ != 0xFFFE:
			item = dict(layer=layer,x=x,y=y,w=1,h=1,type=typ,rot=rot,a=a,b=b,c=c,d=d)
			if typ >= 60178 and typ <= 60182:
				rock_count += 1
			if typ in (60001,60002,60104,60105,60106):
				fruit_tree_count += 1
			if typ >= 60352 and typ <= 60371:
				fruit_tree_count += 1
			try:
				size = item_param.by_id[typ]._e06fb090[0]
				if size in ('1_0x1_0', '1_0x0_5'):            item['w'] = 2
				if size in ('1_5x1_5'):                       item['w'] = 3
				if size in ('2_0x1_0', '2_0x2_0', '2_0x0_5'): item['w'] = 4
				if size in ('3_0x1_0', '3_0x2_0', '3_0x3_0'): item['w'] = 6
				if size in ('1_0x1_0', '2_0x1_0', '3_0x1_0'): item['h'] = 2
				if size in ('1_5x1_5'):                       item['h'] = 3
				if size in ('2_0x2_0', '3_0x2_0'):            item['h'] = 4
				if size in ('3_0x3_0'):                       item['h'] = 6
			except KeyError:
				item['w'] = 2
				item['h'] = 2
			json_stuff['items'].append(item)

	rock_counts[tour.id] = rock_count
	fruit_tree_counts[tour.id] = fruit_tree_count

	json_stuff['crop_from_top'] = 14
	img = img.crop((0, 28, img.width, img.height))
	img.save('mysteryIslands/map%d.png' % tour.id)
	json.dump(json_stuff, open('mysteryIslands/map%d.json' % tour.id, 'w'), indent=4)


for tour in tour_param.rows:
	print('<div class=\'tour\'>')
	print('<a href=\'mapview.html#%d\' class=\'tourImg\'><img src=\'mysteryIslands/mapthumb%d.png\'></a>' % (tour.id, tour.id))
	print('<span class=\'tourName\'>Island #%d</span>' % tour.id)

	rock_count = rock_counts[tour.id]
	sp_behaviour = tour._dd59b554[0]
	if sp_behaviour == 'StoneMaterial':
		rock = 'Crafting Materials'
		rock_special = ' special'
	elif sp_behaviour == 'StoneCoin':
		rock = 'Bells'
		rock_special = ' special'
	elif sp_behaviour == 'StoneGold':
		rock = 'Gold Nuggets'
		rock_special = ' special'
	else:
		rock = 'Normal'
		rock_special = ''

	if sp_behaviour == 'Bamboo':
		tree = 'Bamboo'
		tree_special = ' special'
	elif fruit_tree_counts[tour.id] == 0:
		tree = 'Hardwood'
		tree_special = ''
	elif sp_behaviour == 'TreeSisterFruit':
		tree = 'Sister Fruit'
		tree_special = ' special'
	else:
		tree = 'Native Fruit'
		tree_special = ''

	if sp_behaviour == 'FlowerRare':
		flower = 'Rare'
		flower_special = ' special'
	else:
		flower = 'Normal'
		flower_special = ''

	if tour.insect_param_id != 0xFFFF:
		insect_param = tour_insect_param.by_id[tour.insect_param_id]
		flags = insect_param._d086a528
		insects = []
		for i in range(len(flags)):
			for j in range(8):
				if (flags[i] & (1 << j)) != 0:
					iid = i*8+j
					n = item_names[str(insect_status_param.rows[iid].insect_id)]
					insects.append(n)
		insect = ', '.join(insects)
		insect_special = ' special'
	else:
		insect = 'Normal'
		insect_special = ''

	if tour.fish_param_id != 0xFFFF:
		fish_param = tour_fish_param.by_id[tour.fish_param_id]
		flags = fish_param._c35f78ed
		fishes = []
		for i, size in enumerate(specs.FishStatusParam.__dict__['_ac0ebe24'].values_en.values()):
			if (flags & (1 << i)) != 0:
				fishes.append(size[0] + ' (<i>' + ', '.join(fish_categories[size[0]]) + '</i>)')
		if fishes:
			fish = ', '.join(fishes)
			fish_special = ' special'
		else:
			fish = 'Trash'
			fish_special = ' badSpecial'
	else:
		fish = 'Normal'
		fish_special = ''

	reqs = []
	if tour.land_req == 'BuiltTownOffice':
		reqs.append('Town Hall')
	if 4703 in (tour.item_req_1, tour.item_req_2):
		reqs.append('Vaulting Pole')
	if 2615 in (tour.item_req_1, tour.item_req_2):
		reqs.append('Ladder')

	if tour.id in descriptions:
		print('<span class=\'iDesc\'>' + descriptions[tour.id] + '</span>')
	if reqs:
		print('<span class=\'iReqs\'>🚩 <b>Requires:</b> %s</span>' % ', '.join(reqs))
	if tour.player_flag_set != '':
		print('<span class=\'iLimit\'>📅 Max 1 daily visit</span>')
	print('<div class=\'iShortInfo\'>')
	print('<span class=\'iChance\'>🎲 <b>Chance:</b> %d%%</span>' % tour.chance)
	print('<span class=\'iTree%s\'>🌴 <b>Trees:</b> %s</span>' % (tree_special, tree))
	print('<span class=\'iFlower%s\'>💐 <b>Flowers:</b> %s</span>' % (flower_special, flower))
	print('<span class=\'iRock%s\'>⛏ <b>Rocks:</b> %s (%d)</span>' % (rock_special, rock, rock_count))
	print('</div>')
	print('<span class=\'iInsect%s\'>🐛 <b>Insects:</b> %s</span>' % (insect_special, insect))
	print('<span class=\'iFish%s\'>🐠 <b>Fish:</b> %s</span>' % (fish_special, fish))
	print('</div>')

