import bcsv, binascii, csv, html, importlib, json, os, os.path, sys

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
	bits = []
	bits.append('<!DOCTYPE html>')
	bits.append('<html>')
	bits.append('<body>')
	objs = []

	bits.append('<h1>%s</h1>' % filename)

	b = bcsv.File(row_class)
	with open('%s/%s' % (in_path, filename), 'rb') as f:
		b.load(f.read())

	csvw = csv.writer(open('%s/%s.csv' % (csv_dir, filename.replace('.bcsv', '')), 'w'))

	bits.append('<table>')
	bits.append('<tr>')
	for field in row_class.fields():
		bits.append('<th>%s</th>' % field)
	csvw.writerow(row_class.fields())
	bits.append('</tr>')
	for row in b.rows:
		bits.append('<tr>')
		obj = {}
		crow = []
		for field in row_class.fields():
			value = getattr(row, field)
			if isinstance(value, bytes):
				htmlValue = binascii.hexlify(value).decode('ascii')
				dataValue = htmlValue
			elif isinstance(value, tuple):
				htmlValue = "<span title='%s'>%s</span>" % (html.escape(value[1], True), html.escape(value[0]))
				dataValue = value
			else:
				htmlValue = repr(value)
				dataValue = htmlValue
			bits.append('<td>%s</td>' % htmlValue)
			crow.append(dataValue)
			obj[field] = dataValue
		bits.append('</tr>')
		objs.append(obj)
		csvw.writerow(crow)
	bits.append('</table>')

	bits.append('</body>')
	bits.append('</html>')

	with open('%s/%s.html' % (html_dir, filename.replace('.bcsv', '')), 'w') as f:
		for line in bits:
			f.write(line)
			f.write('\n')
	with open('%s/%s.json' % (json_dir, filename.replace('.bcsv', '')), 'w') as f:
		json.dump(objs, f, indent=4)
