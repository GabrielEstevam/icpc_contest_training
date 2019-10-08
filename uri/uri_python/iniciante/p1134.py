alcool = 0
gasolina = 0
diesel = 0
while True:
    entry = 0
    while entry  < 1 or entry > 4:
        entry = int(input())
    if entry == 1:
        alcool += 1
    elif entry == 2:
        gasolina += 1
    elif entry == 3:
        diesel += 1
    else:
        break

print("MUITO OBRIGADO")
print("Alcool: "+str(alcool))
print("Gasolina: "+str(gasolina))
print("Diesel: "+str(diesel))