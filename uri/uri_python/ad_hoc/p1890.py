for n in range(int(input())):
    entry = input().split(' ')
    C = int(entry[0])
    D = int(entry[1])
    if C == 0 and D == 0:
        print(0)
    else:
        print(pow(26, C) * pow(10, D))
