n = int(input())
coelhos = 0
ratos = 0
sapos = 0
for i in range(n):
    entry = input().split(" ")
    if entry[1] == 'C':
        coelhos += int(entry[0])
    elif entry[1] == 'R':
        ratos += int(entry[0])
    elif entry[1] == 'S':
        sapos += int(entry[0])
cobaias = coelhos+ratos+sapos
print("Total: "+str(cobaias)+" cobaias")
print("Total de coelhos: "+str(coelhos))
print("Total de ratos: "+str(ratos))
print("Total de sapos: "+str(sapos))
print("Percentual de coelhos: "+"{0:.2f}".format(round(100*coelhos/cobaias,2))+" %")
print("Percentual de ratos: "+"{0:.2f}".format(round(100*ratos/cobaias,2))+" %")
print("Percentual de sapos: "+"{0:.2f}".format(round(100*sapos/cobaias,2))+" %")
