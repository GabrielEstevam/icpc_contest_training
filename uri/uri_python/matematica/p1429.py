entrada = input()
fac = [1, 2, 6, 24, 120]
while int(entrada):
    sum = 0
    for i in range(len(entrada)):
        sum += int(entrada[i])*fac[len(entrada)-i-1]
    print(sum)
    entrada = input()