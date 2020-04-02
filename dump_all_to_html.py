import bcsv, specs, sys

path = sys.argv[1]

for filename, row_class in specs.lookup.items():
	out = []
	out.append('<!DOCTYPE html>')
	out.append('<html>')
	out.append('<body>')

	out.append('<h1>%s</h1>' % filename)

	b = bcsv.File(row_class)
	with open('%s/%s' % (path, filename), 'rb') as f:
		b.load(f.read())

	out.append('<table>')
	out.append('<tr>')
	for field in row_class.fields():
		out.append('<th>%s</th>' % field)
	out.append('</tr>')
	for row in b.rows:
		out.append('<tr>')
		for field in row_class.fields():
			out.append('<td>%r</td>' % (getattr(row, field), ))
		out.append('</tr>')
	out.append('</table>')

	out.append('</body>')
	out.append('</html>')

	with open('tables/%s.html' % (filename.replace('.bcsv', '')), 'w') as f:
		for line in out:
			f.write(line)
			f.write('\n')
