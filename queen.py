while (True):
	s = raw_input()
	vet = map (int, s.split())

	if (vet[0] == 0):
		break

	if (vet[0] == vet[2]) and (vet[1] == vet[3]):
		print 0
		continue

	if (vet[0] == vet[2]) or (vet[1] == vet[3]):
		print 1
		continue

	if abs(vet[0] - vet[2]) == abs (vet[1] - vet[3]):
		print 1
		continue

	print 2

