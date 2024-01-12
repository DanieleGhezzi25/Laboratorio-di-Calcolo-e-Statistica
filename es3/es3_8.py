# Write a Python program to draw an exponential distribution and its cumulative function

import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import expon

def main():
   
    x_coord = np.linspace(-5,5,10000)
    y_coord1 = expon.pdf(x_coord)
    
    fig1, ax1 = plt.subplots(nrows = 1, ncols = 1)
    ax1.plot(x_coord, y_coord1, label='Exponential pdf', color ='red')
    ax1.set_title('Exponential pdf')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.legend()
    
    # --------------------- #
    
    y_coord2 = expon.cdf(x_coord)
    
    fig2, ax2 = plt.subplots(nrows = 1, ncols = 1)
    ax2.plot(x_coord, y_coord2, label='Exponential cdf', color ='blue')
    ax2.set_title('Exponential cdf')
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    ax2.legend()
    
    plt.show()
    
    return

if __name__ == "__main__":
  main ()