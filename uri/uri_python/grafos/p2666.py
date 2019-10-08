import math
class No:
    def __init__(self, Imp):
        self.vizinho = []
        self.distancia = []
        self.impostos = Imp
        self.distancias = 0
        self.vizinhos = 0
        self.pai = 0
        self.distanciaPai = 0

    def insertNo(self, no, dist):
        self.vizinho.append(no)
        self.distancia.append(dist)
        self.vizinhos += 1

entrada = input().split(" ")
N = int(entrada[0])
C = int(entrada[1])
entrada = input().split(" ")

I = []
for i in range(N):
    I.append(No(int(entrada[i])))

for i in range(N-1):
    entrada = input().split(" ")
    I[int(entrada[0])-1].insertNo(int(entrada[1])-1, int(entrada[2]))
    I[int(entrada[1])-1].insertNo(int(entrada[0])-1, int(entrada[2]))

pilha = [0]
for i in range(N):
    for j in range(I[pilha[i]].vizinhos):
        if I[pilha[i]].vizinho[j] != I[pilha[i]].pai:
            pilha.append(I[pilha[i]].vizinho[j])
            I[I[pilha[i]].vizinho[j]].pai = pilha[i]
            I[I[pilha[i]].vizinho[j]].distanciaPai = I[pilha[i]].distancia[j]

for i in range(N-1):
    k = pilha[N-1-i]
    I[I[k].pai].distancias += 2*math.ceil(I[k].impostos/C)*I[k].distanciaPai + I[k].distancias
    I[I[k].pai].impostos += I[k].impostos

print(I[pilha[0]].distancias)