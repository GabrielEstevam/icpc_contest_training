def ordena(t):
    return  t[1]*-1, t[0]
for T in range(int(input())):
    entry = input().split(" ")
    N = int(entry[0])
    K = int(entry[1])
    presentes = []
    for i in range(N):
        entry = input().split()
        presentes.append((int(entry[0]), int(int(entry[1])*int(entry[2])*int(entry[3]))))
    presentes = sorted(presentes, key=ordena)
    saida = str(presentes[0][0])
    for i in range(1, K):
        saida += " "+str(presentes[i][0])
    print(saida)