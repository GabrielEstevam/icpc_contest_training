entry = input().split("/")
while entry[0] != '*':
    compassos = 0
    for i in entry:
        tempo = 0
        for j in i:
            if j == 'W':
                tempo += 64
            elif j == 'H':
                tempo += 32
            elif j == 'Q':
                tempo += 16
            elif j == 'E':
                tempo += 8
            elif j == 'S':
                tempo += 4
            elif j == 'T':
                tempo += 2
            else:
                tempo += 1
        if tempo == 64:
            compassos += 1
    print(compassos)
    entry = input().split("/")
