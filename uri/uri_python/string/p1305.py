while True:
    try:
        entry = input().split('.')
        cutoff = input().split('.')
        if len(entry) == 1:
            print(entry[0])
        else:
            num = 0
            if len(entry[0]) > 0:
                num += int(entry[0])
            while len(entry[1]) < 4:
                entry[1] += '0'
            cutoffN = 0
            entryN = 0
            for i in range(4):
                cutoffN = cutoffN*10 + int(cutoff[1][i])
                entryN = entryN*10 + int(entry[1][i])
            if entryN >= cutoffN:
                num += 1
            print(num)
    except EOFError:
        break