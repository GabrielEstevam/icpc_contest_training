entrada = int(input())
while entrada != 0:
    attempt = input().split(" ")
    k = 0
    while len(attempt) != 1:
        k += 1
        attempt = input().split(" ")
    print(k)
    entrada = int(attempt[0])