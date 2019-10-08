import math
N = int(input())
for i in range(N):
    Tn = int(input())
    n = math.floor(math.sqrt(2*Tn + 0.25) - 0.5)
    print(n)