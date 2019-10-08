L = int(input())
operacao = input()
for i in range(12*L):
    input()
soma = 0
for i in range(12):
    soma += int(input())
for i in range(12*(12-L-1)):
    input()
if operacao == "M":
    soma /= 12
print("{0:.1f}".format(soma))