N = int(input())
entry = input().split(' ')
dic = {}
for i in range(N):
	if entry[i] in dic:
		dic[entry[i]] += 1
	else:
		dic[entry[i]] = 1
m = 0
for i in range(1, N):
	if dic[entry[i]] > dic[entry[m]] or (dic[entry[i]] == dic[entry[m]] and int(entry[i]) > int(entry[m])):
		m = i
print(entry[m])