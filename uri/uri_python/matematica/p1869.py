lista = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
         'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
         'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
         'U', 'V']

N = int(input())
while N != 0:
    saida = ""
    while N >= 32:
        resto = N % 32
        saida = str(lista[resto]) + saida
        N = int(N/32)
    saida = str(lista[N]) + saida
    print(saida)
    N = int(input())
print(0)