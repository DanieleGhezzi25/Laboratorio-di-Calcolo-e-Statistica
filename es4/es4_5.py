# Implement a pseudo-random number generator that uses the try-and-catch method to generate pseudo-random numbers 
# according to an arbitrary probability distribution. Take the probability density function (pdf) as an 
# input parameter for generating random numbers. Use the matplotlib library to visualize the distribution.

import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.stats import norm

def standard_gaussian_f(x):
    return norm.pdf(x, 0, 1)

def try_and_catch(xmin, xmax, ymax, function):
    x = random.uniform(xmin, xmax)
    y = random.uniform(0, ymax)
    while (y > function(x)):
        x = random.uniform(xmin, xmax)
        y = random.uniform(0, ymax)
    return x

def sturges(N):
    return int(np.ceil(1+3.322*np.log(N)))

def main():
    mean = 0
    sigma = 1
    xmin = -5*sigma
    xmax = 5*sigma
    ymax = standard_gaussian_f(mean)
    N = 10000
    random_gaussian_list = []
    
    for i in range(N):
        random_gaussian_list.append(try_and_catch(xmin, xmax, ymax, standard_gaussian_f))
    
    bin_intervals = np.linspace(xmin,xmax,sturges(N))
    
    fig, ax = plt.subplots(1,1)
    ax.hist(random_gaussian_list, bins=bin_intervals, color='red')
    ax.set_xlabel('Random Gaussian Data')
    ax.set_ylabel('Counts')
    ax.legend()
    ax.set_title('Random Gaussian Distribution')
    
    plt.show()
    
    return

if __name__ == "__main__":
  main ()
        
        
    

