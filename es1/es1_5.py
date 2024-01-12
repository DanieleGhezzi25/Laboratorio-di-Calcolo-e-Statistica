from library_es1_5 import fibonacci_sequence

def main():
	N = int(input('Insert N: '))
	fibonacci_list = fibonacci_sequence(N)
	fibonacci_pairs = fibonacci_list[0:N:2]
	fibonacci_odd = fibonacci_list[1:N:2]
	print(fibonacci_pairs)
	print(fibonacci_odd)
	return
	
if __name__ == "__main__":
	main()
