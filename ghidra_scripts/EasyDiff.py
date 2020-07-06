# easy... and cheap

import json

s_text = getMemoryBlock('.text')
s_init_array = getMemoryBlock('.init_array')
s_rodata = getMemoryBlock('.rodata.1') # not sure if it's .1 in all bins?
s_data = getMemoryBlock('.data')

anchors = {}

def get_all_inits():
	addr = s_init_array.start
	while addr < s_init_array.end:
		yield getDataAt(addr).value
		addr = addr.add(8)

blob = {}
blob['anchors'] = []

for i, init in enumerate(get_all_inits()):
    # output.write('init %d: %x\n' % (i, init.offset))
    anchors[init] = i
    blob['anchors'].append(init.offset)

fn = getFirstFunction()
anchor = toAddr(blob['anchors'][0])
anchorIndex = 0

blob['nodes'] = []

while fn != None:
    if fn.entryPoint in anchors:
        anchor = fn.entryPoint
        anchorIndex = anchors[anchor]
        if anchorIndex == len(anchors) - 1:
            break
    else:
        blob['nodes'].append([anchorIndex, fn.entryPoint.subtract(anchor), getInt(fn.entryPoint)])
    fn = getFunctionAfter(fn)

with open('/data/switch/%s.info' % currentProgram.name, 'w') as output:
    json.dump(blob, output, indent=2)
