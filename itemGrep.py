import bcsv
import specs
import sys

b = bcsv.File(specs.ItemParam)
b.load(open('../ac120upd/romfs/Bcsv/ItemParam.bcsv', 'rb').read())

pall = False
if '-all' in sys.argv:
    sys.argv.remove('-all')
    pall = True

def prow(row):
    if pall:
        for fld in row.fields():
            print(f'{fld} -> {getattr(row,fld)}')
    else:
        print(f'{row.UniqueID} - {row.Label}')

mode = sys.argv[1]
if mode == 'agg':
    key = sys.argv[2]
    agg = {}
    for row in b.rows:
        val = getattr(row, key)
        if val in agg:
            agg[val].append(row)
        else:
            agg[val] = [row]
    for key,rows in agg.items():
        print(f'[{key}] ({len(rows)})')
        for row in rows:
            prow(row)
elif mode == 'eq':
    key = sys.argv[2]
    for row in b.rows:
        if row._c353ef20 < 65535:
            prow(row)
elif mode == 'id':
    for key in sys.argv[2:]:
        if key.startswith('0x'):
            ikey = int(key[2:], 16)
        else:
            ikey = int(key)
        if ikey in b.by_id:
            prow(b.by_id[ikey])

