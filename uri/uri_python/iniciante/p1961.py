entry = input().split(" ")
P = int(entry[0])
N = int(entry[1])
entry = input().split(" ")
if entry[len(entry) - 1] == '':
    del(entry[len(entry) - 1])
for i in range(len(entry)):
    entry[i] = int(entry[i])
for i in range(0, len(entry) - 1, 1):
    if entry[i] - P > entry[i + 1] or entry[i] + P < entry[i + 1]:
        print("GAME OVER")
        exit()
print("YOU WIN")
