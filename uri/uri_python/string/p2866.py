for n in range(int(input())):
    entry = input()
    out = ""
    for i in range(len(entry)-1, -1, -1):
        if entry[i].islower():
            out += entry[i]
    print(out)