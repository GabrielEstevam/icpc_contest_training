entry = input().split(" ")
A = int(entry[0])
i = 1
while int(entry[i]) <= 0:
    i += 1
N = int(entry[i])
soma = 0
for i in range(N):
    soma += A+i
print(soma)