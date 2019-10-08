N = int(input())
entry = input().split(' ')
A = []
for i in range(N):
	A.append(int(entry[i]))
Hl = [0]
if A[0] > 0:
	Hl[0] = 1
Hr = [0]
if A[N-1] > 0:
	Hr[0] = 1
for i in range(1, N):
	Hl.append(min([Hl[i-1]+1, A[i]]))
 
for i in range(1, N):
	Hr.append(min([Hr[i-1]+1, A[N-i-1]]))

maior = 0
for i in range(N):
	if min([Hl[i], Hr[N-i-1]]) > maior:
		maior = min([Hl[i], Hr[N-i-1]])
print(maior)

