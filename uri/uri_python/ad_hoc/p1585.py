instancias = int(input())
for i in range(instancias):
    entrada = input().split(" ")
    a = int(entrada[0])
    b = int(entrada[1])
    print("%d cm2" %((a*b)/2))