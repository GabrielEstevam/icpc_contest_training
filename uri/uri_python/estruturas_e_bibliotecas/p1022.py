def euclides_MDC(a, b):
    if b == 0:
        return a
    else:
        return euclides_MDC(b, a%b)

N = int(input())
for i in range(N):
    entry = input().split(" ")
    N1 = int(entry[0])
    D1 = int(entry[2])
    N2 = int(entry[4])
    D2 = int(entry[6])
    N = 0
    D = 0
    if entry[3] == '+':
        N = N1*D2+N2*D1
        D = D1*D2
    elif entry[3] == '-':
        N = N1*D2-N2*D1
        D = D1*D2
    elif entry[3] == '*':
        N = N1*N2
        D = D1*D2
    else:
        N = N1*D2
        D = N2*D1
    mdc = euclides_MDC(N, D)
    N_simp = N/mdc
    D_simp = D/mdc
    print(str(N)+"/"+str(D)+" = "+str(int(N_simp))+"/"+str(int(D_simp)))