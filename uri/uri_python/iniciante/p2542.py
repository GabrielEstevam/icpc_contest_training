while True:
	try:
		N = int(input())
		entry = input().split(' ')
		lm = int(entry[0])
		ll = int(entry[1])
		mm = []
		ml = []
		for i in range(lm):
			mm.append(input().split(' '))
		for i in range(ll):
			ml.append(input().split(' '))
		entry = input().split(' ')
		cm = int(entry[0])
		cl = int(entry[1])
		a = int(input())
		if int(mm[cm-1][a-1]) > int(ml[cl-1][a-1]):
			print("Marcos")
		elif int(mm[cm-1][a-1]) < int(ml[cl-1][a-1]):
			print("Leonardo")
		else:
			print("Empate")

	except EOFError:
		break