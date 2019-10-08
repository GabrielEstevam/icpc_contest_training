import math

while True:
    try:
        entrada = input().split(" ")
        A = int(entrada[0])
        B = int(entrada[1])

        print(int(math.fabs(A-B)))

    except EOFError:
        break