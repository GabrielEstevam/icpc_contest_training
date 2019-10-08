instancias = int(input())
while instancias > 0:
    entrada = input().split(" ")
    N = int(entrada[0])
    M = int(entrada[1])
    for i in range(instancias):
        entrada = input().split(" ")
        X = int(entrada[0])
        Y = int(entrada[1])
        if X > N and Y > M:
            print("NE")
        elif X > N and Y < M:
            print("SE")
        elif X < N and Y > M:
            print("NO")
        elif X < N and Y < M:
            print("SO")
        else:
            print("divisa")
    instancias = int(input())