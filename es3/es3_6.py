# Write a python library which, given the name of a text file containing a sample of events as input, 
# is able to read the sample and save it in a numpy array, then calculate its mean, variance, standard deviation, 
# standard deviation from the mean, display the sample in a histogram with an appropriately chosen definition range and bin number. 
# Write a test program for the created library.

import numpy as np
from matplotlib import pyplot as plt
import module_es3_6 as mod

def main():
    mod.sample_hist('eventi_gauss.txt')
    return

if __name__ == "__main__":
  main ()