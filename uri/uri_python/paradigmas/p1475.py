while True:
	try:
		entry = input().split(' ')
		N = int(entry[0])
		C = int(entry[1])
		T1 = int(entry[2])
		T2 = int(entry[3])
		entry = input().split(' ')

		A = [] # Valor otimo
		k = 0
		i = 0
		sobra = 0
		while k < N:
			furo = int(entry[k])
			while i < furo:
				if i > 0:
					A.append(A[i - 1])
				else:
					A.append(0)
				i += 1
			if furo + sobra < C:
				if T2 + 1 <= i and T1 + 1 <= i:
					if A[i - T1 - 1] + T1 <= A[i - T2 - 1] + T2:
						A.append(A[i - T1 - 1] + T1)
						if A[i - T1 - 1] == 0:
							sobra = T1 - i
					else:
						A.append(A[i - T2 - 1] + T2)
						if A[i - T2 - 1] == 0:
							sobra = T2 - i
				elif T1 + 1 <= i:
					A.append(A[i - T1 - 1] + T1)
					if A[i - T1 - 1] == 0:
						sobra = T1 - i
				elif T2 + 1 <= i:
					A.append(A[i - T2 - 1] + T2)
					if A[i - T2 - 1] == 0:
						sobra = T2 - i
				else:
					if T1 < T2:
						A.append(T1)
						sobra = T1 - i
					else:
						A.append(T2)
						sobra = T2 - i
				k += 1
				i += 1
			else:
				break

		print(A[i-1])

	except EOFError:
		break