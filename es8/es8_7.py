# Implement the crude-MC integration method with the example function f(x) = sin(x).
# Write the algorithm that calculates the integral as a function external to the main program, 
# ensuring it takes as input parameters the limits along the x axis and the number of pseudo-random points to generate.
# Make sure the algorithm returns a container with two elements: the first element is the value of the integral, 
# the second is its uncertainty.

import module_randomGen as gen
import numpy as np

def CrudeMC_integral(xmin, xmax, N, function):

    # generating points that gives the sample mean and std's mean of the function we want to integrate 
    sample_x = np.array(gen.UNIF_generation(xmin, xmax, N=N))
    sample_y = function(sample_x)
    
    sample_mean = np.mean(sample_y)
    sample_variance = np.var(sample_y, ddof=1)
    
    integral_value = (xmax-xmin)*sample_mean
    integral_uncertainty = np.sqrt(sample_variance/N) # this is the std_mean
    
    return integral_value, integral_uncertainty

def f(x):
    return np.sin(x)


def main():
    
    xmin = 0
    xmax = 2*np.pi
    N = 10000
    N_times = 1000
    
    integral_list = []
    uncertainty_list = []
    
    for i in range(N_times):
        values = CrudeMC_integral(xmin,xmax,N,f)
        integral_list.append(values[0])
        uncertainty_list.append(values[1])
    
    print(f'{np.mean(integral_list)} ± {np.mean(uncertainty_list)}')    # ± = alt 2 4 1
        
    return

if __name__ == "__main__":
  main ()
