fn = getFirstFunction()
chk = 0x710012a9e0
while fn != None:
	body = fn.body
	if fn.entryPoint.offset == chk: print('body: %r' % body)
	ranges = list(body.addressRanges)
	if len(ranges) > 1:
		if fn.entryPoint.offset == chk:
			print('possible bad %r with %d ranges' % (fn, body.numAddressRanges))
		ranges = list(body.addressRanges)
		ok = True
		for r in ranges:
			if ((r.minAddress.offset) & 0xF) != 0:
				ok = False
				if fn.entryPoint.offset == chk: print('res 1')
			if getInt(r.minAddress.subtract(4)) != 0:
				ok = False
				if fn.entryPoint.offset == chk: print('res 2')
		if ok:
			for r in ranges:
				fx = createFunction(r.minAddress, None)
				if fn.entryPoint.offset == chk: print('rng: %r result: %r' % (r,fx))
	else:
		r = ranges[0]
		if fn.entryPoint != r.minAddress:
			print('possible midentry bad %r' % fn)
			if ((r.minAddress.offset) & 0xF) == 0 and getInt(r.minAddress.subtract(4)) == 0:
				createFunction(r.minAddress, None)
	fn = getFunctionAfter(fn)
