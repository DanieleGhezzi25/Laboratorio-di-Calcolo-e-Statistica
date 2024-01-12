# Implement a pseudo-random number generator according to a uniform distribution between two arbitrary endpoints.
# Use the matplotlib library to visualize the distribution of the generated numbers.

import numpy as np
import random
from matplotlib import pyplot as plt

def random_uniform_distribution(xmin, xmax, N):
    random_list = []
    for i in range(N):
        random_list.append(random.uniform(xmin, xmax,))
    return random_list

def sturges(N):
    return int(np.ceil(1+3.322*np.log(N)))

def main():
    xmin = 0
    xmax = 10
    N = 10000
    random_list = random_uniform_distribution(xmin, xmax, N)
    
    bin_intervals = np.linspace(np.min(random_list), np.max(random_list), sturges(N))
  
    fig, ax = plt.subplots(1,1)
    ax.hist(random_list, bins=bin_intervals, color='red')
    
    plt.show()
    
    return

if __name__ == "__main__":
    main()