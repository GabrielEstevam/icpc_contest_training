entry = input().split(' ')
N = int(entry[0])
C = int(entry[1])
flag = True
k = 0
for i in range(N):
	entry = input().split(' ')
	k -= int(entry[0])
	k += int(entry[1])
	if k > C:
		flag = False
		
if flag:
	print('N')
else:
	print('S')