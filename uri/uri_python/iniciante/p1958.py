entry = input()
if entry[0] == '-':
    entry = float(entry)
    print('%.4E' % entry)
else:
    entry = float(entry)
    print('+%.4E' % entry)