entry = input()
saida = ""
tam = len(entry)
for i in range(tam):
    saida += entry[tam - i - 1]
print(saida)