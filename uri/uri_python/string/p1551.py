for n in range(int(input())):
    entry = input()
    alfabeto = []
    for i in range(26):
        alfabeto.append(False)
    for i in entry:
        letra = ord(i)
        if 97 <= letra <= 122:
            alfabeto[letra-97] = True
    soma = 0
    for i in alfabeto:
        if i:
            soma += 1
    if soma == 26:
        print("frase completa")
    elif soma >= 13:
        print("frase quase completa")
    else:
        print("frase mal elaborada")