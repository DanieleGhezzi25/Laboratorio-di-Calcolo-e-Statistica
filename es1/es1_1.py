# Write a program that reads an integer given as input from the user and determines whether it is divisible by 2, 3, 5, or 7.
# Encapsulate the check into a function taking as input two numbers, and write a program that asks the user to insert two numbers and checks whether the first is divisible by the other one (and vice-versa).

def divisible_by (x, divisor):
	if x % divisor == 0: 
		print (x, 'is divisible by', divisor)
	else:
		print (x, 'is not divisible by', divisor)
	return
	
def main ():
	a = int(input('Insert a number: '))
	divisible_by(a, 2)
	divisible_by(a, 3)
	divisible_by(a, 5)
	divisible_by(a, 7)
	print ('-----------------------')
	num = int(input('Insert another number: '))
	divisor = int(input('Insert a divisor: '))
	divisible_by(num, divisor)
	return


if __name__ == "__main__":
  main ()

