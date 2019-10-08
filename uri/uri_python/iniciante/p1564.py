while True:
    try:
        entry = input()
        if int(entry) > 0:
            print("vai ter duas!")
        else:
            print("vai ter copa!")
    except EOFError:
        break