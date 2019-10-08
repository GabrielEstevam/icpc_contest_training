N = int(input())
while N > 0:
    entry = input().split(' ')
    planeta = entry[0]
    ano = int(entry[1]) - int(entry[2])
    for i in range(1, N):
        entry = input().split(' ')
        if (int(entry[1]) - int(entry[2])) < ano:
            ano = int(entry[1]) - int(entry[2])
            planeta = entry[0]

    print(planeta)

    N = int(input())