N = 32700
num = []
for i in range(N):
	num.append(1)
i = 2
while True:
	k = i * 2
	while k < N:
		num[k] = 0
		k += i

	i += 1
	while i < N:
		if num[i]:
			break
		i += 1
	
	if i == N:
		break

primes = []
for i in range(1, N):
	if num[i]:
		primes.append(i)

N = int(input())
while N != 0:
	flag = []
	for i in range(1, N+1):
		flag.append(i)
	
	j = 0
	for i in range(N-1):
		k = primes[i + 1]
		j += (k - 1) 
		#if j >= N-i:
		j = j % (N-i)
		flag.remove(flag[j])
		

	print(flag[0])

	N = int(input())
