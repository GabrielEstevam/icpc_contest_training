import math
while True:
	try:
		entry = input().split(" ")
		Xf = int(entry[0])
		Yf = int(entry[1])
		Xi = int(entry[2])
		Yi = int(entry[3])
		Vi = int(entry[4])
		R1 = int(entry[5])
		R2 = int(entry[6])
		d = math.sqrt(pow(Xf-Xi, 2) + pow(Yf-Yi, 2))		
		if (R1 + R2 >= d + Vi*1.5):
			print("Y")
		else:
			print("N")
	except EOFError:
		break
