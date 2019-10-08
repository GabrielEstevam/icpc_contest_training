while True:
    try:
        N = input()
        tam = len(N)
        N = int(N)
        mult = ""
        for i in range(tam):
            mult += "1"

        while int(mult) % N != 0:
            mult += "1"
        print(len(mult))

    except EOFError:
        break
