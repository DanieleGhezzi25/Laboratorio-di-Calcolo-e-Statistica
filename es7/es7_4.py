# Use the result from the previous exercise to calculate the statistics of a Poisson distribution varying the mean, 
# from 1 to 250 (how should you sample the interval?).
# Plot the obtained behavior of skewness and kurtosis as function of the Poisson mean.

import module_randomGen as gen
import matplotlib.pyplot as plt
import scipy.stats as st
import numpy as np

def main():
    
    N = 20
    
    mean_list = []
    skew_list = []
    kurt_list = []
    
    for mean in range(N):
        mean_list_tmp = []
        skew_list_tmp = []
        kurt_list_tmp = []
        for i in range(25):
            N_experiments = 2000
            poissonian_distribution = gen.POISSON_generation(mean, N_experiments)
            mean_list_tmp.append(mean)
            skew_list_tmp.append(st.skew(poissonian_distribution))
            kurt_list_tmp.append(st.kurtosis(poissonian_distribution))
        mean_list.append(np.mean(mean_list_tmp))
        skew_list.append(np.mean(skew_list_tmp))
        kurt_list.append(np.mean(kurt_list_tmp))

    x_coord = np.linspace(0,N,N)

    fig, ax = plt.subplots(nrows = 1, ncols = 3)
    
    ax[0].plot(x_coord, mean_list, 'bo-')
    ax[1].plot(x_coord, skew_list, 'bo-')
    ax[2].plot(x_coord, kurt_list, 'bo-')
    
    plt.show()
    
    return

if __name__ == "__main__":
  main ()