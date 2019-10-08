for N in range(int(input())):
    n = int(input())
    entry = input().split(" ")
    presenca = input().split(" ")
    saida = ""
    flag = 1
    for i in range(len(presenca)):
        A = 0
        P = 0
        M = 0
        for j in presenca[i]:
            if j == 'A':
                A += 1
            elif j == 'P':
                P += 1
            else:
                M += 1
        if P / (P + A) < 0.75:
            if flag:
                saida += entry[i]
                flag = 0
            else:
                saida += " " + entry[i]
    print(saida)