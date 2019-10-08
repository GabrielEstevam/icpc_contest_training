for N in range(int(input())):
	dic = {}
	for n in range(int(input())):
		entry = input().split(' ')
		if entry[1] == 'chirrin':
			dic[entry[0]] = 1
		elif entry[1] == 'chirrion':
			dic[entry[0]] = 0
	print("TOTAL")
	for i in sorted(dic):
		if dic[i] == 1:
			print(i)