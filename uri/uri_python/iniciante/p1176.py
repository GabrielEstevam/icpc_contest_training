fib = [0, 1]
for i in range(2, 62):
    fib.append(fib[i-1]+fib[i-2])
T = int(input())
for i in range(T):
    N = int(input())
    print("Fib("+str(N)+") =", fib[N])
