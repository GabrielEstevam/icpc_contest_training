while True:
    try:
        N = int(input())
        soma = []
        entry = input().split(' ')
        soma.append(int(entry[0]))
        for i in range(1, N):
        	soma.append(int(entry[i]) + soma[i-1])
        tam = soma[N-1]/3
        tri = 0
        i = 0
        j = 0
        k = 0
        while True:
        	if soma[i] > tam:
        		break
        	while soma[j] < soma[i] + tam and j < N:
        		j += 1
        	while soma[k] < soma[i] + 2*tam and k < N:
        		k += 1
        	if soma[i] + tam == soma[j] and soma[j] + tam == soma[k]:
        		tri += 1
        	i += 1
        print(tri)

    except EOFError:
        break