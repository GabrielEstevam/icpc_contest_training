import math
entry = input().split(" ")
while int(entry[0]) != 0:
    print(math.floor(math.sqrt(int(entry[0])*int(entry[1])/(int(entry[2])/100))))
    entry = input().split(" ")