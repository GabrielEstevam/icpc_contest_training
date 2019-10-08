N = int(input())
entry = input().split(" ")
pico = False
flag = True
if int(entry[0]) > int(entry[1]):
    pico = True
for i in range(1, N, 1):
    if pico:
        if int(entry[i]) >= int(entry[i-1]):
            flag = False
            break
        pico = False
    else:
        if int(entry[i]) <= int(entry[i-1]):
            flag = False
            break
        pico = True
if flag:
    print('1')
else:
    print('0')