# Perform the previous exercise using a recursive function.

import numpy as np
import time

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

def recursive_bisection(xmin,xmax,function,precision):
    
    x_average = (xmin+xmax)/2
    if ((xmax - xmin) < precision):
        return x_average
    if (function(x_average)*function(xmin)) > 0:
        recursive_bisection(x_average,xmax,function,precision)
    else:
        recursive_bisection(xmin,x_average,function,precision)   

def f(x):
    return np.cos(x)

def main():
    
    xmin = 0
    xmax = 4
    precision = 0.00000001
    
    start1 = time.time()
    zero1 = bisection(xmin, xmax, f, precision)
    end1 = time.time()
    print(f'{zero1}, time = {1000*(end1-start1):.9f} ms')
    
    start2 = time.time()
    zero2 = recursive_bisection(xmin, xmax, f, precision)
    end2 = time.time()
    print(f'{zero2}, time = {1000*(end2-start2):.9f} ms')
    
    return

if __name__ == "__main__":
  main ()