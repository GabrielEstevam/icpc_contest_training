C = int(input())
operacao = input()
soma = 0
for i in range(144):
    entry = input()
    if i % 12 == C:
        soma += float(entry)
if operacao == "M":
    soma /= 12
print("{0:.1f}".format(soma))