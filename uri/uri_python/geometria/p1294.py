import math
while True:
    try:
        entry = input().split(" ")
       	L = float(entry[0])
        W = float(entry[1])
        max_x = (4*(L + W) - math.sqrt(16*(L + W)*(L + W) - 48*L*W))/24
        if (L > W):
        	min_x = W/2
        else:
        	min_x = L/2
        print('{:.3f}'.format(max_x),'{:.3f}'.format(0),'{:.3f}'.format(min_x))
    except EOFError:
        break