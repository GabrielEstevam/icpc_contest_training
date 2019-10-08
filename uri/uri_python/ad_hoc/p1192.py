instancias = int(input())
for i in range(instancias):
    entrada = input()
    A = int(entrada[0])
    B = int(entrada[2])
    if A == B:
        print(A*B)
    elif entrada[1].islower():
        print(A+B)
    else:
        print(B-A)