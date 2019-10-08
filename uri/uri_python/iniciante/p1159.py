X = int(input())
while X != 0:
    soma = 0
    if X % 2 != 0:
        X += 1
    for j in range(5):
        soma += X
        X += 2
    print(soma)
    X = int(input())