N = int(input())
while N != 0:
    for i in range(N):
        entry = int(input())
        if entry % 2 == 0:
            total = entry * 2 - 2
        else:
            total = entry * 2 - 1
        print(total)
    N = int(input())