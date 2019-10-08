import math

while True:
    try:
        entrada = input().split(" ")
        a = int(entrada[0])
        b = int(entrada[1])
        i = 0
        saida = 0
        if a > 0 or b > 0:
            if a >= b:
                i = math.ceil(math.log(a, 2)) + 1
            else:
                i = math.ceil(math.log(b, 2)) + 1
        i = pow(2, i)
        while i > 0:
            if (a >= i or  b >= i) and (a < i or b < i):
                saida += i
            if a >= i:
                a -= i
            if b >= i:
                b -= i
            i /= 2
        print(int(saida))
    except EOFError:
        break