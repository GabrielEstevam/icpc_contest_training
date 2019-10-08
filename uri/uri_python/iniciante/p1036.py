entrada = input()
valor = entrada.split(" ")
a = float(valor[0])
b = float(valor[1])
c = float(valor[2])
delta = pow(b, 2) - 4*a*c
if a == 0 or delta < 0:
    print("Impossivel calcular")
else:
    R1 = (-1*b+pow(delta, 0.5))/(2*a)
    print("R1 = %.5f" % R1)
    R2 = (-1*b-pow(delta, 0.5))/(2*a)
    print("R2 = %.5f" % R2)
