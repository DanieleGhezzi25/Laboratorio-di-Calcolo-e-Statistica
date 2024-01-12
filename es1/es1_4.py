# Write a program that, by using a for loop, returns the Fibonacci sequence up to the n-th term and stores it in a python dictionary, where the key represents the index of each element and value its actual value.

def fibonacci_sequence (N):
	if N == 0:
		print({0:0})
	elif N == 1:
		print({0:0, 1:1})
	else:
		fibonacci = {0:0, 1:1}
		i = 2
		while int(i) < N:
			fibonacci.update({i:fibonacci[len(fibonacci)-1] + fibonacci[len(fibonacci) - 2]})
			i=i+1
		for idx in fibonacci: print (idx, fibonacci[idx]) 
	return
	
def main():
	N = int(input('Insert N: '))
	fibonacci_sequence(N)
	return
	
if __name__ == "__main__":
	main()

