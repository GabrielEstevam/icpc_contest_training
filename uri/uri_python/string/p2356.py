while True:
    try:
        DNA = input()
        entry = input()
        if DNA.find(entry) == -1:
            print("Nao resistente")
        else:
            print("Resistente")
    except EOFError:
        break