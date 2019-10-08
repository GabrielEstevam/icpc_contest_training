romano = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
numero = [1000, 500, 100, 50, 10, 5, 1]
entry = int(input())
saida = []
i = 0
seq = 0
while entry > 0:
    if entry - numero[i] >= 0:
        saida.append(romano[i])
        entry -= numero[i]
        seq += 1
        if seq == 4:
            saida[len(saida) - 3] = romano[i - 1]
            del (saida[len(saida) - 2])
            del (saida[len(saida) - 1])
            if romano[i - 1] == 'D' or romano[i - 1] == 'L' or romano[i - 1] == 'V':
                if len(saida) >= 3:
                    if saida[len(saida)-3] == saida[len(saida)-1]:
                        del(saida[len(saida)-3])
                        saida[len(saida)-1] = romano[i - 2]

            seq == 0
    else:
        i += 1
        seq = 0
imprime = ""
for i in saida:
    imprime += i
print(imprime)