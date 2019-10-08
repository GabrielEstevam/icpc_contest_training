aposta = input().split(" ")
sorteio = input().split(" ")
soma = 0
for i in range(6):
    for j in range(6):
        if aposta[i] == sorteio[j]:
            soma += 1
if soma == 6:
    print("sena")
elif soma == 5:
    print("quina")
elif soma == 4:
    print("quadra")
elif soma == 3:
    print("terno")
else:
    print("azar")
