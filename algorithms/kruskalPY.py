# Kruskal (Arvore Geradora Minima) - Python3
#import sys
#sys.setrecursionlimit(200000)
import time
inicio = time.time()

def find(no):	
	aux = no
	while pai[aux] != aux:
		aux = pai[aux]
	return aux
	#if pai[no] == no:
	#	return no
	#else:
	#	return find(pai[no])

def union(a, b):
	pai[find(a)] = find(b)

entry = input().split(' ')
N = int(entry[0])
M = int(entry[1])
while N != 0:
	k = 0
	print('n:', N)
	m = []
	pai = []
	for i in range(N):
		pai.append(i)	
	for i in range(M):
		entry = input().split(' ')
		m.append([int(entry[2]), int(entry[0]), int(entry[1]), 0])
	m.sort()
	cont = 0 # numero arestas
	i = 0
	while cont < N - 1:
		paix = find(m[i][1])
		paiy = find(m[i][2])
		if paix != paiy:
			pai[paix] = paiy
			cont += 1
			m[i][3] = 1
		i += 1
	soma = 0
	for i in range(M):
		soma += m[i][0] * (1 - m[i][3])
	print(soma)
	entry = input().split(' ')
	N = int(entry[0])
	M = int(entry[1])
print("tempo:", time.time() - inicio)