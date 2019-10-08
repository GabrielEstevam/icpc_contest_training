instancias = int(input())
questoes = ["A", "B", "C", "D", "E"]
while instancias > 0:
    for i in range(instancias):
        entrada = input().split(" ")
        k = 0
        for j in range(len(entrada)):
            if int(entrada[j]) <= 127:
                k += 1
                q = j
        if k != 1:
            print("*")
        else:
            print(questoes[q])
    instancias = int(input())