import math
razao = math.sin(math.radians(108)) / math.sin(math.radians(63))
while True:
    try:
        print("{0:.10f}".format(float(input())*razao))
    except EOFError:
        break