instancias = int(input())
for i in range(instancias):
    entrada = input()
    N = ""
    for j in range(len(entrada)):
        if entrada[j].isdigit():
            N += entrada[j]
    K = len(entrada) - len(N)
    N = int(N)
    soma = N
    k = 1
    while N > K*k:
        soma *= N-K*k
        k += 1
    print(soma)