entry = input().split(' ')
M = int(entry[0])
N = int(entry[1])
dic = {}
for i in range(M):
	entry = input().split(' ')
	dic[entry[0]] = int(entry[1])
for i in range(N):
	entry = input().split(' ')
	soma = 0
	while entry[0] != '.':
		for j in entry:
			if j in dic:
				soma += dic[j]
		entry = input().split(' ')
	print(soma)