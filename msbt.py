import codecs
import struct
from collections import namedtuple
import xml.etree.ElementTree as ET

# lazy implementation, but it's something ¯\_(ツ)_/¯

def hash_label(label, bucket_count):
	val = 0
	for c in label:
		val = ((val * 0x492) + ord(c)) & 0xFFFFFFFF
	return val % bucket_count

def hash_bucket_count(string_count):
	primes = (
		2,3,5,7,11,13,17,19,23,29,31,37,41,43,
		47,53,59,61,67,71,73,79,83,89,97,101
		)
	target = (string_count // 2) + 1
	for prime in primes:
		if prime >= target:
			return prime
	return primes[-1]

def round_up(amount):
	return (amount + 0xF) & ~0xF

StartTag = namedtuple('StartTag', ('a', 'b', 'arg'))
EndTag = namedtuple('EndTag', ('a', 'b'))

# 110, 0 - ellipsis?
# 110, 3 - nickname?
# 110, 5 - phrase?

animEnums = (
	"EmotEnd", "Smiling", "Laughing", "HappyFlower", "Love", "HappyDance", "Angry", "Outraged",
	"Fuming", "Worried", "Sighing", "Thinking", "SadSpiral", "Frantic", "Crying", "Shocked",
	"Aha", "TakenAback", "Surprised", "ColdChill", "Shaking", "Nodding", "IdeaBulb", "QuestionMark",
	"BrokenHeart", "Sleepy", "Blushing", "OhGeez", "Scheming", "Clapping", "Sneezing", "Cheering",
	"Greeting", "SmugFace", "Hot", "Grin", "WrySmile", "FaintSmile", "BigSmile", "Hesitate",
	"Negative", "Oops", "Dance", "AbsentMindedness", "Shaki", "Sleep", "Special", "Silent",
	"Hello", "Confused", "ShyBoy", "Restless", "Serious", "Eh", "Apologize", "Assent",
	"Explain", "NpcShuffle", "Pardon", "NpcHoldout")

# 2e missing ('special')
animMappings = (
	0,0,1,3,4,0x24,0x25,0x26,
	6,7,8,9,0xa,0xb,0xc,0xd,
	0xe,0x18,0x1b,0x31,2,5,0x1d,0x2a,
	0,0x2c,0xf,0x10,0x11,0x12,0x16,0x29,
	0x35,0x1f,0x20,0x36,0x30,0x15,0x17,0x28,
	0x37,0x38,0x13,0x14,0x1e,0x22,0x19,0x2d,
	0,0x2b,0x1a,0x1c,0x27,0x21,0x23,0x32,
	0x33,0x34,0x2f,0x3a,0x39,0x3b)

animIDs = '|'.join([animEnums[x] for x in animMappings])

tagMetadata = {
	(0,0): ('ruby', 'u16 a', 'u16 b', 'str'),
	(0,2): ('size', 'u16 value'),
	(0,3): ('colour', 'u16 id'),
	(0,4): ('pageBreak', ),
	(10,0): ('delay', 'u16 frames'),
	(10,1): ('delay8', ),
	(10,2): ('delay20', ),
	(10,3): ('delay40', ),
	(10,4): ('10_4', ),
	(10,5): ('10_5', ),
	(10,7): ('10_7', 'u32 arg'),
	(10,8): ('10_8', 'u32 arg'),
	(10,9): ('10_9', ),
	(10,10): ('10_10', ),
	(10,11): ('10_11', ),
	(10,14): ('10_14', 'u16 arg'),
	(10,15): ('setNpcTalkChoices', 'u8 chatOption', 'u8 cancelOption'),
	(20,0): ('20_0', 'str arg'),
	(20,1): ('20_1', 'str arg'),
	(20,2): ('20_2', 'u8 arg'),
	(20,3): ('20_3', 'u8 arg'),
	(40,-1): ('anim', 'idB id '+animIDs, 'u8 target actor|player|mainNpc|subNpc', 'align', 'str targetSpec'),
	(45,-1): ('snpcAnim', 'idB id GulCollapsed|GstSurprised|DodWireless|DodRoger|TkkEh|TkkNodding|TkkQuestionMark', 'u8 target actor|player|mainNpc|subNpc', 'align', 'str targetSpec'),
	(50,4): ('capitaliseNextWord', ),
	(50,5): ('gender1', 'str m', 'str f'),
	(50,6): ('gender2', 'str m', 'str f'),
	(50,7): ('gender3', 'str m', 'str f'),
	(50,8): ('50_8', 'u8 x', 'u8 y', 'str a', 'str b', 'str c'),
	(50,9): ('50_9', 'u8 x', 'u8 y', 'str a', 'str b', 'str c'),
	(50,10): ('gender4', 'str m', 'str f'),
	(50,14): ('gender5', 'str m', 'str f'),
	(50,20): ('gender6', 'str m', 'str f'),
	(50,22): ('gender7', 'str m', 'str f'),
	(50,25): ('weatherArea', 'str north', 'str south'),
	(50,27): ('50_27', 'u8 x', 'u8 y', 'str a', 'str b', 'str c'),
	(100,3): ('100_3', 'u8 arg Katsu|PlaneAnnounceOn|PlaneAnnounceOff'),
	(198,0): ('delayByPersonality', 'u16 boy_normal', 'u16 boy_active', 'u16 boy_pride', 'u16 boy_snobby', 'u16 girl_normal', 'u16 girl_active', 'u16 girl_pride', 'u16 girl_big_sis'),
	(199,3): ('199_3', 'u16 a'),
}

def tag_to_xml(tag):
	key = (tag.a, tag.b)
	keyN = (tag.a, -1)
	if key in tagMetadata or keyN in tagMetadata:
		meta = tagMetadata.get(key, tagMetadata.get(keyN))
		elem = ET.Element(meta[0])
		offset = 0
		for argdef in meta[1:]:
			if argdef == 'str':
				elem.text = ''.join(map(chr, tag.arg[offset//2:]))
				break
			if argdef == 'align':
				if (offset & 1) == 1:
					offset += 1
				continue
			bits = argdef.split(' ')
			typ = bits[0]
			name = bits[1]
			if typ == 'str':
				arglen = tag.arg[offset // 2]
				offset += 2
				arg = ''.join(map(chr, tag.arg[offset//2:(offset+arglen)//2]))
				offset += arglen
			elif typ == 'u32':
				arg = str(tag.arg[offset//2] | (tag.arg[(offset//2) + 1] << 16))
				offset += 4
			elif typ == 'u16':
				arg = str(tag.arg[offset//2])
				offset += 2
			elif typ == 'u8':
				if (offset & 1) == 0:
					arg = str(tag.arg[offset // 2] & 0xFF)
				else:
					arg = str(tag.arg[offset // 2] >> 8)
				offset += 1
			elif typ == 'idB':
				arg = str(tag.b)
			if len(bits) > 2:
				enum = bits[2].split('|')
				num = int(arg)
				if num < len(enum):
					arg = enum[num]
			elem.set(name, arg)
		return elem

	# nope
	elem = ET.Element('tag', dict(a=str(tag.a), b=str(tag.b)))
	if tag.arg:
		arg = ' '.join(map(hex, tag.arg))
		elem.set('arg', arg)
	return elem

class Message(namedtuple('Message', ('text', 'attribute'))):
	__slots__ = ()

	@classmethod
	def from_pieces(cls, pieces, attribute):
		chars = []
		for piece in pieces:
			if isinstance(piece, StartTag):
				chars.append(0xE)
				chars.append(piece.a)
				chars.append(piece.b)
				chars.append(len(piece.arg) * 2)
				chars.extend(piece.arg)
			elif isinstance(piece, EndTag):
				chars.append(0xF)
				chars.append(piece.a)
				chars.append(piece.b)
			else:
				chars.extend(map(ord, piece))
		text = struct.pack('<%dH' % len(chars), *chars)
		return cls(text, attribute)

	def parse(self):
		chars = struct.unpack_from('<%dH' % (len(self.text) // 2), self.text)
		last = 0
		pos = 0
		while pos < len(chars):
			c = chars[pos]
			if (c == 0xE) or (c == 0xF):
				if pos > last:
					yield ''.join(map(chr, chars[last:pos]))
				# tag
				a = chars[pos + 1]
				b = chars[pos + 2]
				pos += 3
				if c == 0xE:
					arg_len = chars[pos]
					pos += 1
					assert (arg_len & 1) == 0
					arg = chars[pos:pos+(arg_len>>1)]
					pos += (arg_len >> 1)
					yield StartTag(a, b, arg)
				else:
					yield EndTag(a, b)
				last = pos
			else:
				pos += 1
		if pos > last:
			yield ''.join(map(chr, chars[last:pos]))

	def generate_xml(self, label=None):
		elem = ET.Element('message')
		if label is not None:
			elem.set('label', label)
		if self.attribute:
			elem.set('attrib', self.attribute.hex(' '))
		#elem.set('raw', self.text.hex(' ', -2))
		for bit in self.parse():
			if isinstance(bit, str):
				if len(elem) == 0:
					elem.text = bit
				else:
					elem[-1].tail = bit
			elif isinstance(bit, StartTag):
				elem.append(tag_to_xml(bit))
			elif isinstance(bit, EndTag):
				ET.SubElement(elem, 'endTag', dict(a=str(bit.a), b=str(bit.b)))
		return elem

class MSBT:
	def __init__(self):
		self.data = {}
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
				labels = self._load_lbl1(section)
			elif section_magic == b'ATR1':
				attributes = self._load_atr1(section)
			elif section_magic == b'TXT2':
				strings = self._load_txt2(section)
			else:
				raise 'unknown section %r' % section_magic

		assert(len(labels) == len(strings))
		assert(len(attributes) == len(strings))
		label_list = [None] * len(labels)
		for label, index in labels.items():
			label_list[index] = label

		self.data = {}
		for label, string, attribute in zip(label_list, strings, attributes):
			self.data[label] = Message(string, attribute)

	def _load_lbl1(self, data):
		bucket_count = struct.unpack_from('<I', data, 0)[0]
		results = {}
		for i in range(bucket_count):
			string_count, offset = struct.unpack_from('<II', data, 4 + i * 8)
			for j in range(string_count):
				label_len = data[offset]
				offset += 1
				label = codecs.decode(data[offset:offset+label_len], 'ascii')
				offset += label_len
				index = struct.unpack_from('<I', data, offset)[0]
				offset += 4
				results[label] = index
				assert(hash_label(label, bucket_count) == i)
		return results

	def _load_atr1(self, data):
		count, size = struct.unpack_from('<II', data, 0)
		self.attrib_size = size
		return [data[8+i*size:8+i*size+size] for i in range(count)]

	def _load_txt2(self, data):
		count = struct.unpack_from('<I', data, 0)[0]
		offsets = list(struct.unpack_from('<%dI' % count, data, 4))
		offsets.append(len(data)) # dummy end offset
		return [bytes(data[offsets[i]:offsets[i+1]-2]) for i in range(count)]
		#return [codecs.decode(data[offsets[i]:offsets[i+1]-2], 'utf-16le') for i in range(count)]


	def _get_lbl1_size(self):
		return 4 + (8 * hash_bucket_count(len(self.data))) + (5 * len(self.data)) + sum(map(len, self.data.keys()))
	def _get_atr1_size(self):
		return 8 + (len(self.data) * self.attrib_size)
	def _get_txt2_size(self):
		return 4 + sum([len(msg.text) + 4 + 2 for msg in self.data.values()])
	def _get_file_size(self, block_sizes):
		return 0x20 + sum([0x10 + round_up(size) for size in block_sizes])

	def _pack_section_header(self, buf, offset, magic, size):
		buf[offset:offset+4] = magic
		struct.pack_into('<I', buf, offset + 4, size)
		return offset + 0x10

	def _pack_lbl1(self, buf, base):
		bucket_count = hash_bucket_count(len(self.data))
		buckets = [[] for i in range(bucket_count)]
		for index, label in enumerate(self.data.keys()):
			buckets[hash_label(label, bucket_count)].append((label, index))

		struct.pack_into('<I', buf, base, bucket_count)
		table_offset = 4
		data_offset = 4 + (8 * bucket_count)
		for bucket in buckets:
			struct.pack_into('<II', buf, base + table_offset, len(bucket), data_offset)
			table_offset += 8
			for label, index in bucket:
				buf[base+data_offset] = len(label)
				data_offset += 1
				buf[base+data_offset:base+data_offset+len(label)] = label.encode('ascii')
				data_offset += len(label)
				struct.pack_into('<I', buf, base+data_offset, index)
				data_offset += 4

		return base + data_offset

	def _pack_atr1(self, buf, offset):
		struct.pack_into('<II', buf, offset, len(self.data), self.attrib_size)
		offset += 8
		for msg in self.data.values():
			attrib = msg.attribute
			assert(len(attrib) == self.attrib_size)
			buf[offset:offset+len(attrib)] = attrib
			offset += len(attrib)
		return offset

	def _pack_txt2(self, buf, base):
		struct.pack_into('<I', buf, base, len(self.data))
		table_offset = 4
		data_offset = 4 + (4 * len(self.data))
		for message in self.data.values():
			struct.pack_into('<I', buf, base + table_offset, data_offset)
			table_offset += 4
			string = message.text
			buf[base+data_offset:base+data_offset+len(string)] = string
			data_offset += len(string) + 2
		return base + data_offset

	def pack(self):
		lbl1_size = self._get_lbl1_size()
		atr1_size = self._get_atr1_size()
		txt2_size = self._get_txt2_size()
		file_size = self._get_file_size([lbl1_size, atr1_size, txt2_size])

		buf = bytearray(file_size)
		buf[:8] = b'MsgStdBn'
		struct.pack_into('<HHHII', buf, 8, 0xFEFF, 0, 0x301, 3, file_size)

		offset = 0x20
		offset = self._pack_section_header(buf, offset, b'LBL1', lbl1_size)
		offset = self._pack_lbl1(buf, offset)
		offset = self._round_up_buffer(buf, offset)
		offset = self._pack_section_header(buf, offset, b'ATR1', atr1_size)
		offset = self._pack_atr1(buf, offset)
		offset = self._round_up_buffer(buf, offset)
		offset = self._pack_section_header(buf, offset, b'TXT2', txt2_size)
		offset = self._pack_txt2(buf, offset)
		offset = self._round_up_buffer(buf, offset)
		assert(offset == len(buf))

		return buf

	def _round_up_buffer(self, buf, offset):
		rounded = round_up(offset)
		for i in range(offset, rounded):
			buf[i] = 0xAB
		return rounded


	def generate_xml(self):
		root = ET.Element('msbt', dict(attribsize=str(self.attrib_size)))
		root.text = '\n\t'
		tag = None
		for label, message in self.data.items():
			tag = message.generate_xml(label)
			tag.tail = '\n\t'
			root.append(tag)
		if tag is not None:
			tag.tail = '\n' # no tab on last one
		return root




if __name__ == '__main__':
	import sys, sarc, zstandard

	path = sys.argv[1]
	data = open(path, 'rb').read()
	if path.endswith('.zs'):
		path = path[:-3]
		data = zstandard.ZstdDecompressor().decompress(data)
	if path.endswith('.sarc'):
		arc = sarc.SARC(data)
		if len(sys.argv) == 2:
			for f in sorted(arc.list_files()):
				print(f)
			sys.exit()
		else:
			data = arc.get_file_data(sys.argv[2])

	msbt = MSBT()
	msbt.load(data)
	assert(data == msbt.pack())
	xml = msbt.generate_xml()
	print(ET.tostring(xml, 'unicode'))
	#for label, index in sorted(msbt.labels.items()):
	#	print('%s: %r <%r>' % (label, msbt.strings[index], msbt.attributes[index]))
	#repack = msbt.pack()
	#open('tst.msbt', 'wb').write(repack)
