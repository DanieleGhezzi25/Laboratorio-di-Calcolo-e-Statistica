# Write a Python program to draw a Poisson distribution for several values of its mean, overlapped
# probability = poisson.pmf(k, mu)

import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import poisson

def main():
    
    mu1 = 5 # frequency of success
    mu2 = 10
    mu3 = 20
    mu4 = 40
    n = 100
    
    # x_coord is the array that contains all the "k success"
    x_coord = np.arange(0, n, 1) # step = 1 because it's a discrete distribution
    y_coord1 = poisson.pmf(x_coord, mu1)
    y_coord2 = poisson.pmf(x_coord, mu2)
    y_coord3 = poisson.pmf(x_coord, mu3)
    y_coord4 = poisson.pmf(x_coord, mu4)
    
    fig, ax = plt.subplots(nrows = 1, ncols = 1)
    ax.plot(x_coord, y_coord1, label='Poissonian Distribution (mu = 5)', color ='red')
    ax.plot(x_coord, y_coord2, label='Poissonian Distribution (mu = 10)', color ='blue')
    ax.plot(x_coord, y_coord3, label='Poissonian Distribution (mu = 20)', color ='green')
    ax.plot(x_coord, y_coord4, label='Poissonian Distribution (mu = 40)', color ='purple')
    ax.set_title('Poissonian Distribution')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()
    
    plt.show()
    
    return

if __name__ == "__main__":
  main ()