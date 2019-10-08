for i in range(int(input())):
    entry = input().split('mek')
    k = int(len(entry[0])-1)*int(len(entry[1])-2)
    out = "k"
    for j in range(k):
        out += 'a'
    print(out)
