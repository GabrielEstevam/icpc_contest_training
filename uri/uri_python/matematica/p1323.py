N = int(input())
while N > 0:
    sum = 0
    for i in range(N+1):
        sum += i*i
    print(sum)
    N = int(input())