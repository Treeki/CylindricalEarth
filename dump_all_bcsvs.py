import bcsv, binascii, importlib, json, os, os.path, sys

in_path = sys.argv[1]
out_dir = sys.argv[2]
specs_file = sys.argv[3]
specs = importlib.import_module(specs_file.replace('.py', ''))

json_dir = out_dir + '/json'
html_dir = out_dir + '/html'

if not os.path.exists(json_dir):
	os.makedirs(json_dir)
if not os.path.exists(html_dir):
	os.makedirs(html_dir)

for filename, row_class in specs.lookup.items():
	html = []
	html.append('<!DOCTYPE html>')
	html.append('<html>')
	html.append('<body>')
	objs = []

	html.append('<h1>%s</h1>' % filename)

	b = bcsv.File(row_class)
	with open('%s/%s' % (in_path, filename), 'rb') as f:
		b.load(f.read())

	html.append('<table>')
	html.append('<tr>')
	for field in row_class.fields():
		html.append('<th>%s</th>' % field)
	html.append('</tr>')
	for row in b.rows:
		html.append('<tr>')
		obj = {}
		for field in row_class.fields():
			value = getattr(row, field)
			html.append('<td>%r</td>' % (value, ))
			if isinstance(value, bytes):
				obj[field] = binascii.hexlify(value).decode('ascii')
		html.append('</tr>')
		objs.append(obj)
	html.append('</table>')

	html.append('</body>')
	html.append('</html>')

	with open('%s/%s.html' % (html_dir, filename.replace('.bcsv', '')), 'w') as f:
		for line in html:
			f.write(line)
			f.write('\n')
	with open('%s/%s.json' % (json_dir, filename.replace('.bcsv', '')), 'w') as f:
		json.dump(objs, f, indent=4)
