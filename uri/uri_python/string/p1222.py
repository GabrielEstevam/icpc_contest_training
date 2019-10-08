import math
while True:
	try:
		entry = input().split(" ")
		N = int(entry[0])
		L = int(entry[1])
		C = int(entry[2])
		entry = input().split(" ")
		linhas = 0
		ls = 0
		for i in range(len(entry)):
			if ls > 0:
				ls += 1
			if ls + len(entry[i]) <= C:
				ls += len(entry[i])
				if ls >= C:
					linhas += 1
					ls = 0
			else:
				linhas += 1
				ls = len(entry[i])
		if ls > 0:
			linhas += 1
		print(math.ceil(linhas/L))
				
	except EOFError:
		break
