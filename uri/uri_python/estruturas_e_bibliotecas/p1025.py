entry = input().split(" ")
N = int(entry[0])
Q = int(entry[1])
k = 0
while N != 0 or Q != 0:
    k += 1
    entry = []
    for i in range(N):
        entry.append(int(input()))
    entry.sort()
    print("CASE#", str(k)+":")
    for i in range(Q):
        consulta = int(input())
        flag = True
        for j in range(N):
            if entry[j] == consulta:
                print(consulta, "found at", j+1)
                flag = False
                break
        if flag:
            print(consulta, "not found")
    entry = input().split(" ")
    N = int(entry[0])
    Q = int(entry[1])