# Read the text file eventi_unif.txt:
# Calculate the mean of the numbers in the text file.
# Calculate the variance of the numbers in the text file.
# Calculate the standard deviation of the numbers in the text file.
# Calculate the standard deviation from the mean of the numbers in the text file.

import numpy as np
from matplotlib import pyplot as plt

def main():
    
    sample = np.loadtxt('eventi_unif.txt')
    N = len(sample)
    
    mean = np.sum(sample)/N
    
    summatory = 0
    for i in range(N):
        summatory += (sample[i]-mean)**2
    variance = summatory/(N-1)
    
    std = np.sqrt(variance)
    
    std_mean = std/np.sqrt(N)
    
    print(f"mean = {mean}, variance = {variance}, std = {std}, std mean = {std_mean}")
    
    return

if __name__ == "__main__":
  main ()