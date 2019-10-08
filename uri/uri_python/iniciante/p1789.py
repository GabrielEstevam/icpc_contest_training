import math
while True:
    try:
        N = int(input())
        entry = input().split(" ")
        for i in range(N):
            entry[i] = int(entry[i])
        maior = max(entry)
        print(math.floor(maior/10)+1)
    except EOFError:
        break