def euclides_MDC(a, b):
    if b == 0:
        return a
    else:
        return euclides_MDC(b, a%b)

k = 0
for n in range(int(input())):
    k += 1
    entry1 = int(input(), 2)
    entry2 = int(input(), 2)
    MDC = euclides_MDC(entry1, entry2)
    if MDC > 1:
        print("Pair #" + str(k) + ": All you need is love!")
    else:
        print("Pair #" + str(k) + ": Love is not all you need!")