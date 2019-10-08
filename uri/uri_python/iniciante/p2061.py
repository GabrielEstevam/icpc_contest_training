entry = input().split(" ")
N = int(entry[0])
M = int(entry[1])
fechou = 0
clicou = 0
for i in range(M):
    entry = input()
    if entry[0] == 'f':
        fechou += 1
    else:
        clicou += 1
print(N + fechou - clicou)