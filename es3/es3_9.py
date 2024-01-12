# Use the Python scipy.stat.norm object to determine the area of a normal distribution 
# of its tails outside the range included within an interval of 1, 2, 3, 4, and 5 standard deviations around its mean

import numpy as np
from scipy.stats import norm
from scipy.integrate import quad

def main():
    range = 1
    internal_area, error = quad(norm.pdf, -range, range)
    external_area = 1- internal_area
    print (external_area)
    return

if __name__ == "__main__":
  main ()