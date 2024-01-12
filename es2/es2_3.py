# Create a one-dimensional array containing the sequence of the first 50 even natural numbers
# Create a one-dimensional array containing the sequence of the first 50 odd natural numbers
# Create a one-dimensional array containing the element-wise sum of the previous two arrays

import numpy as np

def main():
    even = np.arange(0,100,2)
    odd = np.arange(1,100,2)
    sum = even + odd
    print(even)
    print(odd)
    print(sum)
    return

if __name__ == '__main__':
    main()