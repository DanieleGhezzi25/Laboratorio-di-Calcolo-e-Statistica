# Insert the calculation of the integral from the previous exercise into a loop that, as the number N 
# of generated points varies, displays the value of the integral and its uncertainty.
# Use a scatter plot to visualize the trends of the integral value and its uncertainty as N varies on a logarithmic scale.

import numpy as np
import random as rand
import matplotlib.pyplot as plt

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
    p = n_counts/N
    integral_value = A*p
    integral_uncertainty = np.sqrt((A**2/N)*(p*(1-p)))
    return integral_value, integral_uncertainty

def HoM_integral_sine(N_points):
    positive_area, sigma_pos = HoM_integral(0,np.pi, 0,1, N=N_points, function=f)
    negative_area_tilde, sigma_neg = HoM_integral(np.pi,2*np.pi, -1,0, N=N_points, function=f)
    negative_area = (np.pi*1) - negative_area_tilde
    integral_value = positive_area-negative_area
    integral_uncertainty = np.sqrt(sigma_pos**2 + sigma_neg**2)
    return integral_value, integral_uncertainty
    
def main():
    
    N_points = 100
    integral_list = []
    sigma_list = []
    N_list = []
    
    for i in range(6):
        results = HoM_integral_sine(N_points)
        integral_list.append(results[0])
        sigma_list.append(results[1])
        N_list.append(N_points)
        N_points = int(N_points*np.log(N_points))
        
    
    print(results)
    
    # Plots
    fig, ax = plt.subplots(1,2)
    
    ax[0].scatter(integral_list, sigma_list, color='red')
    ax[0].set_title('Integral value and its error on log scale')
    ax[0].set_xlabel('Integral values')
    ax[0].set_ylabel('Integral errors')
    ax[0].set_yscale('log')
    ax[0].grid(color='black', linestyle='--', linewidth=0.5, alpha=0.5)
    
    ax[1].scatter(N_list, sigma_list, color='red')
    ax[1].set_title('Number of points evaluated and integral error on log scale')
    ax[1].set_xlabel('Points')
    ax[1].set_ylabel('Integral errors')
    ax[1].set_xscale('log')
    ax[1].set_yscale('log')
    ax[1].grid(color='black', linestyle='--', linewidth=0.5, alpha=0.5)
    
    plt.show()
    
    return 

if __name__ == "__main__":
  main ()