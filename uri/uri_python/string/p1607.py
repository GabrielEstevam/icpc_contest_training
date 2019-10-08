for T in range(int(input())):
    entry = input().split(" ")
    A = entry[0]
    B = entry[1]
    soma = 0
    for i in range(len(A)):
        soma += ord(B[i]) - ord(A[i])
        if ord(B[i]) - ord(A[i]) < 0:
            soma += 26
    print(soma)