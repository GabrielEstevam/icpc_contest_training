a = int(input())
b = int(input())
c = int(input())

A = b*2 + c*4
B = a*2 + c*2
C = a*4 + b*2

if A <= B and A <= C:
    print(A)
elif B <= A and B <= C:
    print(B)
else:
    print(C)