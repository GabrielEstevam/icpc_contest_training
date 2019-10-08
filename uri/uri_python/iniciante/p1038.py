valor = input().split(" ")
codigo = int(valor[0])
quantidade = int(valor[1])
preco = [4, 4.5, 5, 2, 1.5]
print("Total: R$ %.2f" % (quantidade*preco[codigo-1]))
