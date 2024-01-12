def is_prime_number (a, primes):
    
    # Defines if int a is divisible by a list of primes.
    # If that's true, return False (a is not a prime), else return False (a is a prime)
    # Args: int a, list primes
    # Return: Bool
    
    for i in range(len(primes)):
        flag = 0
        if a % primes[i] == 0:
            flag = -1
            break
    if flag == -1:
        return False
    else:
        return True
        
    
def numbers_prime_f (number):
    
    # Finds number's primes
    # Args: int number
    # Return: list primes
    
    primes = [2]
    i = 2
    while i <= number:
        if is_prime_number(i,primes) == True:
            primes.append(i)
        i = i + 1
    return primes

def decomposition (num):
    
    # Decomposes a number in prime factors.
    # Prints the factoritation with products and powers
    # It is a void function.
    # Args: int number
    # Return: ---
    
    if num == 1:
        print ('1 = 1')
        return 
    
    costant = num
    factors = []
    exponent = []
    his_primes = numbers_prime_f(num)
    
    for i in range(len(his_primes)):
        num = costant # ristabilisce il valore originario di num dopo la fine del ciclo (in cui num cambia)
        if num % his_primes[i] == 0:
            times = 1 # quante volte appare un fattore
            factors.append(his_primes[i])
            num = num/his_primes[i] 
            while num % his_primes[i] == 0:
                 times = times + 1
                 num = num/his_primes[i]
            exponent.append(times)
            
    print(costant,'= ', end="")
    for i in range(len(factors)):
        print(factors[i], '^', exponent[i], end=" * " if i < len(factors) - 1 else "\n")
                                 
    return
