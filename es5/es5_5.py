# Write a python program that reads the sample file eventi_gauss.txt of Exercise 3.3 and, 
# using the map function, creates the distribution of the squares and cubes of random Gaussian numbers, 
# respectively, using lambda functions in the process.
# Plot the distribution of them, together with the original sample one, all in the same frame.

import numpy as np
from matplotlib import pyplot as plt

def sturges(N):
    return int(np.ceil(1+3.322*np.log(N)))

def main():
    
    gaussian_data = np.loadtxt('eventi_gauss.txt')
    N = len(gaussian_data)
    
    gaussian_data_squared = list(map(lambda x: x**2, gaussian_data))
    gaussian_data_cubed = list(map(lambda x: x**3, gaussian_data))
    
    bin_intervals1 = np.linspace(np.min(gaussian_data), np.max(gaussian_data), sturges(N))
    bin_intervals2 = np.linspace(np.min(gaussian_data_squared), np.max(gaussian_data_squared), sturges(N))
    bin_intervals3 = np.linspace(np.min(gaussian_data_cubed), np.max(gaussian_data_cubed), sturges(N))
    
    fig, ax = plt.subplots(1,1)
    ax.hist(gaussian_data, label='Data', bins=bin_intervals1, color='red', alpha=0.7)
    ax.hist(gaussian_data_squared, label='Data Squared', bins=bin_intervals2, color='blue', alpha=0.6)
    ax.hist(gaussian_data_cubed, label='Data Cubed', bins=bin_intervals3, color='green', alpha=0.5)
    ax.set_xlabel('Data')
    ax.set_ylabel('Counts')
    ax.set_title('Gaussians')
    ax.legend()
    
    plt.show()
    
    return

if __name__ == "__main__":
  main ()