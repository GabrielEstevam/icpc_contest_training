N = int(input())
entry = []
for n in range(N):
    entry.append(input().split(" "))
maior = float(entry[0][1])
imaior = 0
for i in range(1, N, 1):
    if float(entry[i][1]) > maior:
        imaior = i
        maior = float(entry[i][1])
if maior >= 8:
    print(entry[imaior][0])
else:
    print("Minimum note not reached")