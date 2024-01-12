# Determine the zero of the function g(x) = cos(x) using the bisection method in the interval (0, 4).

import numpy as np

def bisection(xmin, xmax, function, precision):
    
    # checks
    if xmin > 0 or xmax < 0:
        raise ValueError('xmin must be negative and xmax must be positive.')
    
    x_average = xmin
    while xmax - xmin > precision:
        x_average = (xmin+xmax)/2
        if function(x_average)*function(xmin) > 0:
            xmin = x_average
        else: # function(x_average)*function(xmax) < 0
            xmax = x_average
    
    return x_average

def f(x):
    return np.cos(x)

def main():
    xmin = 0
    xmax = 4
    precision = 0.001
    zero = bisection(xmin, xmax, f, precision)
    print(zero)
    return

if __name__ == "__main__":
  main ()