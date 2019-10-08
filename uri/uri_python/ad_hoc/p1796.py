N = int(input())
entrada = input().split(" ")
k = 0
for i in range(N):
    k += int(entrada[i])
if k >= N/2:
    print("N")
else:
    print("Y")