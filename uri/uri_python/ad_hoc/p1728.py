# Functions
def verifica(equacao):
    instancia = equacao.split("+")
    a = int(inverte(instancia[0]))
    instancia = instancia[1].split("=")
    b = int(inverte(instancia[0]))
    c = int(inverte(instancia[1]))
    if a + b == c:
        return True
    else:
        return False

def inverte(stri):
    str_inv = ""
    tam = len(stri)
    for i in range(tam):
        str_inv += stri[tam-i-1]
    return str_inv

# Main
entrada = input()
print(verifica(entrada))
while entrada != "0+0=0":
    entrada = input()
    print(verifica(entrada))
