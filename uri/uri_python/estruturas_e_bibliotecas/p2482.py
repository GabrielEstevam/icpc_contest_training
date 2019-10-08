lingua = []
saudacao = []
for N in range(int(input())):
    lingua.append(input())
    saudacao.append(input())
for M in range(int(input())):
    nome = input()
    tongue = input()
    print(nome)
    for i in range(len(lingua)):
        if tongue == lingua[i]:
            print(saudacao[i])
            break
    print("")