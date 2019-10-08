entry = float(input())
if entry < 400.01:
	print('Novo salario: {:.2f}'.format(entry*1.15))
	print('Reajuste ganho: {:.2f}'.format(entry*0.15))
	print("Em percentual: 15 %")
elif entry < 800.01:
	print('Novo salario: {:.2f}'.format(entry*1.12))
	print('Reajuste ganho: {:.2f}'.format(entry*0.12))
	print("Em percentual: 12 %")
elif entry < 1200.01:
	print('Novo salario: {:.2f}'.format(entry*1.1))
	print('Reajuste ganho: {:.2f}'.format(entry*0.1))
	print("Em percentual: 10 %")
elif entry < 2000.01:
	print('Novo salario: {:.2f}'.format(entry*1.07))
	print('Reajuste ganho: {:.2f}'.format(entry*0.07))
	print("Em percentual: 7 %")
else:
	print('Novo salario: {:.2f}'.format(entry*1.04))
	print('Reajuste ganho: {:.2f}'.format(entry*0.04))
	print("Em percentual: 4 %")
