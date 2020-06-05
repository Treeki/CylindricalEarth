import struct
import array

BIG_ENDIAN, LITTLE_ENDIAN = range(2)

def _create(s):
	return (struct.Struct('>'+s), struct.Struct('<'+s))

u64 = _create('Q')
u32 = _create('I')
u16 = _create('H')
u8 = _create('B')

s64 = _create('q')
s32 = _create('i')
s16 = _create('h')
s8 = _create('b')

f32 = _create('f')
f64 = _create('d')

del _create



class DataInputStream:
	def __init__(self, data, endian=BIG_ENDIAN, coverage=None):
		self.data = data
		self.length = len(data)
		self.pos = 0
		self.endian = endian
		if coverage is None:
			self.coverage = array.array('b')
			self.coverage.extend((0,) * self.length)
		else:
			self.coverage = coverage

	def seek(self, pos):
		assert pos >= 0 and pos <= self.length
		self.pos = pos

	def skip(self, count):
		new_pos = self.pos + count
		assert new_pos >= 0 and new_pos <= self.length
		self.pos = new_pos

	def at_end(self):
		return self.pos >= self.length

	def read_bytes(self, count):
		new_pos = self.pos + count
		assert new_pos >= 0 and new_pos <= self.length
		for i in range(self.pos, new_pos):
			self.coverage[i] = 1
		data = self.data[self.pos:new_pos]
		self.pos = new_pos
		return data

	def read_u8(self):
		return u8[self.endian].unpack(self.read_bytes(1))[0]

	def read_u16(self):
		return u16[self.endian].unpack(self.read_bytes(2))[0]

	def read_u32(self):
		return u32[self.endian].unpack(self.read_bytes(4))[0]

	def read_u64(self):
		return u64[self.endian].unpack(self.read_bytes(8))[0]

	def read_s8(self):
		return s8[self.endian].unpack(self.read_bytes(1))[0]

	def read_s16(self):
		return s16[self.endian].unpack(self.read_bytes(2))[0]

	def read_s32(self):
		return s32[self.endian].unpack(self.read_bytes(4))[0]

	def read_s64(self):
		return s64[self.endian].unpack(self.read_bytes(8))[0]

	def read_float(self):
		return f32[self.endian].unpack(self.read_bytes(4))[0]

	def read_double(self):
		return f64[self.endian].unpack(self.read_bytes(8))[0]


	def at(self, pos):
		copy = DataInputStream(self.data, self.endian, self.coverage)
		copy.seek(pos)
		return copy

	def copy(self):
		return self.at(self.pos)

	@property
	def covered_bytes(self):
		n = 0
		for flag in self.coverage:
			if flag == 1:
				n += 1
		return n


class DataOutputStream:
	def __init__(self, outfile, endian=BIG_ENDIAN):
		self.outfile = outfile
		self.endian = endian

	def write_bytes(self, data):
		self.outfile.write(data)

	def write_u8(self, value):
		self.write_bytes(u8[self.endian].pack(value))

	def write_u16(self, value):
		self.write_bytes(u16[self.endian].pack(value))

	def write_u32(self, value):
		self.write_bytes(u32[self.endian].pack(value))

	def write_u64(self, value):
		self.write_bytes(u64[self.endian].pack(value))

	def write_s8(self, value):
		self.write_bytes(s8[self.endian].pack(value))

	def write_s16(self, value):
		self.write_bytes(s16[self.endian].pack(value))

	def write_s32(self, value):
		self.write_bytes(s32[self.endian].pack(value))

	def write_s64(self, value):
		self.write_bytes(s64[self.endian].pack(value))

	def write_float(self, value):
		self.write_bytes(f32[self.endian].pack(value))

	def write_double(self, value):
		self.write_bytes(f64[self.endian].pack(value))



def read_bytestring(s):
	output = []
	while True:
		bit = s.read_u8()
		if bit == 0:
			return bytes(output)
		else:
			output.append(bit)

def read_u16string(s):
	output = []
	while True:
		bit = s.read_u16()
		if bit == 0:
			return ''.join(output)
		else:
			output.append(chr(bit))


