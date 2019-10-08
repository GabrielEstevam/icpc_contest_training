def ordena(t):
    return -1*t[0], -1*t[1], -1*t[2], t[3]

paises = []
N = int(input())
for n in range(N):
	entry = input().split(' ')
	paises.append([int(entry[1]), int(entry[2]), int(entry[3]), entry[0]])
paises = sorted(paises, key=ordena)
for i in range(N):
	print(paises[i][3], paises[i][0], paises[i][1], paises[i][2])

