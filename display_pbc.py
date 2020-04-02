import os
import sarc
import struct
import zstandard
from PIL import Image

def load_pbc(name):
	blob = open('pbc/' + name + '_pbc.Nin_NX_NVN.zs', 'rb').read()
	blob = zstandard.ZstdDecompressor().decompress(blob)
	# blob = sarc.SARC(blob).get_file_data(name + '.pbc')
	arc = sarc.SARC(blob)
	# open('pbc_ex/%s.pbc' % name, 'wb').write(blob)

	# blob = open('pbc_ex/%s.pbc' % name, 'rb').read()
	for name in arc.list_files():
		blob = arc.get_file_data(name)
		assert(blob[0:4] == b'pbc\0')
		w,h,offset_x,offset_y = struct.unpack_from('<iiii', blob, 4)
		print('%40s | %5d %5d %5d %5d' % (name, w, h, offset_x, offset_y))

		sets = [set() for i in range(12)]
		img = Image.new('RGBA', (w*2, h*2))
		pix = img.load()
		offset = 0x14
		for y in range(h):
			for x in range(w):
				for i in range(12):
					f = struct.unpack_from('<f', blob, offset + i * 4)[0]
					sets[i].add(f)
				a = blob[offset + 0x30]
				b = blob[offset + 0x31]
				c = blob[offset + 0x32]
				d = blob[offset + 0x33]
				pix[x*2,y*2] = (a,a,a,255)
				pix[x*2,y*2+1] = (b,b,b,255)
				pix[x*2+1,y*2+1] = (c,c,c,255)
				pix[x*2+1,y*2] = (d,d,d,255)
				offset += 0x34
		# img.save('imgs/%s.png' % name)
		# for s in sets:
		# 	# print(s)
		# 	print(min(s), max(s))


import sys
if len(sys.argv) > 1:
	load_pbc(sys.argv[1])
else:
	for name in sorted(os.listdir('pbc')):
		trimmed_name = name.replace('_pbc.Nin_NX_NVN.zs', '')
		load_pbc(trimmed_name)

#for name in os.listdir('pbc'):
#	trimmed_name = name.replace('_pbc.Nin_NX_NVN.zs', '')
#	if 'Unit' in trimmed_name: continue
#	if 'RoomTexFloor' in trimmed_name: continue
#	if 'RoomSpFloor' in trimmed_name: continue
#	if 'Bridge' in trimmed_name: continue
#	if 'IdrMuseum' in trimmed_name: continue
#	blob = open('pbc/' + name, 'rb').read()
#	blob = zstandard.ZstdDecompressor().decompress(blob)
#	# print(sarc.SARC(blob).list_files())
#	blob = sarc.SARC(blob).get_file_data(trimmed_name + '.pbc')
#
#	assert(blob[0:4] == b'pbc\0')
#	a,b,c,d = struct.unpack_from('<iiii', blob, 4)
#	print('%4d | %30s | %5d %5d %5d %5d | %5d %04x | %.f' % (a*b, trimmed_name, a, b, c, d, len(blob), len(blob), (len(blob)-20)/a/b))
#
#	with open('pbc_ex/%s.pbc' % trimmed_name, 'wb') as f:
#		f.write(blob)



