from byml import Byml
import sys

KEY_TYPE_ID   = '5c65d8b5' #TypeName
KEY_FIELDS    = 'a2fb4a94' #Members
KEY_FIELD_ID  = '25efa387' #Name
KEY_SIZE      = 'b4a58247' #Size
KEY_OFFSET    = 'a7bb2e42' #Offset
KEY_LENGTH_1  = '1e0eae33' #Length1
KEY_LENGTH_2  = 'a9f41a61' #Length2
KEY_ALIGNMENT = '4a4cb5b4' #Alignment

MAX_TYPE_NAME_LEN = 0
MAX_FIELD_NAME_LEN = 0

import json
with open('save_keys.json', 'r') as f:
    blob = json.load(f)
    FIELD_KEYS = {int(k): v for k,v in blob['f'].items() if v is not None}
    TYPE_KEYS = {int(k): v for k,v in blob['t'].items() if v is not None}

KEY_CHECK_DEBUG = False
if KEY_CHECK_DEBUG:
    with open('save_keys_manualCleanup2.json', 'r') as f:
        blob = json.load(f)
        KEY_CHECK_FIELDS = {int(k): v for k,v in blob['f'].items()}
        KEY_CHECK_TYPES = {int(k): v for k,v in blob['t'].items()}
        FIELD_KEYS = {k: v[0] for k,v in KEY_CHECK_FIELDS.items() if len(v) == 1}
        TYPE_KEYS = {k: v[0] for k,v in KEY_CHECK_TYPES.items() if len(v) == 1}


def cutName(name):
    return name.replace('::Game::', 'G')

class SaveType:
    def __init__(self, id, name, size, alignment):
        self.id = id
        self.name = name
        self.size = size
        self.alignment = alignment
        self.fields = []

        global MAX_TYPE_NAME_LEN
        MAX_TYPE_NAME_LEN = max(MAX_TYPE_NAME_LEN, len(cutName(name)))

    def dumpPseudoC(self):
        lines = []

        my_name = cutName(self.name)
        cmt_pad = ' ' * (MAX_TYPE_NAME_LEN - len(my_name) + 8)
        if KEY_CHECK_DEBUG:
            lines.append(f'  {KEY_CHECK_TYPES[self.id]}')
        lines.append(f'struct {my_name} {{{cmt_pad} /* 0x{self.size:x} big, align {self.alignment} */')
        offset = 0
        for f in self.fields:
            tn = cutName(f.type_name)
            tn_pad = ' ' * (MAX_TYPE_NAME_LEN - len(tn))
            n_pad = ' ' * (MAX_FIELD_NAME_LEN - len(f.name))
            if f.offset > offset:
                lines.append(f'  u8 gap_{offset:x}[{f.offset - offset}];')

            if f.length[1] > 1:
                length_desc = f'[{f.length[0]}][{f.length[1]}]'
            elif f.length[0] > 1:
                length_desc = f'[{f.length[0]}]'
            else:
                length_desc = ''
            n_pad += ' ' * (12 - len(length_desc))

            if KEY_CHECK_DEBUG and len(KEY_CHECK_TYPES[f.type_id]) > 1:
                lines.append(KEY_CHECK_TYPES[f.type_id])

            if KEY_CHECK_DEBUG and len(KEY_CHECK_FIELDS[f.id]) > 1:
                lines.append(f'  {tn} {f.id:08x} {KEY_CHECK_FIELDS[f.id]}')
            else:
                lines.append(f'  {tn}{tn_pad} {f.name}{length_desc};{n_pad} // @0x{f.offset:x} size 0x{f.size:x}, align {f.alignment}')

            offset = f.offset + f.size * f.length[0] * f.length[1]
        lines.append('};')
        return lines

class SaveField:
    def __init__(self, type_id, type_name, id, name, size, offset, length_1, length_2, alignment):
        self.type_id = type_id
        self.type_name = type_name
        self.id = id
        self.name = name
        self.size = size
        self.offset = offset
        self.length = (length_1, length_2)
        self.alignment = alignment

        global MAX_FIELD_NAME_LEN
        MAX_FIELD_NAME_LEN = max(MAX_FIELD_NAME_LEN, len(name))

