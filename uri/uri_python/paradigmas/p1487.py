entry = input().split(' ')
N = int(entry[0])
T = int(entry[1])
k = 1
while N != 0:
    brinq = []
    for i in range(N):
        entry = input().split(' ')
        brinq.append([int(entry[0]), int(entry[1])])
    result = []
    for i in range(T+1):
        result.append(0)
        for j in range(N):
            if brinq[j][0] < i:
                if brinq[j][1] + result[i-brinq[j][0]] > result[i]:
                    result[i] = brinq[j][1] + result[i-brinq[j][0]]
            elif brinq[j][0] == i:
                if brinq[j][1] > result[i]:
                    result[i] = brinq[j][1]

    print('Instancia', k)
    k += 1
    print(result[T])
    print('')

    entry = input().split(' ')
    N = int(entry[0])
    T = int(entry[1])