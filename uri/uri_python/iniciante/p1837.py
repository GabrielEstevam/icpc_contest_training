entry = input().split(" ")
a = int(entry[0])
b = int(entry[1])
r = a%b
if r < 0:
    r += abs(b)
q = (a-r)/b
print(int(q), r)