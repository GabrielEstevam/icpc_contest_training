for n in range(int(input())):
	M = []
	for i in range(9):
		entry = input().split(' ')
		row = []
		for i in range(9):
			row.append(int(entry[i])-1)
		M.append(row)

	flagSudoku = True
	for i in range(9):
		flagNum = True
		
		for j in range(9):
			flag = False
			for k in range(9):
				if (M[j][k] == i):
					flag = True
					break
			if flag == False:
				flagNum = False
				break
		
		if flagNum == False:
			flagSudoku = False
			break

		for j in range(9):
			flag = False
			for k in range(9):
				if (M[k][j] == i):
					flag = True
					break
			if flag == False:
				flagNum = False
				break
		
		if flagNum == False:
			flagSudoku = False
			break

		for j in range(3):
			for k in range(3):
				flag = False
				for l in range(3):
					for m in range(3):
						if (M[3*j+l][3*k+m] == i):
							flag = True
							
				if flag == False:
					flagNum = False
					break
		
		if flagNum == False:
			flagSudoku = False
			break

	print('Instancia', n+1)
	if flagSudoku:
		print('SIM')
	else:
		print('NAO')
	print('')

