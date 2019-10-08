while True:
    try:
        entry1 = input()
        entry2 = input()
        cont = 0
        for i in range(len(entry1)):
            for j in range(len(entry2)):
                if entry1[i] == entry2[j]:
                    cont += 1
        print(cont) 
    except EOFError:
        break