while True:
	try:
		entry = input().split(':')
		h = str(bin(int(entry[0])+16))
		m = str(bin(int(entry[1])+64))
		print(' ____________________________________________')
		print('|                                            |')
		print('|    ____________________________________    |_')
		print('|   |                                    |   |_)')
		print('|   |   8         4         2         1  |   |')
		print('|   |                                    |   |')
		out = '|   |   '
		if h[3] == '1':
			out += 'o'
		else:
			out += ' '
		out += '         '
		if h[4] == '1':
			out += 'o'
		else:
			out += ' '
		out += '         '
		if h[5] == '1':
			out += 'o'
		else:
			out += ' '
		out += '         '
		if h[6] == '1':
			out += 'o'
		else:
			out += ' '
		out += '  |   |'
		print(out)
		print('|   |                                    |   |')
		print('|   |                                    |   |')
		out = '|   |   '
		if m[3] == '1':
			out += 'o'
		else:
			out += ' '
		out += '     '
		if m[4] == '1':
			out += 'o'
		else:
			out += ' '
		out += '     '
		if m[5] == '1':
			out += 'o'
		else:
			out += ' '
		out += '     '
		if m[6] == '1':
			out += 'o'
		else:
			out += ' '
		out += '     '
		if m[7] == '1':
			out += 'o'
		else:
			out += ' '
		out += '     '
		if m[8] == '1':
			out += 'o'
		else:
			out += ' '
		out += '  |   |'
		print(out)
		print('|   |                                    |   |')
		print('|   |   32    16    8     4     2     1  |   |_')
		print('|   |____________________________________|   |_)')
		print('|                                            |')
		print('|____________________________________________|')
		print('')
	except EOFError:
		break