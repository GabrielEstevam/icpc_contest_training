fibonacci = [1, 1]
for i in range(2, 41):
    fibonacci.append(fibonacci[i-1]+fibonacci[i-2])

N = int(input())
while N > 0:
    print(fibonacci[N])
    N = int(input())