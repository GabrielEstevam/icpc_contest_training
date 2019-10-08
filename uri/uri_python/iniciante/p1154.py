n = int(input())
soma = 0
i = 0
while n >= 0:
    i += 1
    soma += n
    n = int(input())
if i > 0:
    print("{0:.2f}".format(soma/i))
else:
    print(0)