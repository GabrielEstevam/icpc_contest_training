import math

def expo(a,b):
    if b < 1:   
        return math.pow(a, b)
    else:
        x = expo(a, b/2)
        return (x*x)%10000

entrada = input().split(" ")
A = int(entrada[0])
B = int(entrada[1])
N = int(entrada[2])
K = int(entrada[3])

X = A + math.sqrt(B)
print("x", X)
X = expo(X, N)
print(X)