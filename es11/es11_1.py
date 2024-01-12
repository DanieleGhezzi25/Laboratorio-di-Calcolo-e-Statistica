# After defining, in a dedicated library, a linear function with two parameters:
# Write a program that generates a set of 10 pairs such that the points are randomly distributed 
# along the horizontal axis between 0 and 10, and the points are constructed using the formula.
# Plot the obtained sample, including the expected error bars.
 
import module_randomGen as gen
import numpy as np
import matplotlib.pyplot as plt

def phi(x, m, q):
    # linear function
    return m*x + q

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
    
    fig, ax = plt.subplots(1,1)
    ax.errorbar(x_coord, y_coord, xerr=0, yerr=sigma, capsize=3, marker='.', color='black', ls='None')
    
    plt.show()
    
    return

if __name__ == "__main__":
    main()