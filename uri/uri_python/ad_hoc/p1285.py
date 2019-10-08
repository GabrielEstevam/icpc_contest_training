rep = [0]
for i in range(1, 5001):
    t = len(str(i))
    string = set(str(i))
    if (len(string) < t):
        rep.append(rep[i-1] + 1)
    else:
        rep.append(rep[i-1])

# print(rep)
while True:
    try:
        entry = input().split(' ')
        N = int(entry[0])-1
        M = int(entry[1])
        print(M-N-rep[M]+rep[N])
    except EOFError:
        break