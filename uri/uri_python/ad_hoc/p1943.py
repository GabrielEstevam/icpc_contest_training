top = [1, 3, 5, 10, 25, 50, 100]
N = int(input())
for i in top:
    if N <= i:
        print("Top", i)
        break
