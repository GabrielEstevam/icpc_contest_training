import math
n = int(input())
while n != 0:
    corridas = 0
    while n > 1:
        n = math.ceil(n / 3)
        corridas += n
    print(corridas)
    n = int(input())