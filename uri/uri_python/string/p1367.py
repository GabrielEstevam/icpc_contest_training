N = int(input())
while N != 0:
    lista = []
    flag = []
    for i in range(26):
        lista.append(0)
        flag.append(0)
    for i in range(N):
        entry = input().split(" ")
        if entry[2][0] == 'i':
            lista[ord(entry[0]) - 65] += 20
        else:
            lista[ord(entry[0]) - 65] += int(entry[1])
            flag[ord(entry[0]) - 65] = 1
    questoes = 0
    tempo = 0
    for i in range(len(lista)):
        if flag[i]:
            questoes += 1
            tempo += lista[i]
    print(questoes, tempo)
    N = int(input())