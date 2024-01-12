# Use the source code written in the previous exercise to add to the library developed for exercise 1
# a function that generates random numbers according to the Poisson distribution, with the mean expected events
# as an input parameter.
# Rewrite the previous exercise using this function, also drawing the probability density histogram.
# Calculate the sample statistics (mean, variance, skewness, kurtosis) from the input list using a library.
# Use the generated sample to test the functionality of the library.

import module_randomGen as gen
import module_stats as st
import numpy as np

def main():
    
    mean = float(input('Insert mean: '))
    N_experiments = 100000
    
    poissonian_distribution = gen.POISSON_generation(mean, N_experiments)
    
    p_distr = st.stats(list = poissonian_distribution)
    p_distr.print_stats()
    p_distr.hist(bin_intervals = np.arange(np.min(poissonian_distribution)-0.5, np.max(poissonian_distribution)+1.5, 1), xlabel = 'Countings', ylabel = 'N times', title = 'Poissonian Distribution', label = 'Poissonian Distribution')
    
    return

if __name__ == "__main__":
  main ()