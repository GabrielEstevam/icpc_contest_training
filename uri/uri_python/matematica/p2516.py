while True:
    try:
        entrada = input().split(" ")
        S = int(entrada[0])
        Va = int(entrada[1])
        Vb = int(entrada[2])
        if Va <= Vb:
            print("impossivel")
        else:
            print("%.2f" % round(S/(Va-Vb),2))
    except EOFError:
        break
