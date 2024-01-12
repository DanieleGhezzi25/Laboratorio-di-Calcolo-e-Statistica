# What is the probability that ten measurements of the same quantity expected to be Gaussian fall 
# within an interval of 1 standard deviation width around the mean?

import numpy as np
from scipy.integrate import quad
from scipy.stats import norm

def main():
    std = 1
    area, error = quad(norm.pdf, -std, std)
    prob = (area**10)*100
    print(f"Probability = {prob:.2f}%")
    return

if __name__ == "__main__":
  main () 

