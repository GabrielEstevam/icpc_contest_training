import math
entry = input().split(" ")
R = int(entry[0])
N = int(entry[1])
k = 0
while R != 0 or N != 0:
    k += 1
    if R / N <= 27:
        print("Case", str(k) + ':', math.ceil(R / N) - 1)
    else:
        print("Case", str(k) + ': impossible')
    entry = input().split(" ")
    R = int(entry[0])
    N = int(entry[1])