import math
def expo(a, b, tam):
    if b == 1:
        return int(math.pow(a, b)%tam)
    else:
        A = expo(a, math.floor(b/2), tam)
        A *= A
        if b % 2 != 0:
            A *= a
        return int(A % tam)

while True:
    try:
        N = input()
        tam = len(N)
        N = int(N)
        tam = math.pow(10, tam)
        A = expo(N, N, tam)
        if A == N:
            print("SIM")
        else:
            print("NAO")

    except EOFError:
        break