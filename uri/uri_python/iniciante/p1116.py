n = int(input())
for i in range(n):
    entry = input().split(" ")
    if int(entry[1]) == 0:
        print('divisao impossivel')
    else:
        print("{0:.1f}".format(int(entry[0])/int(entry[1])))