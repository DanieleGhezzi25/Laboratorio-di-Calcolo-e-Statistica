def fibonacci_sequence (N):
	if N == 0:
		print(0)
	elif N == 1:
		print([0, 1])
	else:
		fibonacci = [0,1]
		i = 2
		while int(i) < N:
			fibonacci.append(fibonacci[len(fibonacci)-1] + fibonacci[len(fibonacci) - 2])
			i=i+1
		print(fibonacci)
	return fibonacci

