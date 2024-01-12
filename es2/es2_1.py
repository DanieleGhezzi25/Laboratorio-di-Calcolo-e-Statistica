# Create one-dimensional NumPy arrays using different generation techniques

import numpy as np

def main():
    list = [1,2,3]
    array1 = np.array(list)
    N = 3
    array2 = np.zeros(N)
    array3 = np.empty(N) # not really empty but has very small number (10^-307)
    
    first = 0
    last = 10
    step = 2
    array4 = np.arange(first, last, step) # numbers from 0 to 10 stepping by 2
    
    number = 5
    array5 = np.linspace(first, last, number) # 5 numbers between 0 and 10
    
    print(array1, array2, array3, array4, array5)
    
    return

if __name__ == "__main__":
  main ()