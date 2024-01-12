# Testing module_stats.py with uniform distribution, central limit theorem and other random number generators.

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import random
import module_stats as st

def random_uniform_distribution(xmin, xmax, N):
    random_list = []
    for i in range(N):
        random_list.append(random.uniform(xmin, xmax,))
    return random_list

def cumulative_inverse_exponential_function(y):
    gamma = 4
    # the cdf is y = 1 - gamma*exp(-gamma*x)
    return (np.log(gamma)-np.log(1-y))/gamma

def inverse_function_algorithm(cumulative_inverse_function):
    y = random.uniform(0,1)
    return cumulative_inverse_function(y)

def random_gaussian_variable_generator_clt(mean, variance, N):
    
    delta = np.sqrt(3*N*variance) # demonstrated
    interval_min = mean - delta
    interval_max = mean + delta
    
    yi = 0
    for i in range(N):
        yi += random.uniform(interval_min, interval_max)
    return yi/N

# --------------------------------------------------------- #

def main():
    N = 10000
    xmin = -5
    xmax = 5
    
    uniform_distribution = st.stats(list=random_uniform_distribution(xmin,xmax,N))
    print('Uniform stats:')
    uniform_distribution.print_stats()
    uniform_distribution.hist(title='Uniform Distribution', label='Uniform Distribution')
    
    random_exponential_distribution = []
    for i in range(N):
        random_exponential_distribution.append(inverse_function_algorithm(cumulative_inverse_exponential_function))
    
    random_exponential_distribution = st.stats(list=random_exponential_distribution)
    print('Exponential stats:')
    random_exponential_distribution.print_stats()
    random_exponential_distribution.hist(title='Exponential Distribution', label='Exponential Distribution')
    
    random_gaussian_list = []
    for i in range(N):
        random_gaussian_list.append(random_gaussian_variable_generator_clt(mean = 0, variance = 1, N = 500))
    random_gaussian_distribution = st.stats(list=random_gaussian_list)
    print('Gaussian stats:')
    random_gaussian_distribution.print_stats()
    random_gaussian_distribution.hist(title='Gaussian Distribution', label='Gaussian Distribution')
    
    return

if __name__ == "__main__":
    main()