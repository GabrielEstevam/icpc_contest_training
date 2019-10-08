N = int(input())
while N != 0:
    entry = input().split(" ")
    picos = 0
    aux_a = int(entry[N-2])
    aux_b = int(entry[N-1])
    for i in range(N):
        if (aux_b < aux_a and aux_b < int(entry[i])) or (aux_b > aux_a and aux_b > int(entry[i])):
            picos += 1
        aux_a = aux_b
        aux_b = int(entry[i])
    print(picos)
    N = int(input())