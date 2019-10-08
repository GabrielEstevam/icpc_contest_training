N = int(input())
while N != 0:
    entry = input().split(' ')
    cont = 0
    for i in range(N-1, -1, -1):
        cont += (cont + int(entry[i]))
    print(cont) 
    N = int(input())