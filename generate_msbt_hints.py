# for use with https://github.com/asteriation/acnh-eventflow-decompiler

from msbt import *
import sys, sarc, zstandard, json

DUAL_KEYS = set([
	(50,5),
	(50,6),
	(50,7),
	(50,10),
	(50,14),
	(50,20),
	(50,22),
	(50,25),
])
TRIPLE_KEYS_ARG = set([
	(50,17),
])
REPLACEMENTS = {
	(10, 5): '«', # KK Slider songs
	(10, 6): '«',
	(110, 0): '…',
	(110, 1): 'PLAYER',
	(110, 8): 'ISLAND',
	(110, 9): 'ISLAND',
	(110, 18): 'WEEKDAY',
	(110, 19): 'AM/PM',
	(50, 0): '<item>',
	(90, 27): 'YEAR',
	(90, 28): 'MONTH',
	(90, 29): 'DAY',
	(90, 30): 'HH',
	(90, 31): 'MM',
	(100, 4): '__',
	(100, 5): '‹',
	(100, 8): '**',
	(100, 9): '«',
}
END_REPLACEMENTS = {
	(10, 5): '»', # KK Slider songs
	(10, 6): '»',
	(100, 4): '__',
	(100, 5): '›',
	(100, 8): '**',
	(100, 9): '»',
}

def generate_strings(msbt, prefix):
	out = {}
	random_fixups = []

	for label, raw_msg in msbt.data.items():
		bits = []
		for bit in raw_msg.parse():
			if isinstance(bit, str):
				bits.append(bit.replace('\n', ' '))
			elif isinstance(bit, StartTag):
				a, b = bit.a, bit.b
				if a == 0:
					if b == 4:
						bits.append(' ') # page break
				elif a == 10 and b in (0, 1, 2, 3):
					pass # delays
				elif a == 20 and b in (0, 1):
					len1 = bit.arg[0] // 2
					str1 = ''.join(map(chr, bit.arg[1:1+len1]))
					bits.append(f'[target {str1}]')
				elif a == 40 or a == 45:
					pass # animations
				elif (a, b) in REPLACEMENTS:
					bits.append(REPLACEMENTS[(a, b)])
				elif a == 198 and b == 0:
					pass # delay
				elif (a, b) in DUAL_KEYS:
					len1 = bit.arg[0] // 2
					str1 = ''.join(map(chr, bit.arg[1:1+len1]))
					len2 = bit.arg[1+len1] // 2
					str2 = ''.join(map(chr, bit.arg[2+len1:2+len1+len2]))
					bits.append(f'[{str1}|{str2}]')
				elif (a, b) in TRIPLE_KEYS_ARG:
					offs1 = 2
					len1 = bit.arg[offs1] // 2
					str1 = ''.join(map(chr, bit.arg[offs1+1:offs1+1+len1]))
					offs2 = offs1 + 1 + len1
					len2 = bit.arg[offs2] // 2
					str2 = ''.join(map(chr, bit.arg[offs2+1:offs2+1+len2]))
					offs3 = offs2 + 1 + len2
					len3 = bit.arg[offs3] // 2
					str3 = ''.join(map(chr, bit.arg[offs3+1:offs3+1+len3]))
					bits.append(f'[{str1}|{str2}|{str3}]')
				else:
					arg = ''
					if bit.arg:
						arg = ':' + ''.join(map(lambda x: '%04x' % x, bit.arg))
					bits.append(f'<{a}:{b}{arg}>')
			elif isinstance(bit, EndTag):
				a, b = bit.a, bit.b
				if (a, b) in END_REPLACEMENTS:
					bits.append(END_REPLACEMENTS[(a, b)])
				else:
					bits.append(f'</{a}:{b}>')
		msg = ''.join(bits)
		msg = msg.replace('<50:3><50:2>', '[A|An]')
		msg = msg.replace('<50:2>', '[a|an]')
		key = prefix + ':' + label
		if msg == '<60:20>':
			random_fixups.append(key)
		else:
			if len(msg) > 150:
				msg = msg[:149] + '…'
			out[key] = msg

	# add random messages
	for fixup in random_fixups:
		choices = []
		for key, value in out.items():
			if key.startswith(fixup):
				if len(value) > 40:
					value = value[:39] + '…'
				choices.append(value)
		msg = 'RANDOM: ' + ' // '.join(choices)
		out[fixup] = msg
	return out


out = {}
for path in sys.argv[1:]:
	with open(path, 'rb') as f:
		data = f.read()
	if path.endswith('.zs'):
		path = path[:-3]
		data = zstandard.ZstdDecompressor().decompress(data)
	if path.endswith('.sarc'):
		arc = sarc.SARC(data)
		for f in sorted(arc.list_files()):
			data = arc.get_file_data(f)
			msbt = MSBT()
			msbt.load(data)
			prefix = path[path.rindex('/')+1:path.rindex('_')] + '/' + f[:f.rindex('.')]
			out.update(generate_strings(msbt, prefix))

print(json.dumps(out, indent=4))

