# Given an array of numbers, write a Python library containing a function which determines the value below which 
# lies the 25% of the values, and the one above which lies the 25% of the the values.
# Generalise the function to the case where the percentage of tails is set as input value

import numpy as np
import module_es2_6 as mod

def main():
    percentual = 21.9
    array = np.arange(0, 100)
    value1, value2 = mod.values_that_determine_tails_given_the_percentual(array, percentual)
    print(value1,value2)
    return

if __name__ == '__main__':
    main()