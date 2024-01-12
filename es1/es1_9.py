# Find the decomposition in prime factors of a positive integer number, incapsulating the algorithm in a module
# Write a test function to find the decomposition for all numbers from 1 to 100

import module_es1_9 as mod

def main():
    N = int(input('N = '))
    print('===========================')
    for i in range(1,N+1):
        mod.decomposition(i)
    return
    
if __name__ == "__main__":
  main ()
             
             