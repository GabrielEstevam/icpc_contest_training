n = int(input())
IN = 0
OUT = 0
for i in range(n):
    entry = int(input())
    if 10 <= entry <= 20:
        IN += 1
    else:
        OUT += 1
print(str(IN)+" in")
print(str(OUT)+" out")