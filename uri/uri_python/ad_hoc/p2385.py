N = int(input())
entry = input().split(" ")
P = int(entry[0])
Q = int(entry[1])
R = int(entry[2])
S = int(entry[3])
X = int(entry[4])
Y = int(entry[5])
entry = input().split(" ")
I = int(entry[0])
J = int(entry[1])
soma = 0
for n in range(N):
    Aij = (P * I + Q * (n + 1)) % X
    Bij = (R * (n + 1) + S * J) % Y
    soma += Aij * Bij
print(soma)