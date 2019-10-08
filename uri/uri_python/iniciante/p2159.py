import math
n = int(input())
P = n / math.log(n)
M = P * 1.25506
print('{0:.1f}'.format(P), '{0:.1f}'.format(M))