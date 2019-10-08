valor = 0
peso = 0
N = int(input())
for i in range(N):
    valor += float(input())
    entry = input().split()
    peso += len(entry)
    print("day "+str(i+1)+": "+str(len(entry))+" kg")
print("{0:.2f}".format(peso/N), "kg by day")
print("R$", "{0:.2f}".format(valor/N), "by day")