N = int(input())
for n in range(N):
	entry = input()
	flag = True
	if len(entry) != 20:
		flag = False
	elif (entry[0] != 'R' or entry[1] != 'A'):
		flag = False
	else:	
		aux = ""
		for i in range(2, 20):
			if entry[i].isdigit():
				aux += entry[i]
			else:
				flag = False
				break	
	if (flag):
		print(int(aux))
	else:
		print("INVALID DATA")
