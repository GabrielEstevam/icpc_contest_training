for N in range(int(input())):
    mensagem = ""
    entry = input().split(" ")
    for i in entry:
        if len(i) > 0:
            mensagem += i[0]
    print(mensagem)