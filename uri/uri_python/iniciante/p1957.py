h = hex(int(input()))
saida = ""
for i in range(2, len(h), 1):
    saida += h[i]
print(saida.upper())