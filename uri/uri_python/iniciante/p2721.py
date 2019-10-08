renas = ['Dasher', 'Dancer', 'Prancer', 'Vixen', 'Comet', 'Cupid', 'Donner', 'Blitzen', 'Rudolph']
entry = input().split()
soma = 0
for i in entry:
    soma += int(i)
print(renas[soma%9-1])