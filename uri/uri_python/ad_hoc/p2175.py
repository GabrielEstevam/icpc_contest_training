entrada = input().split(" ")
O = float(entrada[0])
B = float(entrada[1])
I = float(entrada[2])
if O < B and O < I:
    print("Otavio")
elif B < O and B < I:
    print("Bruno")
elif I < O and I < B:
    print("Ian")
else:
    print("Empate")