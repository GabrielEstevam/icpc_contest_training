dic = {}
while True:
    try:
        entry = input().lower()
        aux = ""
        for i in entry:
            if ord(i) >= 97 and ord(i) <= 122:
                aux += i
            elif len(aux) > 0:
                if aux not in dic:
                    dic[aux] = aux
                aux = ""
    except EOFError:
        break
for i in sorted(dic):
    print(i)