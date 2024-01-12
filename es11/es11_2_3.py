# Use the iMinuit library to perform a fit on the simulated sample.
# Check if the fit was successful.
# Print the values of the determined parameters and their sigmas on the screen.

from iminuit import Minuit
from iminuit.cost import LeastSquares
import module_randomGen as gen
import numpy as np
from scipy.stats import chi2

def phi(x, m, q):
    # linear function
    return m*x + q

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
    
    m = 2
    q = 1
    N = 10
    sigma = 3
    
    x_coord = gen.UNIF_generation(0, 10, N)
    epsilon_list = gen.CLT_generation(0, sigma, N)
    y_coord = []
    for i in range(N):
        y_coord.append(phi(x_coord[i],m,q)+epsilon_list[i])
    
    sigma_y = sigma*np.ones(N)
    
    least_squares = LeastSquares(x_coord, y_coord, sigma_y, phi)
    my_minuit = Minuit(least_squares, m=0, q=0)
    my_minuit.migrad()
    my_minuit.hesse()
    
    display(my_minuit)
    
    Q_squared = 0.
    m_fit = my_minuit.values[0]
    q_fit = my_minuit.values[1] 
    for i in range(N):
        Q_squared += (y_coord[i] - m_fit*x_coord[i] - q_fit)**2/(sigma_y[i])**2
    print(f'My Q2: {Q_squared}')
    
    return

if __name__ == "__main__":
    main()
