entry = input().split(" ")
a = int(entry[0])
b = int(entry[1])
c = int(entry[2])
if a == b:
    if c > b:
        print(":)")
    else:
        print(":(")
elif b < a:
    if c >= b or c-b > b-a:
        print(":)")
    else:
        print(":(")
else:
    if c <= b or c-b < b-a:
        print(":(")
    else:
        print(":)")
