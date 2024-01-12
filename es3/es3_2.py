# Read the text file eventi_unif.txt:
# Print the first 10 positive elements to the screen.
# Count the number of events contained in the file.
# Determine the minimum and maximum values among the numbers saved in the file.

import numpy as np
from matplotlib import pyplot as plt

def main():
    sample = np.loadtxt('eventi_unif.txt')
    N = 10
    for i in range(N):
        print(sample[i])
    print(len(sample))
    max = np.max(sample)
    min = np.min(sample)
    print ('Maximum = ', max, 'Minimum =', min)
    return

if __name__ == "__main__":
  main ()