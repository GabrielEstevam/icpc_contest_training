while True:
    try:
        entrada = input().split(" ")
        a = int(entrada[0])
        b = int(entrada[1])
        c = int(entrada[2])
        if a != b and a != c:
            print("A")
        elif b != a and b != c:
            print("B")
        elif c != a and c != b:
            print("C")
        else:
            print("*")
    except EOFError:
        break