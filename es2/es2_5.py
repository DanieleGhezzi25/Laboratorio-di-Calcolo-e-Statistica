# After finding how the numpy.sort function works, write a Python library containing a function that determines the median of an array.
# Write a main program that tests the performance of the developed function.

import numpy as np
import module_es2_5 as mod

def main():
    list = [1,6,2,5,8,3,1,54,6,6,6,7,8,3,1,2,3,5,78,9,34,1,34,1,1,1,1,1,1,1,5,7,5,7,4,2,1]
    array = np.array(list)
    median = mod.median(array)
    print (median)
    return

if __name__ == '__main__':
    main()
    