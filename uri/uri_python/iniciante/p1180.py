N = int(input())
entry = input().split(" ")
iMin = 0
Min = int(entry[0])
for i in range(N):
    if int(entry[i]) < Min:
        Min = int(entry[i])
        iMin = i
print("Menor valor:", Min)
print("Posicao:", iMin)