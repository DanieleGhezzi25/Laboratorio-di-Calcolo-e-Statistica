# Implement the hit-or-miss integration method with the example function f(x) = sin(x).
# Write the algorithm that calculates the integral as function external to the main program, ensuring 
# it takes as input parameters the limits along the x and y axis, as well as the number of pseudo-random points to 
# generate.
# Make sure the algorithm returns a container with two elements: the first element is the value of the integral, 
# the second is its uncertainty

import numpy as np
import random as rand

def f(x):
    return np.sin(x)

def HoM_integral(xmin,xmax,ymin,ymax,N,function):
    A = (xmax-xmin)*(ymax-ymin)
    n_counts = 0
    for i in range(N):
        x = rand.uniform(xmin,xmax)
        y = rand.uniform(ymin, ymax)
        if y <= function(x):
            n_counts += 1
    print(n_counts)
    p = n_counts/N
    integral_value = A*p
    integral_uncertainty = np.sqrt((A**2/N)*(p*(1-p)))
    return integral_value, integral_uncertainty
    
def main():
    positive_area, sigma_pos = HoM_integral(0,np.pi, 0,1, N=10000, function=f)
    negative_area_tilde, sigma_neg = HoM_integral(np.pi,2*np.pi, -1,0, N=10000, function=f)
    
    negative_area = (np.pi*1) - negative_area_tilde
    
    integral_value = positive_area-negative_area
    integral_uncertainty = np.sqrt(sigma_pos**2 + sigma_neg**2)
    
    print(integral_value, integral_uncertainty)
    
    return 

if __name__ == "__main__":
  main ()