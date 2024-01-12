# Write a Python program to draw a Poisson distribution. Show, by using the third and fourth central momenta calculations 
# available in the scipy.stat library, that the momenta of a Poisson distribution asymptotically tend to the ones of a 
# Gaussian.

import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import poisson

def main():
    
    mu1 = 5 # frequency of success
    mu2 = 10
    mu3 = 25
    mu4 = 50
    mu5 = 75
    n = 100
    
    # x_coord is the array that contains all the "k success"
    x_coord = np.arange(0, n, 1) # step = 1 because it's a discrete distribution
    
    y_coord1 = poisson.pmf(x_coord, mu1)
    skew1, kurt1 = poisson.stats(mu1, moments='sk')
    
    y_coord2 = poisson.pmf(x_coord, mu2)
    skew2, kurt2 = poisson.stats(mu2, moments='sk')
    
    y_coord3 = poisson.pmf(x_coord, mu3)
    skew3, kurt3 = poisson.stats(mu3, moments='sk')
    
    y_coord4 = poisson.pmf(x_coord, mu4)
    skew4, kurt4 = poisson.stats(mu4, moments='sk')
    
    y_coord5 = poisson.pmf(x_coord, mu5)
    skew5, kurt5 = poisson.stats(mu5, moments='sk')
    
    fig, ax = plt.subplots(nrows = 1, ncols = 1)
    ax.plot(x_coord, y_coord1, label='Poissonian Distribution (mu = 5)', color ='red')
    ax.plot(x_coord, y_coord2, label='Poissonian Distribution (mu = 10)', color ='blue')
    ax.plot(x_coord, y_coord3, label='Poissonian Distribution (mu = 25)', color ='green')
    ax.plot(x_coord, y_coord4, label='Poissonian Distribution (mu = 50)', color ='purple')
    ax.plot(x_coord, y_coord5, label='Poissonian Distribution (mu = 75)', color ='yellow')
    ax.set_title('Poissonian Distribution')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()
    
    print(f"For mu = 5, we have skewness = {skew1} and kurtosis = {kurt1}.")
    print(f"For mu = 10, we have skewness = {skew2} and kurtosis = {kurt2}.")
    print(f"For mu = 25, we have skewness = {skew3} and kurtosis = {kurt3}.")
    print(f"For mu = 50, we have skewness = {skew4} and kurtosis = {kurt4}.")
    print(f"For mu = 75, we have skewness = {skew5} and kurtosis = {kurt5}.")
    
    plt.show()
    
    return

if __name__ == "__main__":
  main ()
