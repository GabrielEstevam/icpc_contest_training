aux = ""
for i in range(100000):
    aux =+ 'a'
print(a)
while True:
    try:
        entry = input()
        home = True
        out = ""
        homeT = ""
        for i in entry:
            if i == '[':
                home = False
                out = homeT + out
            elif i == ']':
                home = True
            else:
                if home:
                    out += i
                else:
                    homeT += i
        print(homeT+out)
    except EOFError:
        break