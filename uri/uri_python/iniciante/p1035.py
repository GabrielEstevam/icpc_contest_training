entrada = input()
valor = entrada.split(" ")
a = int(valor[0])
b = int(valor[1])
c = int(valor[2])
d = int(valor[3])
if b > c and d > a and (c+d) > (a+b) and c > 0 and d > 0 and a%2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")