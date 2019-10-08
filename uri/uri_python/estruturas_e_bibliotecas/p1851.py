import heapq

heap = []
multaPorDia = 0
multa = 0
dias = 0

while True:
	try:
		entry = input().split(" ")
		T = int(entry[0])
		F = int(entry[1])
		heapq.heappush(heap, [T/F, T, F])
		multaPorDia += F
		if dias == 0:
			h = heapq.heappop(heap)
			multaPorDia -= h[2]
			dias += h[1]
		multa += multaPorDia
		dias -= 1
	except EOFError:
		break

multa += dias * multaPorDia
for i in range(len(heap)):
	h = heapq.heappop(heap)
	multaPorDia -= h[2]
	multa += h[1] * multaPorDia
print(multa)
	
