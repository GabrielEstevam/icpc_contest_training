for N in range(int(input())):
    entry = input()
    cont = 1
    for i in range(len(entry)):
    	if entry[i] == 'A' or entry[i] == 'a' or entry[i] == 'E' or entry[i] == 'e' or entry[i] == 'I' or entry[i] == 'i' or entry[i] == 'O' or entry[i] == 'o' or entry[i] == 'S' or entry[i] == 's':
    		cont *= 3
    	else:
    		cont *= 2
    print(cont)