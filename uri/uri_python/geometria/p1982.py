import math

def produtoCruzado (x1, y1, x2, y2):
	return x1*y2 - x2*y1

def calculaAngulo(pivo, ponto):
	#return produtoCruzado(1, 0, ponto[0]-pivo[0], ponto[1]-pivo[1])	
	return math.atan2(ponto[1]-pivo[1], ponto[0]-pivo[0])

def curva(a, b, c):
	# retorna 1 se a curva for para direita
	d = produtoCruzado(b[0]-a[0], b[1]-a[1], c[0]-b[0], c[1]-b[1])
	if d < 0:
		return 1
	return 0

N = int(input())
while N > 0:
	pontos = []
	for i in range(N):
		entry = input().split(" ")
		pontos.append([int(entry[0]), int(entry[1])])
	
	from operator import itemgetter, attrgetter
	pontos.sort(key=itemgetter(1))

	pivo = pontos[0]
	angulo = [[0, pontos[0]]]
	for i in range(1, len(pontos)):
		angulo.append([calculaAngulo(pivo, pontos[i]), pontos[i]])
	angulo.sort(key=itemgetter(0))
	print('a:', angulo)
	pilha = []
	pilha.append(pivo)
	pilha.append(angulo[1][1])
	for i in range(2, len(pontos)):
		pilha.append(angulo[i][1])
		while True:
			size = len(pilha)
			if size < 3:
				break
			if curva(pilha[size-3], pilha[size-2], pilha[size-1]):
				del pilha[size-2]
			else:
				break
	print('p:', pilha)
	d = 0
	for i in range(1, len(pilha)):
		d += math.sqrt(pow(pilha[i][0] - pilha[i-1][0], 2) + pow(pilha[i][1] - pilha[i-1][1], 2))
	d += math.sqrt(pow(pilha[len(pilha)-1][0] - pilha[0][0], 2) + pow(pilha[len(pilha)-1][1] - pilha[0][1], 2))

	print('Tera que comprar uma fita de tamanho', format(d, '.2f')+'.')

	N = int(input())

