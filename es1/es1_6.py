def squared (x):
	x = x**2
	return x
	
def multiplied_by (x,n):
	x = x*n
	return x

def main():	
	
	int = 12
	print(int)
	print(squared(int))
	print(int)
	
	print('--------------------------')
	
	float = 2.3
	print(float)
	print(squared(float))
	print(float)
	
	print('--------------------------')
	
	complex = 2 + 1j
	print (complex)
	print(squared(complex))
	print (complex)
	
	print('--------------------------')
	
	list = [1,2,3]
	print(list)
	print(multiplied_by(list,3))
	print(list)
	
	return


if __name__ == "__main__":
  main ()
  
  
  
