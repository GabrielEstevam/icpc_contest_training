instancias = int(input())
for i in range(instancias):
    e1 = int(input())
    e2 = input().split(" ")
    e3 = int(input())
    lista = [e1, e3]
    for j in range(4):
        lista.append(int(e2[j]))
    flag = 0
    for j in range(6):
        for k in range(6):
            if lista[k] == (j+1):
                flag += 1
                break
    if e1+e3 == 7 and int(e2[0])+int(e2[2]) == 7 and int(e2[1])+int(e2[3]) and flag == 6:
        print("SIM")
    else:
        print("NAO")