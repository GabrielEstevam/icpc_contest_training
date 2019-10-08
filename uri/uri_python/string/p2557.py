while True:
	try:
		entry = input().split('=')
		J = entry[1]
		[R, L] = entry[0].split('+')
		if J == 'J':
			print(int(R)+int(L))
		elif R == 'R':
			print(int(J)-int(L))
		elif L == 'L':
			print(int(J)-int(R))
	except EOFError:
		break
