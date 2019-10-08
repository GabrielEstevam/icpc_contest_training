entry = []
for N in range(int(input())):
    entry.append(input().split(" "))
while True:
    try:
        attempt = input().split(" ")
        for i in range(len(entry)):
            if entry[i][0] == attempt[0]:
                if attempt[1] == entry[i][1] or attempt[1] == entry[i][2] or attempt[1] == entry[i][3]:
                    print("Uhul! Seu amigo secreto vai adorar o/")
                else:
                    print("Tente Novamente!")
    except EOFError:
        break