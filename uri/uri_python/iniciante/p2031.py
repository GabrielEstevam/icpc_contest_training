for n in range(int(input())):
    entry1 = input()
    entry2 = input()
    if entry1[1] == 't' and entry2[1] == 'e':
        print("Jogador 1 venceu")
    elif entry1[1] == 'e' and entry2[1] == 't':
        print("Jogador 2 venceu")
    elif entry1[1] == 'e' and entry2[1] == 'a':
        print("Jogador 1 venceu")
    elif entry1[1] == 'a' and entry2[1] == 'e':
        print("Jogador 2 venceu")
    elif entry1[1] == 'a' and entry2[1] == 't':
        print("Jogador 2 venceu")
    elif entry1[1] == 't' and entry2[1] == 'a':
        print("Jogador 1 venceu")
    elif entry1[1] == 'a' and entry2[1] == 'a':
        print("Ambos venceram")
    elif entry1[1] == 'e' and entry2[1] == 'e':
        print("Sem ganhador")
    elif entry1[1] == 't' and entry2[1] == 't':
        print("Aniquilacao mutua")