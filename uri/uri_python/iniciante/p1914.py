for N in range(int(input())):
    entry = input().split(" ")
    nums = input().split(" ")
    if entry[1] == "PAR":
        if (int(nums[0]) + int(nums[1])) % 2 == 0:
            print(entry[0])
        else:
            print(entry[2])
    elif entry[1] == "IMPAR":
        if (int(nums[0]) + int(nums[1])) % 2 != 0:
            print(entry[0])
        else:
            print(entry[2])