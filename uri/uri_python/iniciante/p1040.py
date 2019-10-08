# -*- coding: utf-8 -*-
notas = input().split(" ")
pesos = [2, 3, 4, 1]
media = 0
for i in range(4):
    media += float(notas[i])*pesos[i]
media /= 10
print("Media: %.1f" % media)
if media >= 7:
    print("Aluno aprovado.")
elif media >= 5:
    print("Aluno em exame.")
    rec = float(input())
    print("Nota do exame: %.1f" % rec)
    media_final = (media+rec)/2
    if media_final >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: %.1f" % media_final)
else:
    print("Aluno reprovado.")
