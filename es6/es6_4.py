# Determine the minimum of the function g(x) = x2 + 7.3x + 4 using the golden ratio search method 
# in the interval (-10, 10).

import numpy as np

def f(x):
    return x**2

def minimum_f(f, x0, x1, precision):
    
    if x0 > x1:
        raise ValueError
    
    r = (np.sqrt(5)-1)/2
    
    if (x1-x0) < precision:
        if f(x1) > f(x0):
            return x0
        else:
            return x1
    
    if f(x0) >= f(x1):
        x0 = x0 + r*(x1-x0)
    else:
        x1 = x0 + (1-r)*(x1-x0)
    
    return minimum_f(f, x0, x1, precision)
        

def main():
    
    xmin = -1
    xmax = 1
    precision = 0.000000000000000000000001
    
    print(f'The local minimum of x2 - 10x + 25 searched in {xmin,xmax} is {minimum_f(f, xmin, xmax, precision)} (precision = {precision}.)')
    
    return

if __name__ == "__main__":
  main ()