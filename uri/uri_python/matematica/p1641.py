import math
k = 0
entry = input().split(' ')
while len(entry) > 1:
	R = int(entry[0])
	W = int(entry[1])
	L = int(entry[2])
	k += 1
	if R >= math.sqrt(W*W+L*L)/2:
		print("Pizza", k, "fits on the table.")
	else:
		print("Pizza", k, "does not fit on the table.")
	entry = input().split(' ')