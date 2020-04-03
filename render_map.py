import bcsv
import json
import pbc
import sarc
import specs
import struct
import sys
import zstandard
from PIL import Image

romfs_path = sys.argv[1]
savefile_path = sys.argv[2]

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

savefile = open(savefile_path, 'rb').read()
chunks = struct.unpack_from('<72H', savefile, 0x2D12B4)
img = Image.new('RGBA', (7 * 32 * 2, 6 * 32 * 2))
pix = img.load()

json_stuff = {}

# place down our own map tiles
seen = [set() for i in range(7)]
for y in range(16 * 6):
	for x in range(16 * 7):
		offset = 0x2AC31C + ((x * 16 * 6) + y) * 14
		base_id,b,base_rot,d,e,f,level = struct.unpack_from('<HHHHHHH', savefile, offset)
		col = tile_pbcs['col%s.pbc' % tile_defs.by_id[base_id]._39b5a93d]
		blit_pbc(pix, x*4, y*4, col, base_rot, level)
		seen[0].add(base_id)
		seen[1].add(b)
		seen[2].add(base_rot)
		seen[3].add(d)
		seen[4].add(e)
		seen[5].add(f)
		seen[6].add(level)


for s in seen:
	print(sorted(s))

# draw the chunks
for chunk_y in range(6):
	for chunk_x in range(7):
		chunk_id = chunks[((chunk_y + 1) * 9) + (chunk_x + 1)]
		if chunk_id == 0:
			continue
		chunk_name = chunk_defs.by_id[chunk_id]._39b5a93d
		print('%d,%d :: Chunk %02d :: %s' % (chunk_x, chunk_y, chunk_id, chunk_name))
		col = load_single_pbc(chunk_name)
		blit_pbc(pix, chunk_x * 32 * 2, chunk_y * 32 * 2, col)

# throw in the items
seen = [set() for i in range(6)]
json_stuff['items'] = []
json_stuff['width'] = 32 * 7
json_stuff['height'] = 32 * 6
item_lookup = {}
for layer in range(2):
	for y in range(32 * 6):
		for x in range(32 * 7):
			offset = 0x20191C + 8 * ((layer * 32 * 6 * 32 * 7) + (x * 32 * 6) + y)
			typ,rot,a,b,c,d = struct.unpack_from('<HBBHBB', savefile, offset)
			if typ == 0xFFFD:
				item = item_lookup[(layer, x - c, y - d)]
				assert item['type'] == b
				item['extenders'].append((c,d))
			elif typ != 0xFFFE:
				item = dict(layer=layer,x=x,y=y,w=1,h=1,type=typ,rot=rot,a=a,b=b,c=c,d=d,extenders=[])
				item_lookup[(layer,x,y)] = item
				json_stuff['items'].append(item)
			seen[0].add(typ)
			seen[1].add(rot)
			seen[2].add(a)
			seen[3].add(b)
			seen[4].add(c)
			seen[5].add(d)

for s in seen:
	print(sorted(s))

# combine extended items into a single unit
for item in json_stuff['items']:
	if item['extenders']:
		width, height = 1, 1
		for x,y in item['extenders']:
			if (x + 1) > width:  width = x + 1
			if (y + 1) > height: height = y + 1
		assert len(item['extenders']) == (width * height) - 1
		item['w'] = width
		item['h'] = height
	del item['extenders']

# structures, too
# why the fuck not
'''
# there should be a count somewhere... but I'm not sure where
# so just wing it for now
for i in range(46):
	offset = 0x2D0F1C + 0x14 * i
	typ, x, y, rot, u1, u2, u3, u4, u5, u6 = struct.unpack_from('<HHHHHHHHHH', savefile, offset)
	# we wouldn't need this if we knew where the count was..
	if typ == 0 and x == 0 and y == 0:
		continue
	info = structure_info.by_id[typ]
	if info._c01e47a7[0] == 'Facility': # same info is in _d6704d8b...
		# we need to be able to tell the difference between the markets etc...
		# for now just wing it
		print('Facility:', x, y, typ, rot, u1, u2, u3, u4, u5, u6)
		for model in facility_models.rows:
			if model._00c1577d == typ and 'Reserve' not in model._39b5a93d:
				print('Using ' + model._39b5a93d)
				# dunno if rotation actually works in-game on these...
				blit_pbc(pix, x * 2 - 64, y * 2 - 64, load_single_pbc(model._39b5a93d), rot)
				break
	elif info._c01e47a7[0] == 'Bridge':
		print('Bridge:', x, y, rot, u1, u2, u3, u4, u5, u6)
		bparam = bridge_defs.by_id[u1]
		blit_pbc(pix, x * 2 - 64, y * 2 - 64, tile_pbcs[bparam._39b5a93d + '.pbc'], rot)
	elif info._c01e47a7[0] == 'Slope':
		in_progress = (rot & 0x200) != 0
		style = u2
		print('Slope:', x, y, rot & 3, u1, u2, u3, u4, u5, u6)
		sparam = slope_defs.by_id[u1]
		blit_pbc(pix, x * 2 - 64, y * 2 - 64, load_single_pbc(sparam._39b5a93d), rot)
	else:
		print('Other Structure:', x, y, typ, rot, u1, u2, u3, u4, u5, u6, info._c01e47a7)
'''


img.save('map.png')
json.dump(json_stuff, open('map.json', 'w'), indent=4)
