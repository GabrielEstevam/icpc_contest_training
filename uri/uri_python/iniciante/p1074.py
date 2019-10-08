n = int(input())
for i in range(n):
    entry = int(input())
    if entry == 0:
        print("NULL")
    else:
        if entry % 2 == 0:
            if entry > 0:
                print("EVEN POSITIVE")
            else:
                print("EVEN NEGATIVE")
        else:
            if entry > 0:
                print("ODD POSITIVE")
            else:
                print("ODD NEGATIVE")