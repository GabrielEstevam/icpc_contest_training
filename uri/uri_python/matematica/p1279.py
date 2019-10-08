flag = False
while True:
    try:
        entry = int(input())
        bissexto = False
        huluculu = False
        bulukulu = False
        if entry % 4 == 0 and (entry % 400 == 0 or entry % 100 != 0):
            bissexto = True
        if entry % 15 == 0:
            huluculu = True
        if bissexto and entry % 55 == 0:
            bulukulu = True
        if flag:
            print("")
        else:
            flag = True
        if not bissexto and not huluculu and not bulukulu:
            print("This is an ordinary year.")
        else:
            if bissexto:
                print("This is leap year.")
            if huluculu:
                print("This is huluculu festival year.")
            if bulukulu:
                print("This is bulukulu festival year.")
    except EOFError:
        break