for n in range(int(input())):
    entry = input().split("x")
    if int(entry[0]) == int(entry[1]):
        for i in range(5, 11, 1):
            print(int(entry[0]), "x", i, "=", int(entry[0])*i)
    else:
        for i in range(5, 11, 1):
            print(int(entry[0]), "x", i, "=", int(entry[0])*i, "&&", int(entry[1]), "x", i, "=", int(entry[1])*i)