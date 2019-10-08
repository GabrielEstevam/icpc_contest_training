N = int(input())
for i in range(N):
    entry = input().split(" ")
    X = int(entry[0])
    Y = int(entry[1])
    soma = 0
    if X % 2 == 0:
        X += 1
    for j in range(Y):
        soma += X
        X += 2
    print(soma)