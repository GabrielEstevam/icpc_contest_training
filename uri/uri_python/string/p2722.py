for i in range(int(input())):
    entry1 = input()
    entry2 = input()
    nome = ""
    for j in range(len(entry1)+len(entry2)):
        if j % 4 == 0 or j % 4 == 1:
            nome += entry1[int(j/4)*2+int(j%4)]
        else:
            nome += entry2[int(j/4)*2+int(j%4)-2]
    print(nome)