class SaveDefinition:
    def __init__(self, data):
        yaml = Byml(data).parse()
        self.types = {}

        struct_types = set([e[KEY_TYPE_ID] for e in yaml])
        struct_names = {k: TYPE_KEYS.get(k, 's_%08x' % k) for k in struct_types}

        for entry in yaml:
            type_id = entry[KEY_TYPE_ID]
            type_obj = SaveType(type_id, struct_names[type_id], entry[KEY_SIZE], entry[KEY_ALIGNMENT])

            for field in entry[KEY_FIELDS]:
                field_type_id = field[KEY_TYPE_ID]
                field_id = field[KEY_FIELD_ID]
                type_obj.fields.append(SaveField(
                    field_type_id, struct_names.get(field_type_id, TYPE_KEYS.get(field_type_id, '_%08x' % field_type_id)),
                    field_id, FIELD_KEYS.get(field_id, '_%08x' % field_id),
                    field[KEY_SIZE], field[KEY_OFFSET], field[KEY_LENGTH_1],
                    field.get(KEY_LENGTH_2, 1), field[KEY_ALIGNMENT]))
            type_obj.fields.sort(key=lambda f: f.offset)
            self.types[type_obj.id] = type_obj



import os
type_hashes = set()
field_hashes = set()
for name in os.listdir(sys.argv[1]):
    if name.endswith('.byml'):
        sd = SaveDefinition(open(sys.argv[1] + '/' + name, 'rb').read())
        for type_obj in sd.types.values():
            type_hashes.add(type_obj.id)
            for field in type_obj.fields:
                type_hashes.add(field.type_id)
                field_hashes.add(field.id)

with open('typeHashes', 'w') as f:
    for h in type_hashes:
        if h not in TYPE_KEYS or TYPE_KEYS[h] == None:
            f.write(f'{h:08x}:00000000\n')
with open('fieldHashes', 'w') as f:
    for h in field_hashes:
        if h not in FIELD_KEYS or FIELD_KEYS[h] == None:
            f.write(f'{h:08x}:00000000\n')
#with open('all_save_field_keys.json', 'w') as f:
#    json.dump({'t': list(type_hashes), 'f': list(field_hashes)}, f)


def dump(path, version):
    types = {}
    for name in ('P00', 'P01', 'P02', 'P03', 'S00'):
        sd = SaveDefinition(open(f'{path}/{name}_{version}.byml', 'rb').read())
        types.update(sd.types)

    jtypes = {}
    jprimitives = {}
    for t in types.values():
        jtypes[t.id] = dict(
            name=t.name, size=t.size, alignment=t.alignment, fields=[]
        )
        for f in t.fields:
            if f.type_id not in types and f.type_id not in jprimitives:
                jprimitives[f.type_id] = dict(name=f.type_name, size=f.size)
            jtypes[t.id]['fields'].append(dict(
                id=f.id, name=f.name, type=f.type_id,
                size=f.size, offset=f.offset, length=f.length,
                alignment=f.alignment
            ))

    with open(f'save_schema_{version}_pseudoC.h', 'w') as f:
        for t in types.values():
            for line in t.dumpPseudoC():
                f.write(line)
                f.write('\n')

    # if a primitive type starts with ::Game::Save then something might be up
    for prim in jprimitives.values():
        if prim['name'].startswith('::Game::Save'):
            print('? Is %r ok?' % prim)

    with open(f'save_schema_{version}.json', 'w') as f:
        json.dump(dict(types=jtypes, primitives=jprimitives), f, indent=4)

def print_single_file(path):
    sd = SaveDefinition(open(path, 'rb').read())
    for type_obj in sd.types.values():
        type_obj.print()

if __name__ == '__main__':
    # print_single_file(sys.argv[1])
    dump(sys.argv[1], '111_103')
    dump(sys.argv[1], '120_109')
    dump(sys.argv[1], '131080_131078')
    dump(sys.argv[1], '262152_262146')
