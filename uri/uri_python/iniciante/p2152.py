for n in range(int(input())):
    entry = input().split(" ")
    if entry[2] == '1':
        print('{:0>2}'.format(int(entry[0])) + ':' + '{:0>2}'.format(int(entry[1])) + ' - A porta abriu!')
    else:
        print('{:0>2}'.format(int(entry[0])) + ':' + '{:0>2}'.format(int(entry[1])) + ' - A porta fechou!')