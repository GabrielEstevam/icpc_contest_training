entrada = input().split(" ")
A = int(entrada[0])
B = int(entrada[1])
while A != 0 or B != 0:
    lenA = len(entrada[0])
    lenB = len(entrada[1])
    nCarry = 0
    carry = 0
    i = 0
    while lenA > i or lenB > i:
        num = A % 10 + B % 10 + carry
        if num > 9:
            nCarry += 1
        A = int(A/10)
        B = int(B/10)
        carry = int(num/10)
        i += 1

    if nCarry == 0:
        print("No carry operation.")
    elif nCarry == 1:
        print("1 carry operation.")
    else:
        print(nCarry, "carry operations.")

    entrada = input().split(" ")
    A = int(entrada[0])
    B = int(entrada[1])