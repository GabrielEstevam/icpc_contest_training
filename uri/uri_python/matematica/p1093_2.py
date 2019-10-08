import math
entry = input().split(' ')
AT = float(entry[2])
while AT != 0:
    D = int(entry[3])
    EV1 = math.ceil(int(entry[0])/D)
    EV2 = math.ceil(int(entry[1])/D)
    if AT == 3:
        P = EV1/(EV1+EV2)
    else:
        P = 1 - (1-pow(AT/(6-AT), EV2))/(1-pow(AT/(6-AT), EV1+EV2))
    print("{:.1f}".format(P*100))
    entry = input().split(' ')
    AT = float(entry[2])