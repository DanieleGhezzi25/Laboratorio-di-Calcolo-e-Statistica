# Write a python program that reads the sample file eventi_unif.txt of Exercise 3.2 and, using the filter function, 
# creates two different sub-sets of events containing those larger or smaller than the average respectively, 
# using lambda functions in the process.
# Show that the sigma of the two subsets is half the one of the parent sample.

import numpy as np

def main():
    
    data = np.loadtxt('eventi_unif.txt')
    
    mean = np.mean(data)
    variance = np.var(data)
    
    first_half = list(filter(lambda x: x < mean, data))
    second_half = list(filter(lambda x: x >= mean, data))
    
    first_half_variance = np.var(first_half)
    second_half_variance = np.var(second_half)
    
    print(f'Original data std:{np.sqrt(variance)}')
    print(f'First half std:{np.sqrt(first_half_variance)}')
    print(f'Second half std:{np.sqrt(second_half_variance)}')
    
    return


if __name__ == "__main__":
  main ()
    
    