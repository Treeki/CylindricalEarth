import codecs
import struct

# lazy implementation, but it's something ¯\_(ツ)_/¯

class MSBT:
	def __init__(self):
		self.labels = {}
		self.attributes = []
		self.strings = []

	def load(self, blob):
		assert blob[:8] == b'MsgStdBn'
		endian, version, section_count, file_size = struct.unpack_from('<HxxHII', blob, 8)
		assert version == 0x0301
		offset = 0x20

		for i in range(section_count):
			section_magic, section_size = struct.unpack_from('<4sI', blob, offset)
			offset += 0x10
			section = blob[offset:offset+section_size]
			offset += (section_size + 0xF) & ~0xF

			if section_magic == b'LBL1':
				self.labels = self._load_lbl1(section)
			elif section_magic == b'ATR1':
				self.attributes = self._load_atr1(section)
			elif section_magic == b'TXT2':
				self.strings = self._load_txt2(section)
			else:
				raise 'unknown section %r' % section_magic

	def _load_lbl1(self, data):
		offset_count = struct.unpack_from('<I', data, 0)[0]
		results = {}
		for i in range(offset_count):
			string_count, offset = struct.unpack_from('<II', data, 4 + i * 8)
			for j in range(string_count):
				string_len = data[offset]
				offset += 1
				string = codecs.decode(data[offset:offset+string_len], 'ascii')
				offset += string_len
				index = struct.unpack_from('<I', data, offset)[0]
				offset += 4
				results[string] = index
		return results

	def _load_atr1(self, data):
		count, size = struct.unpack_from('<II', data, 0)
		return [data[8+i*size:8+i*size+size] for i in range(count)]

	def _load_txt2(self, data):
		count = struct.unpack_from('<I', data, 0)[0]
		offsets = list(struct.unpack_from('<%dI' % count, data, 4))
		offsets.append(len(data)) # dummy end offset
		return [codecs.decode(data[offsets[i]:offsets[i+1]-2], 'utf-16le') for i in range(count)]


if __name__ == '__main__':
	import sys, sarc, zstandard
	arc = sarc.SARC(zstandard.ZstdDecompressor().decompress(open(sys.argv[1], 'rb').read()))
	if len(sys.argv) == 2:
		for f in sorted(arc.list_files()):
			print(f)
	else:
		msbt = MSBT()
		msbt.load(arc.get_file_data(sys.argv[2]))
		for label, index in sorted(msbt.labels.items()):
			print('%s: %r' % (label, msbt.strings[index]))
