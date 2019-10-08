for N in range(int(input())):
	n = int(input())
	vagoes = input().split(" ")
	for i in range(n):
		vagoes[i] = int(vagoes[i])
	swaps = 0
	while len(vagoes) > 1:
		maior = max(vagoes)
		swaps += maior - vagoes.index(maior) - 1
		vagoes.remove(maior)
	print("Optimal train swapping takes", swaps,"swaps.")
