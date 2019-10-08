entry = int(input())
soma = 0
if entry > 100:
	soma += (entry - 100)*5
	entry = 100
if entry > 30:
	soma += (entry - 30)*2
	entry = 30
if entry > 10:
	soma += (entry - 10)
soma += 7
print(soma)