valor = 0
for n in range(int(input())):
    entry = input().split(" ")
    if entry[0] == '1001':
        valor += int(entry[1])*1.5
    elif entry[0] == '1002':
        valor += int(entry[1])*2.5
    elif entry[0] == '1003':
        valor += int(entry[1])*3.5
    elif entry[0] == '1004':
        valor += int(entry[1])*4.5
    else:
        valor += int(entry[1])*5.5
print("{0:.2f}".format(valor))