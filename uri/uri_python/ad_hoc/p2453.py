entry = input()
out = ''
flag = 0
for i in entry:
	if i == 'p':
		if flag:
			out += i
			flag = 0
		else:
			flag = 1
	else:
		out += i
		flag = 0
print(out)