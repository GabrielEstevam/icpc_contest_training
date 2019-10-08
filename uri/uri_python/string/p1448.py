try:
	N = int(input())
	for n in range(N):
		entry1 = input()
		while len(entry1) == 0:
			entry1 = input()
		entry2 = input()
		while len(entry2) == 0:
			entry2 = input()
		entry3 = input()
		while len(entry3) == 0:
			entry3 = input()
		a = 0
		b = 0
		ia = len(entry1)
		ib = len(entry1)
		if len(entry1) == len(entry2) and len(entry1) == len(entry3):
			for i in range(len(entry1)-1, -1, -1):
				if entry2[i] == entry1[i]:
					a += 1
					ia = i
				if entry3[i] == entry1[i]:
					b += 1
					ib = i
			print("Instancia", n+1)
			if a > b:
				print("time", 1)
			elif b > a:
				print("time", 2)
			else:
				if ia < ib:
					print("time", 1)
				elif ib < ia:
					print("time", 2)
				else:
					print("empate")
			print("")
except EOFError:
	NULL