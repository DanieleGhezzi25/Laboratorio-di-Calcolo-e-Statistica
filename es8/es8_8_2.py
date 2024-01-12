# Overlay this behavior with the one obtained from completing Exercise 8.6.

import module_randomGen as gen
import random as rand
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------ #

def CrudeMC_integral(xmin, xmax, N, function):

    # generating points that gives the sample mean and std's mean of the function we want to integrate 
    sample_x = np.array(gen.UNIF_generation(xmin, xmax, N=N))
    sample_y = function(sample_x)
    
    sample_mean = np.mean(sample_y)
    sample_variance = np.var(sample_y, ddof=1)
    
    integral_value = (xmax-xmin)*sample_mean
    integral_uncertainty = np.sqrt(sample_variance/N) # this is the std_mean
    
    return integral_value, integral_uncertainty

# ------------------------------------ #

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

# ------------------------------------ #

def f(x):
    return np.sin(x)

# ------------------------------------ #

def main():
    
    xmin = 0
    xmax = np.pi
    N = 500
    N_times = 4
    
    N_list = []
    integral_list_mc = []
    uncertainty_list_mc = []
    integral_list_hom = []
    uncertainty_list_hom = []
    
    for i in range(N_times):
        
        N_list.append(N)
        
        integral_list_mc_tmp = []
        uncertainty_list_mc_tmp = []
        integral_list_hom_tmp = []
        uncertainty_list_hom_tmp = []
        
        for j in range(25):
            values_mc = CrudeMC_integral(xmin, xmax, N, f)
            integral_list_mc_tmp.append(values_mc[0])
            uncertainty_list_mc_tmp.append(values_mc[1])

            values_hom = HoM_integral(xmin, xmax, ymin=0, ymax=1, N=N, function=f)
            integral_list_hom_tmp.append(values_hom[0])
            uncertainty_list_hom_tmp.append(values_hom[1])
            
        integral_list_mc.append(np.mean(integral_list_mc_tmp))
        uncertainty_list_mc.append(np.mean(uncertainty_list_mc_tmp))
        integral_list_hom.append(np.mean(integral_list_hom_tmp))
        uncertainty_list_hom.append(np.mean(uncertainty_list_hom_tmp))
        
        N = int(N*np.log(N))
    
    fig, ax = plt.subplots(1,2)
    
    ax[0].plot(N_list, integral_list_mc, color='blue', marker='o', label='Crude MonteCarlo')
    ax[0].plot(N_list, integral_list_hom, color='red', marker='o', label='Hit or Miss')
    ax[0].set_title('Integral Values')
    ax[0].set_xlabel('N')
    ax[0].set_ylabel('Integral value')
    ax[0].set_xscale('log')
    ax[0].legend()
    ax[0].grid(color='black', linestyle='--', linewidth=0.5, alpha=0.5)
    
    ax[1].plot(N_list, uncertainty_list_mc, color='blue', marker='o', label='Crude MonteCarlo')
    ax[1].plot(N_list, uncertainty_list_hom, color='red', marker='o', label='Hir or Miss')
    ax[1].set_title('Uncertainty Values')
    ax[1].set_xlabel('N')
    ax[1].set_ylabel('Integral error')
    ax[1].set_xscale('log')
    ax[1].legend()
    ax[1].grid(color='black', linestyle='--', linewidth=0.5, alpha=0.5)
    
    plt.show()
    
    return
    
if __name__ == "__main__":
    main()