while True:
	try:
		entry = input()
		saida = ""
		if len(entry) > 1:
			for i in range(len(entry)):
				if (entry[i]).lower() == 'a' or (entry[i]).lower() == 'b' or (entry[i]).lower() == 'c':
					saida += '2'
				elif (entry[i]).lower() == 'd' or (entry[i]).lower() == 'e' or (entry[i]).lower() == 'f':
					saida += '3'
				elif (entry[i]).lower() == 'g' or (entry[i]).lower() == 'h' or (entry[i]).lower() == 'i':
					saida += '4'
				elif (entry[i]).lower() == 'j' or (entry[i]).lower() == 'k' or (entry[i]).lower() == 'l':
					saida += '5'
				elif (entry[i]).lower() == 'm' or (entry[i]).lower() == 'n' or (entry[i]).lower() == 'o':
					saida += '6'
				elif (entry[i]).lower() == 'p' or (entry[i]).lower() == 'q' or (entry[i]).lower() == 'r' or (entry[i]).lower() == 's':
					saida += '7'
				elif (entry[i]).lower() == 't' or (entry[i]).lower() == 'u' or (entry[i]).lower() == 'v':
					saida += '8'
				elif (entry[i]).lower() == 'w' or (entry[i]).lower() == 'x' or (entry[i]).lower() == 'y' or (entry[i]).lower() == 'z':
					saida += '9'
				elif entry[i] == '*' or entry[i] =='#' or entry[i].isdigit():
					saida += entry[i]
		print(saida)
	except EOFError:
		break
