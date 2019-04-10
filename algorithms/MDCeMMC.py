''' (MAT) MDC e MMC '''

def euclides_MDC(a, b):
    if b == 0:
        return a
    else:
        return euclides_MDC(b, a%b)

def MMC(a, b):
    return int((a*b)/euclides_MDC(a, b))

while True:
    try:
        M = int(input())
        entrada = input().split(" ")
        mmc = MMC(int(entrada[0]), int(entrada[1]))
        mmc = MMC(mmc, int(entrada[2]))
        print(mmc - M)
    except EOFError:
        break