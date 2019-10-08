entry = input().split(' ')
maior = int(entry[0])
for i in range(1, len(entry)):
	if int(entry[i]) > maior:
		maior = int(entry[i])
print(maior)