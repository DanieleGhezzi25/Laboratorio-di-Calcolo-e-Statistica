# Using the toy experiments technique, generate 10,000 fit experiments 
# with the model studied in the previous exercises and fill a histogram with the obtained 
# values of Q-squared.
# Compare the expected value of Q-squared obtained from the
# toy experiments with the degrees of freedom of the problem.

from iminuit import Minuit
from iminuit.cost import LeastSquares
import module_randomGen as gen
import module_stats as st
import numpy as np
import matplotlib.pyplot as plt

def phi(x, m, q):
    return (m*x) + q

def Q_squared(m,q,N,sigma):
    x_coord = gen.UNIF_generation(0, 10, N)
    epsilon_list = np.random.normal(loc=0., scale=sigma, size=N)
    y_coord = []
    for i in range(N):
        y_coord.append(phi(x_coord[i],m,q) + epsilon_list[i])
    
    least_squares = LeastSquares(x_coord, y_coord, sigma, phi)
    my_minuit = Minuit(least_squares, m=0, q=0)
    my_minuit.migrad()
    
    return my_minuit.fval

def main():
    
    m = 2
    q = 1
    N = 10
    sigma = 1
    
    Q_squared_list = []
    for i in range(10000):
        Q_squared_list.append(Q_squared(m,q,N,sigma))
    
    Q_squared_stats = st.stats(array=Q_squared_list)
    Q_squared_stats.print_stats()
    Q_squared_stats.hist()
    
    return

if __name__ == "__main__":
    main()
    