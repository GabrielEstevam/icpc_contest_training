entry = input().split(' ')
L = int(entry[0])
N = int(entry[1])
irr = {}
for i in range(L):
	entry = input().split(' ')
	irr[entry[0]] = entry[1]
v = []
for i in range(N):
	v.append(input())
	if v[i] in irr:
		v[i] = irr[v[i]]
	elif v[i][len(v[i])-2] != 'a' and v[i][len(v[i])-2] != 'e' and v[i][len(v[i])-2] != 'i' and v[i][len(v[i])-2] != 'o' and v[i][len(v[i])-2] != 'u' and v[i][len(v[i])-1] == 'y':
		aux = ""
		for j in range(len(v[i])-1):
			aux += v[i][j]
		aux += "ies"
		v[i] = aux
	elif v[i][len(v[i])-1] == 'o' or v[i][len(v[i])-1] == 's' or (v[i][len(v[i])-2] == 'c' and v[i][len(v[i])-1] == 'h') or (v[i][len(v[i])-2] == 's' and v[i][len(v[i])-1] == 'h') or v[i][len(v[i])-1] == 'x':
		aux = ""
		for j in range(len(v[i])):
			aux += v[i][j]
		aux += "es"
		v[i] = aux
	else:
		aux = ""
		for j in range(len(v[i])):
			aux += v[i][j]
		aux += "s"
		v[i] = aux
for i in range(N):
	print(v[i])