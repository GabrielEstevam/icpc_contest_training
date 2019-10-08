def euclides_MDC(a, b):
    if b == 0:
        return a
    else:
        return euclides_MDC(b, a%b)

while True:
    try:
        entrada = input().split(" ")
        A = int(entrada[0])
        B = int(entrada[1])
        C = int(entrada[2])

        AB = euclides_MDC(A, B)
        MDC = euclides_MDC(AB, C)

        A = A*A
        B = B*B
        C = C*C

        if A + B == C or A + C == B or B + C == A:
            if MDC == 1:
                print("tripla pitagorica primitiva")
            else:
                print("tripla pitagorica")
        else:
            print("tripla")
    except EOFError:
        break