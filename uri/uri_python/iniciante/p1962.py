N = int(input())
for n in range(N):
    entry = int(input())
    if entry >= 2015:
        print(entry - 2014, "A.C.")
    else:
        print(2015 - entry, "D.C.")