import json

s_text = getMemoryBlock('.text')
s_init_array = getMemoryBlock('.init_array')
s_rodata = getMemoryBlock('.rodata.1') # not sure if it's .1 in all bins?
s_data = getMemoryBlock('.data')

def get_all_inits():
	addr = s_init_array.start
	while addr < s_init_array.end:
		yield getDataAt(addr).value
		addr = addr.add(8)

with open('/data/switch/ac120.info', 'r') as f:
    blob = json.load(f)

anchors = list(get_all_inits())
assert(len(anchors) == len(blob['anchors']))

for anchorIndex, anchorOffset, firstInt in blob['nodes']:
    oldAddr = blob['anchors'][anchorIndex] + anchorOffset
    newAddr = anchors[anchorIndex].add(anchorOffset)
    firstInt &= 0xFFFFFFFF
    if (firstInt & 0xFC000000) == 0x14000000:
        # skip b
        continue
    if (firstInt & 0x9F000000) == 0x90000000:
        # need to take adrp into account
        adrpOffset = (firstInt & 0x00FFFFE0) >> 3
        adrpOffset |= (firstInt & 0x60000000) >> 29
        origDest = (oldAddr + (adrpOffset << 12)) & ~0xFFF
        #print('adrp compensate oldAddr=%x newAddr=%r firstInt=%x check=%x adrpOffset=%x' % (oldAddr, newAddr, firstInt&0xffffffff, getInt(newAddr)&0xffffffff, adrpOffset))
        adrpOffset = (origDest - (newAddr.offset & ~0xFFF)) >> 12
        firstInt &= 0x9F00001F
        firstInt |= (adrpOffset & 3) << 29
        firstInt |= (adrpOffset & 0x1FFFFC) << 3
    check = getInt(newAddr) & 0xFFFFFFFF
    if check != firstInt:
        print('mismatch on %d:%x %x -> %r' % (anchorIndex, anchorOffset, oldAddr, newAddr))

