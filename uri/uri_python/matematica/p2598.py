import math
instancias = int(input())
for i in range(instancias):
    entrada = input().split(" ")
    print(math.ceil(int(entrada[0])/int(entrada[1])))