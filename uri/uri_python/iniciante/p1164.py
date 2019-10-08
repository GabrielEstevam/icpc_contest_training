N = int(input())
for i in range(N):
    n = int(input())
    soma = 0
    for j in range(1, n):
        if n % j == 0:
            soma += j
    if soma == n:
        print(n,"eh perfeito")
    else:
        print(n,"nao eh perfeito")