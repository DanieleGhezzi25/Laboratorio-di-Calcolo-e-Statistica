# find the list of prime integer smaller than 100, starting by knowing that 2 is a prime number

def is_prime_number (a, primes):
    for i in range(len(primes)):
        flag = 0
        if a % primes[i] == 0:
            flag = -1
            break
    if flag == -1:
        return False
    else:
        return True
        
    
def primes_f(N):
    primes = [2]
    i = 2
    while i <= N:
        if is_prime_number(i,primes) == True:
            primes.append(i)
        i = i + 1
    return primes

def main():
    N = int(input('Insert N: '))
    primes_list = primes_f(N)
    print (primes_list)
    return

if __name__ == "__main__":
  main ()

