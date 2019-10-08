for n in range(int(input())):
    entry = input().split(' ')
    N = int(entry[0])
    M = int(entry[1])
    entry = input().split(' ')
    r = []
    for i in range(M):
        r.append(int(entry[i]))
    P = [0]
    for i in range(1, N):
        P.append(0)
        for j in range(M):
            if r[j] <= i:
                P[i] += P[i-r[j]] + 1

    #print(P)
    print(P[N-1] + M)
