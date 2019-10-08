entry = input().split(" ")
a = int(entry[0])
b = int(entry[1])
while a > 0 and b > 0:
    menor = a
    maior = b
    if a > b:
        menor = b
        maior = a
    saida = ""
    soma = 0
    for i in range(menor, maior+1):
        saida += str(i)+" "
        soma += i
    saida += "Sum="+str(soma)
    print(saida)
    entry = input().split(" ")
    a = int(entry[0])
    b = int(entry[1])