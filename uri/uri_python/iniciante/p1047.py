entry = input().split(" ")
for i in range(len(entry)):
	entry[i] = int(entry[i])
hour = entry[2]-entry[0]
minute = entry[3]-entry[1]
minute += hour*60
if minute <= 0:
	minute += 1440
hour = (int) (minute/60)
minute -= hour*60
print("O JOGO DUROU", hour, "HORA(S) E", minute, "MINUTO(S)")
