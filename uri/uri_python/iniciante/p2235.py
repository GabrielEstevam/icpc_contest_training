entry = input().split(' ')
A = int(entry[0])
B = int(entry[1])
C = int(entry[2])
if A == B or A == C or B == C or A+B == C or A+C == B or B+C == A:
	print('S')
else:
	print('N') 