n = int(input())
for i in range(n):
    entry = input().split(" ")
    soma = float(entry[0]) * 2
    soma += float(entry[1]) * 3
    soma += float(entry[2]) * 5
    soma /= 10
    print(round(soma, 1))