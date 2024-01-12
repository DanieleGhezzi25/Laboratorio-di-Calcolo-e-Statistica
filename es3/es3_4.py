# Display the distributions of events from the two files of the previous exercises, overlaid, 
# finding the best visualization for the comparison between the two histograms.

import numpy as np
from matplotlib import pyplot as plt

def sturges(N):
    return int(np.ceil(1+3.322*np.log(N)))

def main():
    
    sample_unif = np.loadtxt('eventi_unif.txt')
    sample_gauss = np.loadtxt('eventi_gauss.txt')
    
    fig, ax = plt.subplots(nrows=1, ncols=1)
    
    bin_intervals_unif = np.linspace(np.min(sample_unif), np.max(sample_unif), sturges(len(sample_unif)))
    bin_intervals_gauss = np.linspace(np.min(sample_gauss), np.max(sample_gauss), sturges(len(sample_gauss)))
    
    ax.hist(sample_unif, bins=bin_intervals_unif, color='red')
    ax.hist(sample_gauss, bins=bin_intervals_gauss, color='blue')
    ax.set_xlabel('Data')
    ax.set_ylabel('Event')
    ax.set_title('Comparison between Uniform and Gaussian Distribution')
    
    plt.show()
    
    return


if __name__ == "__main__":
  main ()