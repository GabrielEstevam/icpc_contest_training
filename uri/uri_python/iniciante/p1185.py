operacao = input()
soma = 0
n = 0
for i in range(12):
    for j in range(12):
        entry = input()
        if j+i < 11:
            soma += float(entry)
            n += 1
if operacao == "M":
    soma /= n
print("{0:.1f}".format(soma))