import struct

blob = open('InsectAppearParamOrig.bcsv', 'rb').read()

ecount, esize, fcount = struct.unpack_from('<IIH', blob, 0)
offset = 0x1C+fcount*8
out = [blob[:offset]]
for o in range(offset, len(blob), esize):
    entry = blob[o:o+esize]
    who = struct.unpack_from('<H', entry, 4)
    start = entry[:6]
    end = entry[-6:]
    midlen = len(entry) - 12
    if who[0] == 646:
        mid = b'\xFF'*midlen
    else:
        mid = b'\x00'*midlen
    out.append(start)
    out.append(mid)
    out.append(end)
    print(who)

open('InsectAppearParam.bcsv', 'wb').write(b''.join(out))



