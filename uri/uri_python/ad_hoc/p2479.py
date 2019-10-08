Lista = []
comportadas = 0
descomportadas = 0
for N in range(int(input())):
    entry = input().split(" ")
    Lista.append(entry[1])
    if entry[0] == '+':
        comportadas += 1
    else:
        descomportadas += 1
Lista.sort()
for i in Lista:
    print(i)
print("Se comportaram:", comportadas, "| Nao se comportaram:", descomportadas)