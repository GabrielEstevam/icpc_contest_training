n1 = int(input())
n2 = int(input())
maior = n2
menor = n1
if n1 > n2:
    maior = n1
    menor = n2
soma = 0
i = menor+1
if i % 2 == 0:
    i += 1
while i < maior:
    soma += i
    i += 2
print(soma)
