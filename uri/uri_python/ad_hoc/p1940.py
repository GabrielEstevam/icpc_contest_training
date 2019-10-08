entry = input().split(' ')
J = int(entry[0])
R = int(entry[1])
pontos = []
for i in range(J):
	pontos.append(0)
entry = input().split(' ')
for i in range(R):	
	for j in range(J):
		pontos[j] += int(entry[J*i + j])
imax = 0
for i in range(1, J):
	if pontos[i] >= pontos[imax]:
		imax = i
print(imax + 1)