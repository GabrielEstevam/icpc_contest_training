import math
while True:
	try:
		entry = input().split(" ")
		h1 = float(entry[0])
		h2 = float(entry[1])
		h3 = float(entry[2])

		if (h1 == 0 or h2 == 0 or h3 == 0):
			print("-1.000")
		else:
			num = (-4*h1*h1 + 8*h2*h2 + 8*h3*h3)/9
			if (num <= 0):
				print("-1.000")
			else:
				x1 = math.sqrt(num)
				num = (4*h2*h2 + 8*h3*h3 - 6*x1*x1)/3
				if (num <= 0):
					print("-1.000")
				else:
					x2 = math.sqrt(num)
					num = 2*x1*x1 + 2*x2*x2 - 4*h3*h3
					if (num <= 0):
						print("-1.000")
					else:
						x3 = math.sqrt(num)
						p = (x1+x2+x3)/2
						num = p*(p-x1)*(p-x2)*(p-x3)
						if (num <= 0):
							print("-1.000")
						else:
							A = math.sqrt(num)
							#if (round(A, 3) == 0):
							#	print("-1.000")
							#else:
							#print("x1, x2, x3: ", x1, x2, x3)
							#print(A)
							print('{:.3f}'.format(A))

	except EOFError:
		break
