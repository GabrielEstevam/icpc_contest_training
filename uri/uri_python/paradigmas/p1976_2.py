class A:
    def __init__(self, M, N):
        self.m = M
        self.n = N
        self.flag = 0
        self.corte = 0
        self.multiplicacoes = 0

def minimizaMult(As, M, i, j, Empate):
    print("i, j:", i, j)
    if j - i > 1:
        for k in range(i, j, 1):
            print("k: ", k)
            if M[i][k - i].flag == 0:
                minimizaMult(As, M, i, k, Empate)
                M[i][k - i].flag = 1
            if M[k + 1][j - k - 1].flag == 0:
                minimizaMult(As, M, k + 1, j, Empate)
                M[k + 1][j - k - 1].flag = 1
            mult = M[i][k - i].multiplicacoes + M[k + 1][j - k - 1].multiplicacoes + As[i].m * As[k].n * As[j].n
            if mult < M[i][j - i].multiplicacoes:
                M[i][j - i].multiplicacoes = mult
                M[i][j - i].corte = k
            elif mult == M[i][j - i].multiplicacoes:
                Empate = 1
N = int(input())
while N > 0:
    As = []
    for i in range(N):
        entrada = input().split(" ")
        As.append(A(int(entrada[0]), int(entrada[1])))

    M = []
    for i in range(N):
        M.append([])
        for j in range(N-i):
            M[i].append(A(i, j+i))
            if j == 0:
                M[i][0].flag = 1
                M[i][0].corte = i
            else:
                M[i][j].multiplicacoes = As[M[i][j].m].m * As[M[i][j].n].m * As[M[i][j].n].n + M[i][j-1].multiplicacoes
                M[i][j].corte = j+i

    Empate = 0
    minimizaMult(As, M, 0, N-1, Empate)
    M[0][N-1].flag = 1


    print("##")
    for i in range(len(M)):
        for j in range(len(M[i])):
            print(M[i][j].m, M[i][j].n, M[i][j].multiplicacoes, M[i][j].corte)

    if Empate:
        mult = 0
        for i in range(len(M)):
            for j in range(len(M[i])):
                if M[i][j].multiplicacoes > mult:
                    mult = M[i][j].multiplicacoes
        print(mult)
    else:
        print("nada")

    N = int(input())