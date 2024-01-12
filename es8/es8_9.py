# Use the hit-or-miss method to estimate the integral underlying a Gaussian probability distribution with μ=0 and σ=1 
# within a generic interval [a,b].
# Calculate the integral contained within the intervals [-kσ, kσ] as k varies from 1 to 5.

import random as rand
import numpy as np
from scipy.stats import norm

def HoM_integral(xmin,xmax,ymin,ymax,N,function):
    
    A = (xmax-xmin)*(ymax-ymin)
    n_counts = 0
    
    for i in range(N):
        x = rand.uniform(xmin,xmax)
        y = rand.uniform(ymin, ymax)
        if y <= function(x):
            n_counts += 1
    
    p = n_counts/N
    integral_value = A*p
    integral_uncertainty = np.sqrt((A**2/N)*(p*(1-p)))
    
    return integral_value, integral_uncertainty

def f(x):
    return norm.pdf(x)

# ------------------------------------ #

def main():
    
    k = int(input('Insert k range: '))
    
    ymin = 0
    ymax = 1
    N = 10000
    
    print(HoM_integral(-k,k,ymin,ymax,N,f))
    
    return

if __name__ == "__main__":
    main()