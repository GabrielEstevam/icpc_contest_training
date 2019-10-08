import math
def expo(N):
    if N <= 1:
        return int(math.pow(7, N) % 10)
    else:
        A = expo(math.floor(N/2))
        A *= A
        if N % 2 != 0:
            A *= 7
        return int(A % 10)

instancias = int(input())
for i in range(instancias):
    print(expo(int(input())))