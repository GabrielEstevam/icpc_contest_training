N = int(input())
entry = input().split(' ')
P = int(entry[0])
Q = int(entry[2])
if entry[1] == '+':
	if P+Q > N:
		print('OVERFLOW')
	else:
		print('OK')
else:
	if P*Q > N:
		print('OVERFLOW')
	else:
		print('OK')