N = int(input())
while N != 0:
	v = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	M = input().split(' ')
	L = input().split(' ')
	for i in range(N):
		M[i] = int(M[i])
		L[i] = int(L[i])
	mcont = sum(M)
	lcont = sum(L)
	for i in range(N-2):
		if M[i+1] == M[i] and M[i+2] == M[i]:
			mcont += 30
		if L[i+1] == L[i] and L[i+2] == L[i]:
			lcont += 30
		if (M[i+1] == M[i] and M[i+2] == M[i]) or (L[i+1] == L[i] and L[i+2] == L[i]):
			break
	if mcont == lcont:
		print("T")
	elif mcont > lcont:
		print("M")
	else:
		print("L")
	N = int(input())