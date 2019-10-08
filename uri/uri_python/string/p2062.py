N = int(input())
entry = input().split(" ")
saida = ""
for i in range(N):
    if i > 0:
        saida += " "
    if len(entry[i]) == 3:
        if entry[i][0] == 'O' and entry[i][1] == 'B':
            saida += "OBI"
        elif entry[i][0] == 'U' and entry[i][1] == 'R':
            saida += "URI"
        else:
            saida += entry[i]
    else:
        saida += entry[i]
print(saida)