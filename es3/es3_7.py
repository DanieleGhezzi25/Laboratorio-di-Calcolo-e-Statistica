# Write a Python program to draw a Gaussian distribution and its cumulative function

import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm

def main():
    
    mean = 0
    sigma = 1
    
    x_coord = np.linspace(-5,5,10000)
    y_coord1 = norm.pdf(x_coord,mean,sigma)
    
    fig1, ax1 = plt.subplots(nrows = 1, ncols = 1)
    ax1.plot(x_coord, y_coord1, label='Gaussian pdf', color ='red')
    ax1.set_title('Gaussian pdf')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.legend()
    
    # --------------------- #
    
    y_coord2 = norm.cdf(x_coord,mean,sigma)
    
    fig2, ax2 = plt.subplots(nrows = 1, ncols = 1)
    ax2.plot(x_coord, y_coord2, label='Gaussian cdf', color ='blue')
    ax2.set_title('Gaussian cdf')
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    ax2.legend()
    

    plt.show()
    
    return

if __name__ == "__main__":
  main ()