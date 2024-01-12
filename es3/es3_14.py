# What is the probability that ten measurements of the same counting experiment expected to be Poisson 
# distributed are all larger than the expected average number of events?

import numpy as np
from scipy.stats import poisson
from scipy.integrate import quad

def main():
    average = 5 # chosen by me
    x_coord = np.arange(0,10,1)
    probability = (1-poisson.cdf(x_coord,average)) # external area
    total_probability = (probability**10)*100
    print(f"Single probability = {probability:.2f}%")
    print(f"Total probability with 10 measurements = {total_probability:.2f}%")
    return

if __name__ == "__main__":
  main () 
