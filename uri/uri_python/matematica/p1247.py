import math

while True:
    try:
        entrada = input().split(" ")
        D = int(entrada[0])
        VF = int(entrada[1])
        VG = int(entrada[2])

        hip = math.hypot(12, D)

        if hip/VG <= 12/VF:
            print("S")
        else:
            print("N")

    except EOFError:
        break