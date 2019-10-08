fat = [1, 1, 2]
for i in range(3, 16):
	fat.append(i*fat[i-1])

N = input().split(' ')
flag = False
while True:
	for i in range(len(N)):
		if N[i] == "0":
			flag = True
			break
		k = 0
		for j in range(len(N[i])):
			if ord(N[i][j]) >= 65 and ord(N[i][j]) <= 90 or ord(N[i][j]) >= 97 and ord(N[i][j]) <= 122:
				k += 1
		if k > 0:
			print(fat[k])
	if flag:
		break
	N = input().split(' ')