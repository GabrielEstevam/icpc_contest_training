entry = input().split(' ')
times = int(entry[0])
partidas = int(entry[1])
while partidas != 0 or times != 0:
	pontos = 0
	for i in range(times):
		entry = input().split(' ')
		pontos += int(entry[1])
	print(3*partidas - pontos)

	entry = input().split(' ')
	times = int(entry[0])
	partidas = int(entry[1])