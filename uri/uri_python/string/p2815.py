entry = input().split(' ')
v = []
for i in range(len(entry)):
    aux = ""
    if len(entry[i]) >= 4:
        if entry[i][0] == entry[i][2] and entry[i][1] == entry[i][3]:
            for j in range(2, len(entry[i])):
                aux += entry[i][j]
    if len(aux) == 0:
        v.append(entry[i])
    else:
        v.append(aux)
out = v[0]
for j in range(1, len(v)):
    out += " " + v[j]
print(out)