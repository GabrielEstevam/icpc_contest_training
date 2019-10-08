aux = 0
flag = True
while True:
	try:
		entry = int(input())
		if flag:
			if entry <= aux:
				flag = False
			else:
				aux = entry
	except EOFError:
		break
print(aux+1)
