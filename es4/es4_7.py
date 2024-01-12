# Implement a pseudo-random number generator that uses the central limit theorem method to generate events 
# distributed according to a Gaussian probability distribution.

# How can you obtain a normal distribution, i.e., a Gaussian distribution centered at zero with unit variance?

# Visually verify that as the number of events increases, the similarity between the obtained distribution and the 
# Gaussian functional form increases, both graphically and by using the moments of the distributions calculated on 
# the generated event sample.

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import random

def sturges(N):
    return int(np.ceil(1+3.322*np.log(N)))

def random_gaussian_variable_generator_clt(mean, variance, N):
    
    # Pseudo number generator of an event with gaussian probability distribution.
    # The generator uses the Central Limit Theorem.
    # First it generates N xi variables according to uniform distribution with same mean and variance.
    # Then it takes xi and return the sample mean y = xi/N.
    # Its variance will be V = variance/N but the function won't return that

    # If y must have fixed mean and variance, the uniform distribution interval [a,b] will be 
    # (mean - delta, mean + delta)
    
    delta = np.sqrt(3*N*variance) # demonstrated
    interval_min = mean - delta
    interval_max = mean + delta
    
    yi = 0
    for i in range(N):
        yi += random.uniform(interval_min, interval_max)
    return yi/N

def main():
    random_gaussian_list = []
    M = 20000 # number gaussian i want
    N = 500 # number of uniform distributed variable taken in the gaussian's sum
    for i in range(M):
        random_gaussian_list.append(random_gaussian_variable_generator_clt(mean = 2, variance = 3, N = N))
    
    bin_intervals = np.linspace(np.min(random_gaussian_list), np.max(random_gaussian_list), sturges(M))
    
    print(f'mean = {np.mean(random_gaussian_list):.3f}')
    print(f'variance = {np.var(random_gaussian_list):.3f}')
    print(f'skewness = {stats.skew(random_gaussian_list):.3f}')
    print(f'kurtosis = {stats.kurtosis(random_gaussian_list):.3f}')
    
    fig, ax = plt.subplots(1,1)  
    ax.hist(random_gaussian_list, bins=bin_intervals, color='red')
    ax.set_xlabel('Random Generated Numbers')
    ax.set_ylabel('Counts')
    ax.set_title('Random Gaussian Distribution')
    ax.legend()
    plt.show()
    
    return

if __name__ == "__main__":
  main ()