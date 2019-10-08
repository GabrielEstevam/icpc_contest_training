import math
entrada = input().split(" ")
for i in range(len(entrada)):
	entrada[i] = float(entrada[i])
entrada.sort(reverse=True)
if entrada[0] >= entrada[1]+entrada[2]:
	print("NAO FORMA TRIANGULO")
else :
	if math.pow(entrada[0], 2) == math.pow(entrada[1], 2)+math.pow(entrada[2], 2):
		print("TRIANGULO RETANGULO")
	if math.pow(entrada[0], 2) > math.pow(entrada[1], 2)+math.pow(entrada[2], 2):
		print("TRIANGULO OBTUSANGULO")
	if math.pow(entrada[0], 2) < math.pow(entrada[1], 2)+math.pow(entrada[2], 2):
		print("TRIANGULO ACUTANGULO")
	if entrada[0] == entrada[1] == entrada[2]:
		print("TRIANGULO EQUILATERO")
	elif entrada[0] == entrada[1] or entrada[0] == entrada[2] or entrada[1] == entrada[2]:
		print("TRIANGULO ISOSCELES")

