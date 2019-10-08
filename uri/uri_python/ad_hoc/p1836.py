import math
for t in range(int(input())):
    entry = input().split(' ')
    nome = entry[0]
    L = int(entry[1])
    at = ["HP", "AT", "DF", "SP"]
    print("Caso #"+str(t+1)+":", nome, "nivel", L)
    for i in range(4):
        entry = input().split(' ')
        B = int(entry[0])
        IV = int(entry[1])
        EV = int(entry[2])
        if i == 0:
            AT = ((IV + B + math.sqrt(EV)/8 + 50)*L)/50 + 10
        else:
            AT = ((IV + B + math.sqrt(EV)/8)*L)/50 + 5
        print(at[i]+str(":"), math.floor(AT))