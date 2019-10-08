fat = [1, 1]
for i in range(2, 10001):
	fat.append((fat[i-1]*i)%1000000007)
while True:
	try:
		entry = input()
		dic = {}
		for i in entry:
			if i in dic:
				dic[i] += 1
			else:
				dic[i] = 1
		print(dic)
		den = 1
		for i in dic:
			den = (den*fat[dic[i]]) % 1000000007
		print("d:", den)
		print("n:", fat[len(entry)])
		print(int(fat[len(entry)]/den))
	except EOFError:
		break