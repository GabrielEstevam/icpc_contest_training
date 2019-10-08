iMaior = 1
maior = 0
for i in range(100):
    entry = int(input())
    if entry > maior:
        iMaior = i+1
        maior = entry
print(maior)
print(iMaior)