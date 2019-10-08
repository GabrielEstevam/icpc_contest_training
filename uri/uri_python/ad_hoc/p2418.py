entry = input().split(' ')
for i in range(5):
	entry[i] = float(entry[i])
entry.sort()
print("{:.1f}".format(sum(entry)-entry[0]-entry[4]))