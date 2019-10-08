time = 0
entry = input().split(" ")
time -= int(entry[1])*86400
entry = input().split(" : ")
time -= int(entry[0])*3600
time -= int(entry[1])*60
time -= int(entry[2])
entry = input().split(" ")
time += int(entry[1])*86400
entry = input().split(" : ")
time += int(entry[0])*3600
time += int(entry[1])*60
time += int(entry[2])
days = int(time/86400)
time -= days*86400
hours = int(time/3600)
time -= hours*3600
minutes = int(time/60)
time -= minutes*60
print(str(days)+" dia(s)")
print(str(hours)+" hora(s)")
print(str(minutes)+" minuto(s)")
print(str(time)+" segundo(s)")