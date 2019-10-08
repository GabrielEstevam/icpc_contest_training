def euclides_MDC(a, b):
    if b == 0:
        return a
    else:
        return euclides_MDC(b, a%b)

fibbo = [2, 3]
while True:
    try:
        N = int(input())
        B = pow(2, N)
        while len(fibbo) < N:
            fibbo.append(fibbo[len(fibbo)-1]+fibbo[len(fibbo)-2])
        A = fibbo[N-1]
        MDC = euclides_MDC(A, B)
        A /= MDC
        B /= MDC
        resposta = str(int(A)) + "/" + str(int(B))
        print(resposta)
    except EOFError:
        break