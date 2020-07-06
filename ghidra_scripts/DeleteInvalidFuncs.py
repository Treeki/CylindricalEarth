
f = getFirstFunction()
while f != None:
	try:
		if f.body.numAddresses == 1 and getInt(f.entryPoint) == 0:
			print('yeah we can remove %r' % f)
			removeFunction(f)
	except:
		pass
	f = getFunctionAfter(f)
