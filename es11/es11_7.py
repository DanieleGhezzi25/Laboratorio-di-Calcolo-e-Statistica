# Least Squares with parabolic trend

from iminuit import Minuit
from iminuit.cost import LeastSquares
import module_randomGen as gen
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chi2

def phi(x,a,b,c):
    return a*x**2 + b*x + c

def display(my_minuit):
   
    for par, val, err in zip (my_minuit.parameters, my_minuit.values, my_minuit.errors) :
        print(f'{par} = {val:.3f} ± {err:.3f}')
    
    print (my_minuit.covariance)
    print (my_minuit.covariance.correlation())
    
    print ('Value of Q2: ', my_minuit.fval)
    print ('Number of degrees of freedom: ', my_minuit.ndof)
    print ('Associated p-value: ', 1. - chi2.cdf (my_minuit.fval, df = my_minuit.ndof))
    
    return

def main():
    
    a = -3
    b = +4
    c = +3
    N = 20
    xmin = -10
    xmax = 10
    sigma = 3
    
    x_coord = gen.UNIF_generation(xmin, xmax, N)
    epsilon_list = gen.CLT_generation(0, sigma, N)
    y_coord = []
    for i in range(N):
        y_coord.append(phi(x_coord[i],a,b,c)+epsilon_list[i])
    
    sigma_y = sigma*np.ones(N)
    
    least_squares = LeastSquares(x_coord, y_coord, sigma_y, phi)
    my_minuit = Minuit(least_squares, a=0, b=0, c=0)
    my_minuit.migrad()
    my_minuit.hesse()
    
    display(my_minuit)
    
    Q_squared = 0.
    a_fit = my_minuit.values[0]
    b_fit = my_minuit.values[1]
    c_fit = my_minuit.values[2] 
    for i in range(N):
        Q_squared += (y_coord[i] - a_fit*x_coord[i]**2 - b_fit*x_coord[i] - c_fit)**2/(sigma_y[i])**2
    print(f'My Q2: {Q_squared}')
    
    fig, ax = plt.subplots(1,1)
    x_plot = np.linspace(xmin,xmax,10000)
    y_plot = phi(x_plot, a_fit, b_fit, c_fit)
    ax.plot(x_plot, y_plot, label='Fit', color='red')
    ax.errorbar(x_coord, y_coord, xerr=0, yerr=sigma_y, capsize=5, marker='.',color='black', ls='None')
    ax.set_title('Quadratic Fit')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()
    ax.grid(color='black', linestyle='--', linewidth=0.5, alpha=0.5) 
    
    plt.show()
    
    return

if __name__ == "__main__":
    main()