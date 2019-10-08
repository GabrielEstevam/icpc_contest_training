X = int(input())
Z = int(input())
while Z <= X:
    Z = int(input())
soma = 0
i = 0
while soma <= Z:
    soma += X+i
    i += 1
print(i)