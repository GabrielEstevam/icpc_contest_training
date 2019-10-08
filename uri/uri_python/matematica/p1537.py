entry = int(input())
while entry > 0:
    r = 1
    for i in range(4, entry+1):
        r = (r*i) % 1000000009
    print(r)
    entry = int(input())