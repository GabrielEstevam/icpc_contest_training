entrada = input().split(" ")
while entrada[0] != "0" or entrada[1] != "0":
    while len(entrada[0]) > 1:
        sum1 = 0
        for i in entrada[0]:
            sum1 += int(i)
        entrada[0] = str(sum1)
    while len(entrada[1]) > 1:
        sum2 = 0
        for i in entrada[1]:
            sum2 += int(i)
        entrada[1] = str(sum2)
    if int(entrada[0]) > int(entrada[1]):
        print(1)
    elif int(entrada[0]) < int(entrada[1]):
        print(2)
    else:
        print(0)
    entrada = input().split(" ")
