entry = input().split(" ")
A = int(entry[0])
B = int(entry[1])
while A != 0 and B != 0:
    a = set(input().split(' '))
    b = set(input().split(' '))
    c = a.union(b)

    if (len(c) - len(a) < len(c) - len(b)):
        print(len(c) - len(a))
    else:
        print(len(c) - len(b))

    entry = input().split(" ")
    A = int(entry[0])
    B = int(entry[1])