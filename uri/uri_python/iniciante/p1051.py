entry = float(input())
imposto = 0
if entry <= 2000:
    print("Isento")
else:
    if entry > 4500:
        imposto += (entry-4500)*0.28
        entry = 4500
    if entry >  3000:
        imposto += (entry-3000)*0.18
        entry = 3000
    if entry > 2000:
        imposto += (entry-2000)*0.08
    print('R$ {0:.2f}'.format(imposto))