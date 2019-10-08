T = int(input())
for t in range(T):
	bonus = int(input())
	entry = input().split(" ")
	Ad = int(entry[0])
	Dd = int(entry[1])
	Ld = int(entry[2])
	entry = input().split(" ")
	Ag = int(entry[0])
	Dg = int(entry[1])
	Lg = int(entry[2])
	D = (Ad+Dd)/2
	if Ld % 2 == 0:
		D += bonus
	G = (Ag+Dg)/2
	if Lg % 2 == 0:
		G += bonus
	if D > G:
		print("Dabriel")
	elif G > D:
		print("Guarte")
	else:
		print("Empate")
