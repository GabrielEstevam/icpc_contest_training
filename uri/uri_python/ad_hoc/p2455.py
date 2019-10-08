entry = input().split(" ")
if int(entry[0])*int(entry[1]) > int(entry[2])*int(entry[3]):
    print("-1")
elif int(entry[0])*int(entry[1]) < int(entry[2])*int(entry[3]):
    print("1")
else:
    print("0")