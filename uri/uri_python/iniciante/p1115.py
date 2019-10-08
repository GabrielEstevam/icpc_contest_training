entry = input().split(" ")
x = int(entry[0])
y = int(entry[1])
while x != 0 and y != 0:
    if x > 0:
        if y > 0:
            print('primeiro')
        else:
            print('quarto')
    else:
        if y > 0:
            print('segundo')
        else:
            print('terceiro')
    entry = input().split(" ")
    x = int(entry[0])
    y = int(entry[1])