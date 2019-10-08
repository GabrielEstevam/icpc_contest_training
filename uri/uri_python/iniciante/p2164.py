import math
n = int(input())
m1 = pow((1 + math.sqrt(5))/ 2, n)
m2 = pow((1 - math.sqrt(5))/ 2, n)
fib = (m1 - m2) / math.sqrt(5)
print('{0:.1f}'.format(fib))