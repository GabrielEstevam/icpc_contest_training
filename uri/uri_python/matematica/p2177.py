entry = input().split(' ')
xi = int(entry[0])
yi = int(entry[1])
out = ""
for i in range(int(entry[2])):
	entry = input().split(' ')
	x = int(entry[0])
	y = int(entry[1])
	t = int(entry[2])
	if (x-xi)*(x-xi) + (y-yi)*(y-yi) < t*t:
		if len(out) == 0:
			out = str(i+1)
		else:
			out += " " + str(i+1)
if len(out) == 0:
	print(-1)
else:
	print(out)
