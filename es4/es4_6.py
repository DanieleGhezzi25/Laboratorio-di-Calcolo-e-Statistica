# Implement a pseudo-random number generator that uses the inverse function method to generate events 
# distributed according to an exponential probability distribution.

import numpy as np
import matplotlib.pyplot as plt
import random

def cumulative_inverse_exponential_function(y):
    gamma = 4
    # the cdf is y = 1 - gamma*exp(-gamma*x)
    return (np.log(gamma)-np.log(1-y))/gamma

def inverse_function_algorithm(cumulative_inverse_function):
    y = random.uniform(0,1)
    return cumulative_inverse_function(y)

def sturges(N):
    return int(np.ceil(1+3.322*np.log(N)))

def main():
    N = 20000
    random_exponential_distribution = []
    
    for i in range(N):
        random_exponential_distribution.append(inverse_function_algorithm(cumulative_inverse_exponential_function))
    
    bin_intervals = np.linspace(np.min(random_exponential_distribution), np.max(random_exponential_distribution), sturges(N))
    
    fig, ax = plt.subplots(1,1)
    ax.hist(random_exponential_distribution, bins=bin_intervals, color='red')
    ax.set_xlabel('Random Generated Numbers')
    ax.set_ylabel('Counts')
    ax.set_title('Random Exponential Distribution')
    ax.legend()
    
    plt.show()
    
    return

if __name__ == "__main__":
  main ()