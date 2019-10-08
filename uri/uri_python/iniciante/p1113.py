entry = input().split(" ")
a = int(entry[0])
b = int(entry[1])
while a != b:
    if a < b:
        print('Crescente')
    else:
        print('Decrescente')
    entry = input().split(" ")
    a = int(entry[0])
    b = int(entry[1])