entry = input().split(" ")
N = int(entry[0])
M = int(entry[1])
possibilidades = [4, 7, 10 ,12, 15, 20, 22, 25, 30, 40, 52, 55, 60, 70, 100, 102, 105, 110, 120, 150, 200]
while N != 0 or M != 0:
    troco = M - N
    flag = True
    for i in possibilidades:
        if troco == i:
            print("possible")
            flag = False
            break
    if flag:
        print("impossible")
    entry = input().split(" ")
    N = int(entry[0])
    M = int(entry[1])