N = int(input())
entrada1 = input().split(" ")
LA = int(entrada1[0])
LB = int(entrada1[1])
entrada2 = input().split(" ")
SA = int(entrada2[0])
SB = int(entrada2[1])

if N >= LA and N <= LB and N >= SA and N <= SB:
    print("possivel")
else:
    print("impossivel")