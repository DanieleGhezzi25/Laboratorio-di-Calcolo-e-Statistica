# Read the text file eventi_gauss.txt:
# Fill a histogram with the first N numbers contained in the file, where N is a command-line parameter during program execution.
# Choose the histogram’s definition range and its bin number based on the numbers to be represented.

import numpy as np
from matplotlib import pyplot as plt

def sturges(N):
    return int(np.ceil(1+3.322*np.log(N)))

def main():
    
    N = int(input('Insert N: '))
    
    sample_N = np.loadtxt('eventi_gauss.txt', max_rows=N)
    
    bins_number = sturges(N)
    bin_intervals = np.linspace(np.min(sample_N), np.max(sample_N), bins_number)
    
    fig,ax = plt.subplots(nrows=1,ncols=1)
    ax.hist(sample_N, bins=bin_intervals, color='red')
    ax.set_xlabel('Data')
    ax.set_ylabel('Number')
    ax.set_title('Gaussian Distribution')
    
    plt.show()
    
    return

if __name__ == "__main__":
  main ()