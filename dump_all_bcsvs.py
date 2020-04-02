import bcsv, binascii, csv, importlib, json, os, os.path, sys

in_path = sys.argv[1]
out_dir = sys.argv[2]
specs_file = sys.argv[3]
specs = importlib.import_module(specs_file.replace('.py', ''))

csv_dir = out_dir + '/csv'
json_dir = out_dir + '/json'
html_dir = out_dir + '/html'

if not os.path.exists(csv_dir):
	os.makedirs(csv_dir)
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

	csvw = csv.writer(open('%s/%s.csv' % (csv_dir, filename.replace('.bcsv', '')), 'w'))

	html.append('<table>')
	html.append('<tr>')
	for field in row_class.fields():
		html.append('<th>%s</th>' % field)
	csvw.writerow(row_class.fields())
	html.append('</tr>')
	for row in b.rows:
		html.append('<tr>')
		obj = {}
		crow = []
		for field in row_class.fields():
			value = getattr(row, field)
			html.append('<td>%r</td>' % (value, ))
			if isinstance(value, bytes):
				value = binascii.hexlify(value).decode('ascii')
			crow.append(value)
			obj[field] = value
		html.append('</tr>')
		objs.append(obj)
		csvw.writerow(crow)
	html.append('</table>')

	html.append('</body>')
	html.append('</html>')

	with open('%s/%s.html' % (html_dir, filename.replace('.bcsv', '')), 'w') as f:
		for line in html:
			f.write(line)
			f.write('\n')
	with open('%s/%s.json' % (json_dir, filename.replace('.bcsv', '')), 'w') as f:
		json.dump(objs, f, indent=4)
