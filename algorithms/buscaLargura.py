''' (Grafos) Busca Largura '''
def inverte(A):
	num = ""
	for i in str(A):
		num = i + num
	return int(num) 

def buscaLargura(A, B):
	flag = []
	for i in range(10000):
		flag.append(True)
	fila = [[A, 0]]
	while (len(fila) > 0):
		n = fila[0]
		fila.remove(fila[0])
		a = inverte(n[0])
		if a == B:
			return n[1] + 1
		if (a < 10000):		
			if (flag[a]):
				fila.append([a, n[1] + 1])
				flag[a] = False
		a = n[0] + 1
		if a == B:
			return n[1] + 1
		if (a < 10000):
			if (flag[a]):		
				fila.append([a, n[1] + 1])
				flag[a] = False
	return -1

for t in range(int(input())):
	entry = input().split(" ")
	print(buscaLargura(int(entry[0]), int(entry[1])))


