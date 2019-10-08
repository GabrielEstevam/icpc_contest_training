N = int(input())
i = 1
while N != -1:
    r = "Experiment "+str(i)+": "+ str(int(N/2)) + " full cycle(s)"
    i += 1
    print(r)
    N = int(input())