# Write a Python program to draw a binomial distribution and its cumulative function
# probability = binom.pmf(k, n, p), where k = success, n = total events, p = probability success 

import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import binom

def main():
    
    p = 0.5
    n = 100 # total events
    
    # x_coord is the array that contains all the "k success"
    x_coord = np.arange(0, n, 1) # step = 1 because it's a discrete distribution
    y_coord1 = binom.pmf(x_coord, n, p)
    
    fig, ax1 = plt.subplots(nrows = 1, ncols = 1)
    ax1.plot(x_coord, y_coord1, label='Binomial Distribution', color ='red')
    ax1.set_title('Binomial Distribution (p = 0.5, n = 100)')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.legend()
    
    # ------------------- #
    
    y_coord2 = binom.cdf(x_coord, n, p)
    
    fig2, ax2 = plt.subplots(nrows = 1, ncols = 1)
    ax2.plot(x_coord, y_coord2, label='Binomial cdf', color ='blue')
    ax2.set_title('Binomial cdf')
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    ax2.legend()
    
    
    plt.show()
    
    return

if __name__ == "__main__":
  main ()