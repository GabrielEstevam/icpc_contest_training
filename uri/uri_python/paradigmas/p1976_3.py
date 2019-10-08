class A:
    def __init__(self, M, N):
        self.m = M
        self.n = N
        self.flag = 0
        self.corte = -1
        self.multiplicacoes = -1

def minimizaMult(As, M, i, j, Empate):
    if i == j:
        M[i][j - i].multiplicacoes = 0
        M[i][j - i].corte = i
    else:
        for k in range(i, j, 1):
            #print("i, j, k: ", i, j, k)
            if M[i][k - i].flag == 0:
                Empate = minimizaMult(As, M, i, k, Empate)
            if M[k + 1][j - (k + 1)].flag == 0:
                Empate = minimizaMult(As, M, k + 1, j, Empate)
            mult = M[i][k - i].multiplicacoes + M[k + 1][j - (k + 1)].multiplicacoes + As[i].m * As[k].n * As[j].n
            if mult < M[i][j - i].multiplicacoes or M[i][j - i].multiplicacoes == -1:
                M[i][j - i].multiplicacoes = mult
                M[i][j - i].corte = k
            elif mult == M[i][j - i].multiplicacoes:
                Empate = 1
    M[i][j - i].flag = 1
    return Empate

def printSaida(i, j, M, saida):
    if i == j:
            return "A"+str(i+1)
    elif i+1 == j:
            return "A"+str(i+1)+"A"+str(j+1)+""
    else:
        saida1 = printSaida(i, M[i][j - i].corte, M, saida)
        if i != M[i][j-i].corte:
            saida1 = "("+saida1+")"
        saida2 = printSaida(M[i][j - i].corte + 1, j, M, saida)
        if M[i][j-i].corte+1 != j:
            saida2 = "(" + saida2 + ")"
    return saida1+saida2

N = int(input())
while N > 0:
    As = []
    for i in range(N):
        entrada = input().split(" ")
        As.append(A(int(entrada[0]), int(entrada[1])))

    M = []
    for i in range(N):
        M.append([])
        for j in range(i, N, 1):
            M[i].append(A(i, j))

    Empate = minimizaMult(As, M, 0, N-1, 0)
    M[0][N-1].flag = 1

    if Empate:
        mult = 0
        for i in range(len(M)):
            for j in range(len(M[i])):
                if M[i][j].multiplicacoes > mult:
                    mult = M[i][j].multiplicacoes
        print(mult)
    else:
        print("("+printSaida(0, N-1, M, "")+")")

    N = int(input())