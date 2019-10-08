while True:
    try:
        entry = input()
        num = 0
        k = 1
        for i in range(len(entry)-1,-1,-1):
            num = (num + k*(ord(entry[i])-65)) % 1000000007
            k = (k*26) % 1000000007
        print(num)
    except EOFError:
        break