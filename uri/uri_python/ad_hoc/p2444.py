entry = input().split(' ')
V = int(entry[0])
T = int(entry[1])
entry = input().split(' ')
for i in range(T):
	V += int(entry[i])
	if V < 0:
		V = 0
	elif V > 100:
		V = 100
print(V)