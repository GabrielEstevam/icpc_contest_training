import math

pontos = []

def closestPair(a, b):
	#print("a, b:", a, b)
	if (b - a == 3):
		d1_2 = math.sqrt(pow(pontos[a][0]-pontos[a+1][0], 2) + pow(pontos[a][1]-pontos[a+1][1], 2))
		d1_3 = math.sqrt(pow(pontos[a][0]-pontos[a+2][0], 2) + pow(pontos[a][1]-pontos[a+2][1], 2))
		d2_3 = math.sqrt(pow(pontos[a+1][0]-pontos[a+2][0], 2) + pow(pontos[a+1][1]-pontos[a+2][1], 2))
		if d1_2 <= d1_3 and d1_2 <= d2_3:
			return d1_2
		elif d1_3 <= d1_2 and d1_3 <= d2_3:
			return d1_3
		else:
			return d2_3
	elif (b - a == 2):
		return math.sqrt(pow(pontos[a][0]-pontos[a+1][0], 2) + pow(pontos[a][1]-pontos[a+1][1], 2))
	elif (b - a <= 1):
		return 10000		
	else:
		delta = (pontos[b-1][0] - pontos[a][0])/2
		for i in range(a, b):
			if pontos[i][0] >= pontos[a][0] + delta:
				d1 = closestPair(a, i)
				d2 = closestPair(i, b)
				break
		if d1 <= d2:
			dmin = d1
		else:
			dmin = d2
		if (b - a < 16):
			for i in range(a, b):
				for j in range(a, b):
					if i != j:
						d = math.sqrt(pow(pontos[i][0]-pontos[j][0], 2) + pow(pontos[i][1]-pontos[j][1], 2))
						if d < dmin:
							dmin = d
		else:
			for i in range(a, a+16):
				for j in range(a, a+16):
					if i != j:
						d = math.sqrt(pow(pontos[i][0]-pontos[j][0], 2) + pow(pontos[i][1]-pontos[j][1], 2))
						if d < dmin:
							dmin = d
		return dmin

N = int(input())
while (N != 0):
	for i in range(N):
		entry = input().split(" ")
		pontos.append([float(entry[0]), float(entry[1])])
	pontos.sort()
	d = closestPair(0,N)
	if d < 10000:
		print("{0:.4f}".format(d))
	else:
		print("INFINITY")
	pontos.clear()	
	N = int(input())
