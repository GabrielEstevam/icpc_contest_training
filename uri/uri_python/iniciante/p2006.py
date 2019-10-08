C = input()
entry = input().split(" ")
acertos = 0
for i in entry:
    if i == C:
        acertos += 1
print(acertos)