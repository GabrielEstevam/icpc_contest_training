for n in range(int(input())):
	S = input()
	t1 = len(S)
	for i in range(int(input())):
		k = 0
		j = 0
		entry = input()
		t2 = len(entry)
		while j < t2 and k < t1:
			if entry[j] == S[k]:
				j+=1
			k+=1
		if j == t2:
			print("Yes")
		else:
			print("No")