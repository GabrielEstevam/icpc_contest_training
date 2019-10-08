N = 1000000
fat = [1]
mod = 1000000000
for i in range(1, N + 1):
	fat.append(fat[i-1]*i % mod)
	while fat[i] % 10 == 0:
		fat[i] = int(fat[i]/10)
#for i in range(N):
#	print('i, f: ', i, fat[i])
k = 1
while (True):
	try:
		n = int(input())
		print("Instancia", k)
		print(fat[n] % 10)
		print("")
		k += 1
	except EOFError:
		break

