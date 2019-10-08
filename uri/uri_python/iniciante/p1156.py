s = 1
a = 2
for i in range(3, 39, 2):
    s += i/a
    a *= 2
print("{0:.2f}".format(s))