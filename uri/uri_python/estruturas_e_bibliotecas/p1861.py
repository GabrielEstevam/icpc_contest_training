dic = {}
while True:
	try:
		entry = input().split(' ')
		if entry[0] not in dic:
			dic[entry[0]] = 1
		else:
			if dic[entry[0]] != -1:
				dic[entry[0]] += 1
		dic[entry[1]] = -1
	except EOFError:
		break
print("HALL OF MURDERERS")
for i in sorted(dic):
	if dic[i] > 0:
		print(i, dic[i])