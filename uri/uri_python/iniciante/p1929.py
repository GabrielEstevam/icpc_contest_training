entry = input().split(" ")
for i in range(4):
    entry[i] = int(entry[i])
entry.sort()
if entry[0] + entry [1] > entry[2] or entry[1] + entry[2] > entry[3]:
    print('S')
else:
    print('N')