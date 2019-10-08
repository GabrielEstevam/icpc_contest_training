import heapq

while True:
	try:
		entry = input().split()
		N = int(entry[0])
		B = int(entry[1])

		listMax = []
		listMin = []
		score = 0
		partialScore = 0
		k = 0

		entry = input().split("")		

		for i in range(N):
			n = int(entry[i])
			if (i < (B - 1)):
				listMax.append(n)
				listMin.append(n*-1)
				heapq.heappush(listMax, at)

	except EOFError:
		break



entry = input().split()
atendentes = []
for i in range(N):
	atendentes.append([0, i, int(entry[i])])

entry = input().split()

heap = []
for i in range(N):
	heapq.heappush(heap, atendentes[i])

tempo = 0
for i in range(M):
	c = int(entry[i])
	h = heapq.heappop(heap)
	atendentes[h[1]][0] += h[2]*c
	heapq.heappush(heap, atendentes[h[1]])

for i in range(N):
	h = heapq.heappop(heap)
print(h[0])
