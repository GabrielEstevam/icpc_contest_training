dic = {}
last = 0
while True:
	try:
		entry = input().split(' ')
		if len(entry) == 3:
			last = int(entry[2])
			dic[entry[0]] = last
		else:
			last = 0
			if entry[2] in dic:
				last += dic[entry[2]]
			else:
				last += int(entry[2])
			if entry[4] in dic:
				last += dic[entry[4]]
			else:
				last += int(entry[4])
			dic[entry[0]] = last
	except EOFError:
		break
print(last)