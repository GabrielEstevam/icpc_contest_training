k = 1
entry = input().split(" ")
a = int(entry[0])
b = int(entry[1])
gremio = 0
inter = 0
empate = 0
if a > b:
    inter += 1
elif b > a:
    gremio += 1
else:
    empate += 1
print("Novo grenal (1-sim 2-nao)")
entry = int(input())
while entry == 1:
    k += 1
    entry = input().split(" ")
    a = int(entry[0])
    b = int(entry[1])
    if a > b:
        inter += 1
    elif b > a:
        gremio += 1
    else:
        empate += 1
    print("Novo grenal (1-sim 2-nao)")
    entry = int(input())
print(str(k)+" grenais")
print("Inter:"+str(inter))
print("Gremio:"+str(gremio))
print("Empates:"+str(empate))
if gremio > inter:
    print("Gremio venceu mais")
elif inter > gremio:
    print("Inter venceu mais")
else:
    print("Nao houve vencedor")