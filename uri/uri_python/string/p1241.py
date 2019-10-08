instancias = int(input())
for i in range(instancias):
    entrada = input().split(" ")
    A = entrada[0]
    B = entrada[1]

    if len(A) >= len(B):
        flag = True
        for j in range(len(B)):
            if A[len(A)-j-1] != B[len(B)-j-1]:
                flag = False
                break
        if flag:
            print("encaixa")
        else:
            print("nao encaixa")
    else:
        print("nao encaixa")