entry = input().split(" ")
if int(entry[3]) == 1 and int(entry[4]) == 1:
    print("Jogador 2 ganha!")
elif int(entry[3]) == 1 and int(entry[4]) == 0:
    print("Jogador 1 ganha!")
elif int(entry[3]) == 0 and int(entry[4]) == 1:
    print("Jogador 1 ganha!")
elif int(entry[3]) == 0 and int(entry[4]) == 0:
    if int(entry[0]) == 1:
        if (int(entry[1]) + int(entry[2])) % 2 == 0:
            print("Jogador 1 ganha!")
        else:
            print("Jogador 2 ganha!")
    else:
        if (int(entry[1]) + int(entry[2])) % 2 == 0:
            print("Jogador 2 ganha!")
        else:
            print("Jogador 1 ganha!")