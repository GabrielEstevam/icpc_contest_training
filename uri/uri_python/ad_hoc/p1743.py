entrada1 = input().split(" ")
entrada2 = input().split(" ")

flag = True
for i in range(5):
    if int(entrada1[i]) + int(entrada2[i]) != 1:
        flag = False
        break

if flag:
    print("Y")
else:
    print("N")