# Insert the calculation of the integral from the previous exercise into a loop that, as the number N 
# of generated points varies, displays the value of the integral and its uncertainty.
# Plot the trends of the integral value and its uncertainty as N varies on a logarithmic scale.

import module_randomGen as gen
import numpy as np
import matplotlib.pyplot as plt

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
    N = 500
    N_times = 6
    
    N_list = []
    integral_list = []
    uncertainty_list = []
    
    for i in range(N_times):
        
        N_list.append(N)
        values = CrudeMC_integral(xmin, xmax, N, f)
        integral_list.append(values[0])
        uncertainty_list.append(values[1])
        
        N = int(N*np.log(N))
    
    fig, ax = plt.subplots(1,2)
    
    ax[0].plot(N_list, integral_list, color='blue', marker='o')
    ax[0].set_title('Integral value')
    ax[0].set_xlabel('N')
    ax[0].set_ylabel('Integral value')
    ax[0].set_xscale('log')
    ax[0].grid(color='black', linestyle='--', linewidth=0.5, alpha=0.5)
    
    ax[1].plot(N_list, uncertainty_list, color='red', marker='o')
    ax[1].set_title('Uncertainty Value')
    ax[1].set_xlabel('N')
    ax[1].set_ylabel('Integral error')
    ax[1].set_xscale('log')
    ax[1].grid(color='black', linestyle='--', linewidth=0.5, alpha=0.5)
    
    plt.show()
    
    return
    
if __name__ == "__main__":
    main()