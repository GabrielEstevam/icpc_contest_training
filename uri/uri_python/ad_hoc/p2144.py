entry = input().split(" ")
w1 = float(entry[0])
w2 = float(entry[1])
r = float(entry[2])
soma = 0
cont = 0
while w1 != 0 and w2 != 0 and r != 0:
	m = (w1*(1+r/30) + w2*(1+r/30))/2
	if m < 13:
		print('Nao vai da nao')
	elif m < 14:
		print('E 13')
	elif m < 40:
		print('Bora, hora do show! BIIR!')
	elif m <= 60:
		print('Ta saindo da jaula o monstro!')
	else:
		print('AQUI E BODYBUILDER!!')
	soma += m
	cont += 1
	entry = input().split(" ")
	w1 = float(entry[0])
	w2 = float(entry[1])
	r = float(entry[2])

if soma/cont > 40:
	print('')
	print('Aqui nois constroi fibra rapaz! Nao e agua com musculo!')