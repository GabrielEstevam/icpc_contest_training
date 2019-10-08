while True:
    try:
        entrada = input().split(" ")
        A = int(entrada[0])
        B = int(entrada[1])

        print(int(2*B*A))

    except EOFError:
        break