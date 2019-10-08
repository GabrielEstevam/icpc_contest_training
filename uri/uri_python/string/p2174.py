N = int(input())
lista = []
for n in range(N):
    lista.append(input())
lista = list(set(lista))
print("Falta(m)", 151-len(lista), "pomekon(s).")