#coding: utf-8

valor = float(input())
cedula = [100, 50, 20, 10, 5, 2]
moeda = [1, 0.5, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for i in range(6):
    k = valor / cedula[i]
    valor %= cedula[i]
    print("%d nota(s) de R$ %.d.00" % (k, cedula[i]))

print("MOEDAS:")
k = valor / moeda[0]
print("%d moeda(s) de R$ 1.00" % k)
valor %= moeda[0]
k = valor / moeda[1]
print("%d moeda(s) de R$ 0.50" % k)
valor %= moeda[1]
k = valor / moeda[2]
print("%d moeda(s) de R$ 0.25" % k)
valor %= moeda[2]
k = valor / moeda[3]
print("%d moeda(s) de R$ 0.10" % k)
valor %= moeda[3]
k = valor / moeda[4]
print("%d moeda(s) de R$ 0.05" % k)
valor %= moeda[4]
k = valor / moeda[5]
print("%d moeda(s) de R$ 0.01\n" % k)
valor %= moeda[5]


'''
for i in range(6):
    k = valor / moeda[i]
    valor %= moeda[i]
    print("%d moeda(s) de R$ %1.2f" % (k, moeda[i]))
'''
