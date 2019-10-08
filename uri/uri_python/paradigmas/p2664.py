entrada = input().split(" ")
T = int(entrada[0])
M = int(entrada[1])
N = int(entrada[2])

largura = (N-M+1)
table = []
aux = []
if largura == 2:
    print(2)
elif largura > 2:
    if largura%2 == 0:
        largura = int(largura/2)
        for i in range(largura):
            aux.append(1)
            table.append(1)
        for i in range(T-1):
            for j in range(largura):
                if j == 0:
                    table[j] = aux[j+1]
                elif j == largura - 1:
                    table[j] = aux[j]+aux[j-1]
                else:
                    table[j] = aux[j-1] + aux[j+1]
            for j in range(largura):
                aux[j] = table[j]%1000000007
        print((sum(aux)*2)%1000000007)
    else:
        largura = int(largura/2)
        largura += 1
        for i in range(largura):
            aux.append(1)
        for i in range(T-1):
            for j in range(largura):
                if j == 0:
                    table[j] = aux[1]
                elif j == largura - 1:
                    table[j] = 2*aux[j]
                else:
                    table[j] = aux[j-1] + aux[j+1]
            for j in range(largura):
                aux[j] = table[j] % 1000000007
        print((sum(aux)*2-aux[largura-1])% 1000000007)
else:
    print(0)