entry = input().split(" ")
h = int(entry[0]) + int(entry[1]) + int(entry[2])
while h > 23:
    h -= 24
while h < 0:
    h += 24
print(h)