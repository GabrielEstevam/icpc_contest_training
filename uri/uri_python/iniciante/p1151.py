N = int(input())
a = 0
b = 1
saida = ""
if N > 0:
    saida = str(a)
for i in range(1, N):
    saida += " "+str(b)
    aux = a+b
    a = b
    b = aux
print(saida)