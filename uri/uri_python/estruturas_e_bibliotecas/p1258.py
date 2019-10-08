N = int(input())
while (N != 0):
    v = []
    for i in range(N):
        entry1 = input().split(' ')
        entry2 = input().split(' ')
        entry = []
        entry.append(entry2[0])
        if entry2[1] == 'P':
            entry.append(0)
        elif entry2[1] == 'M':
            entry.append(1)
        else:
            entry.append(2)
        entry.append(entry2[1])
        for j in range(len(entry1)):
            entry.append(entry1[j])
        v.append(entry)
    v.sort()
    for i in range(N):
        out = v[i][0] + ' ' + v[i][2]
        for j in range(3, len(v[i])):
            out += ' ' + v[i][j]
        print(out) 
    N = int(input())
    if N != 0:
        print()