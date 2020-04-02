import struct
import zlib

class File:
	def __init__(self, row_class):
		self.fields = {}
		self.rows = []
		self.row_class = row_class
		self.by_id = {}

	def load(self, blob):
		# read file header
		entry_count, entry_size, field_count, version, jp_enum_flag = struct.unpack_from('<IIHBB', blob, 0)
		assert(0 <= version <= 1)
		if version == 0:
			pos = 0xC
		elif version == 1:
			assert(blob[0xC:0x10] == b'VSCB')
			pos = 0x1C

		self.jp_enums = (jp_enum_flag == 0)

		# read field specs
		field_pairs = [struct.unpack_from('<II', blob, pos + i * 8) for i in range(field_count)]
		for i, (key, offset) in enumerate(field_pairs):
			next_offset = entry_size if i == (field_count - 1) else field_pairs[i + 1][1]
			size = next_offset - offset
			self.fields[key] = (offset, size)
		pos += 8 * field_count

		# read data
		for i in range(entry_count):
			entry_pos = pos + (i * entry_size)
			row = self.row_class({key: blob[entry_pos+start:entry_pos+start+end] for (key, (start, end)) in self.fields.items()}, self)
			self.rows.append(row)
			if hasattr(row, 'id'):
				self.by_id[row.id] = row

class Field:
	def __init__(self, key):
		self.key = key
	def __get__(self, instance, owner):
		return self.decode(instance._data[self.key],  instance._context)

	def decode(self, blob, context):
		return blob

class U8(Field):
	def decode(self, blob, context):
		return struct.unpack_from('<B', blob, 0)[0]
class U16(Field):
	def decode(self, blob, context):
		return struct.unpack_from('<H', blob, 0)[0]
class U32(Field):
	def decode(self, blob, context):
		return struct.unpack_from('<I', blob, 0)[0]
class Float(Field):
	def decode(self, blob, context):
		return struct.unpack_from('<f', blob, 0)[0]
class String(Field):
	def decode(self, blob, context):
		try:
			return blob.rstrip(b'\0').decode('utf-8')
		except UnicodeDecodeError:
			return 'UTF-8 err %r' % (blob,)
class Enum(Field):
	def __init__(self, key, values):
		super(Enum, self).__init__(key)
		self.values_en = {zlib.crc32(v[0].encode('utf-8')): v for v in values}
		self.values_jp = {zlib.crc32(v[1].encode('utf-8')): v for v in values}
	def decode(self, blob, context):
		v = struct.unpack('<I', blob)[0]
		try:
			if context.jp_enums:
				return self.values_jp[v]
			else:
				return self.values_en[v]
		except KeyError:
			return '_UNK_%08x_' % v

class Row:
	def __init__(self, data, context):
		self._data = data
		self._context = context

	@classmethod
	def fields(cls):
		if not hasattr(cls, '_fields'):
			cls._fields = []
			for k, v in cls.__dict__.items():
				if isinstance(v, Field):
					cls._fields.append(k)
		return cls._fields
