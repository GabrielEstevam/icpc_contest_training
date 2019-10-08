fib = [1, 1]
size = 2
thr = []
while len(thr) < 60:
    fib.append(fib[size-1] + fib[size-2])
    size += 1
    f = str(fib[size-1])
    soma = 0
    flag = 0
    for i in f:
        if i == '3':
            flag = 1
            break
        soma += int(i)
    if flag or soma % 3 == 0:
        thr.append(f)
while True:
    try:
        print(thr[int(input())-1])
    except EOFError:
        break