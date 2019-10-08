x = int(input())
y = int(input())
soma = 0
menor = x
maior = y
if y < x:
    menor = y
    maior = x
for i in range(menor, maior+1):
    if i % 13 != 0:
        soma += i
print(soma)