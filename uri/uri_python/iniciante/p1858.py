N = input()
entry = input().split(" ")
m = min(entry)
for i in range(len(entry)):
    if m == entry[i]:
        print(i+1)
        break
