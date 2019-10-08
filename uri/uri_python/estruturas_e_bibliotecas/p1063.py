N = int(input())
while N != 0:
    e1 = input().split(' ')
    entry1 = []
    for i in range(len(e1)):
        if len(e1[i]) > 0:
            if ord(e1[i]) >= 97 and ord(e1[i]) <= 122:
                entry1.append(e1[i])
    e2 = input().split(' ')
    entry2 = []
    for i in range(len(e2)):
        if len(e2[i]) > 0:
            if ord(e2[i]) >= 97 and ord(e2[i]) <= 122:
                entry2.append(e2[i])
    stack = ['-', entry1.pop(0)]
    out = 'I'
    while True:
        #print('s: ', stack)
        #print('e2: ', entry2)
        #print('e1: ', entry1)
        if stack[len(stack)-1] == entry2[0]:
            out += 'R'
            stack.pop()
            entry2.pop(0)
        else:
            if len(entry1) == 0:
                break
            stack.append(entry1.pop(0))
            out += 'I'
        if len(entry2) == 0:
            break
        
    if len(entry2) == 0:
        print(out)
    else:
        print(out, "Impossible")
    N = int(input())