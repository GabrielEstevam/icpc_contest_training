n = int(input())
d = 6
for i in range(n - 1):
    d = 1/d + 6
if n == 0:
    print('{0:.10f}'.format(3))
else:
    print('{0:.10f}'.format(3 + 1/d))