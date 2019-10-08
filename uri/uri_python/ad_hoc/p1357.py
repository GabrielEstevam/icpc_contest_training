N = int(input())
while N != 0:
    if input() == 'S':
        entry = input()
        out1 = ""
        out2 = ""
        out3 = ""
        for i in range(N):
            if i > 0:
                out1 += ' '
                out2 += ' '
                out3 += ' '
            if entry[i] == '1' or entry[i] == '2' or entry[i] == '5' or entry[i] == '8':
                out1 += '*.'
            elif entry[i] == '3' or entry[i] == '4' or entry[i] == '6' or entry[i] == '7':
                out1 += '**'
            elif entry[i] == '9' or entry[i] == '0':
                out1 += '.*'

            if entry[i] == '1' or entry[i] == '3':
                out2 += '..'
            elif entry[i] == '2' or entry[i] == '6' or entry[i] == '9':
                out2 += '*.'
            elif entry[i] == '4' or entry[i] == '5':
                out2 += '.*'
            elif entry[i] == '7' or entry[i] == '8' or entry[i] == '0':
                out2 += '**'

            out3 += ".." 
        print(out1)
        print(out2)
        print(out3)
    else:
        entry1 = input().split(' ')
        entry2 = input().split(' ')
        entry3 = input().split(' ')
        out = ""
        for i in range(N):
            if entry1[i] == '*.' and entry2[i] == '..' and entry3[i] == '..':
                out += '1'
            elif entry1[i] == '*.' and entry2[i] == '*.' and entry3[i] == '..':
                out += '2'
            elif entry1[i] == '**' and entry2[i] == '..' and entry3[i] == '..':
                out += '3'
            elif entry1[i] == '**' and entry2[i] == '.*' and entry3[i] == '..':
                out += '4'
            elif entry1[i] == '*.' and entry2[i] == '.*' and entry3[i] == '..':
                out += '5'
            elif entry1[i] == '**' and entry2[i] == '*.' and entry3[i] == '..':
                out += '6'
            elif entry1[i] == '**' and entry2[i] == '**' and entry3[i] == '..':
                out += '7'
            elif entry1[i] == '*.' and entry2[i] == '**' and entry3[i] == '..':
                out += '8'
            elif entry1[i] == '.*' and entry2[i] == '*.' and entry3[i] == '..':
                out += '9'
            elif entry1[i] == '.*' and entry2[i] == '**' and entry3[i] == '..':
                out += '0'
        print(out)
    N = int(input())
