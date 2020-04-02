import struct

class PBC:
	def __init__(self, blob):
		assert(blob[0:4] == b'pbc\0')
		w, h, self.offset_x, self.offset_y = struct.unpack_from('<iiii', blob, 4)
		self.width = w
		self.height = h
		self.data = bytearray(w * h * 4)

		# ignore the heightmap for now
		offset = 0x14
		for y in range(h):
			for x in range(w):
				a, b, c, d = blob[offset+0x30:offset+0x34]
				self.data[(x*2)   + ((y*2)  *(w*2))] = a
				self.data[(x*2)   + ((y*2+1)*(w*2))] = b
				self.data[(x*2+1) + ((y*2+1)*(w*2))] = c
				self.data[(x*2+1) + ((y*2)  *(w*2))] = d
				offset += 0x34

