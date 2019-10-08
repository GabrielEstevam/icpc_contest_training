entry1 = input()
entry2 = input()
entry3 = input()
if entry1 == 'vertebrado':
	if entry2 == 'ave':
		if entry3 == 'carnivoro':
			print('aguia')
		else:
			print('pomba')
	else:
		if entry3 == 'onivoro':
			print('homem')
		else:
			print('vaca')
else:
	if entry2 == 'inseto':
		if entry3 == 'hematofago':
			print('pulga')
		else:
			print('lagarta')
	else:
		if entry3 == 'hematofago':
			print('sanguessuga')
		else:
			print('minhoca')
