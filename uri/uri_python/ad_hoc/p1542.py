entrada = input().split(" ")
while len(entrada) > 1:
    A = int(entrada[0])
    B = int(entrada[1])
    C = int(entrada[2])

    D = int(A*B*C/(C-A))
    if D == 1:
        print("1 pagina")
    else:
        print(D,"paginas")
    entrada = input().split(" ")