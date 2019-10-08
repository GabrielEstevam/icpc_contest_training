N = int(input())
fat = [1]
i = 2
while fat[len(fat) - 1] < N:
	fat.append(fat[len(fat) - 1] * i)
	i += 1
cont = 0
k = len(fat) - 1
while N > 0:
	while N >= fat[k]:
		cont += 1
		N -= fat[k]
	k -= 1
print(cont)
