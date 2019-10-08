while True:
	try:
		n = int(input())
		entry = input().split(' ')
		k = 0
		flag = -1
		for i in range(n):
			if int(entry[i]) == k:
				flag = i+1
				break
		if flag > -1:
			print(flag)
		else:
			print("nao achei")
	except EOFError:
		break