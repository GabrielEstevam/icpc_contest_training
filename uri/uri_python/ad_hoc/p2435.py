entry1 = input().split(' ')
entry2 = input().split(' ')
if int(entry1[1])/int(entry1[2]) < int(entry2[1])/int(entry2[2]):
	print(entry1[0])
else:
	print(entry2[0])
