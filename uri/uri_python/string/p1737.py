N = int(input())
while N != 0:
    entry = ""
    for n in range(N):
        entry += input()
    dic = {}
    for i in range(len(entry)-1):
        if str(entry[i])+str(entry[i+1]) in dic:
            dic[str(entry[i])+str(entry[i+1])] += 1
        else:
            dic[str(entry[i])+str(entry[i+1])] = 1
    v = []
    for i in dic:
        v.append([-1*dic[i], i])
    v.sort()
    for i in range(5):
        print(v[i][1], v[i][0]*-1, "{:.6f}".format(v[i][0]*-1/(len(entry)-1)))
    print("")
    N = int(input())