import heapq

entry = input().split()
N = int(entry[0])
M = int(entry[1])

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
