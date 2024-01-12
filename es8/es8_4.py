# Use two scatter plots to compare the evolution of the standard deviation of the mean calculated for each 
# individual toy with the standard deviation of the sample of means as the number of events 
# generated in a single toy experiment varies.

import sys
import module_randomGen as gen
import module_stats as st
import numpy as np
import matplotlib.pyplot as plt

def main():
    
    # Toy experiment with Poissonian Distribution
    
    if len(sys.argv) < 4:
        print('Usage', sys.argv[0], 'N_toys N_max1 N_max2')
        exit()
        
    N_toys = int(sys.argv[1])
    N_max1 = int(sys.argv[2])
    N_max2 = int(sys.argv[3])
    
    poiss_mean = 5
    deltaN = abs(N_max2 - N_max1)/N_toys
    
    toys_means = []
    toys_std_means = []
    for i in range(N_toys):
            N = N_max1
            poissonian_distribution1 = gen.POISSON_generation(poiss_mean, N)
            poissonian_distribution_stats1 = st.stats(array = poissonian_distribution1)
            toys_std_means.append(poissonian_distribution_stats1.return_std_mean())
            toys_means.append(poissonian_distribution_stats1.return_mean())
            N += deltaN
    
    tot_stats = st.stats(array = toys_means)
    
    # Plots
    fig, ax = plt.subplots(1,2)
    
    ax[0].scatter(toys_means, toys_std_means, color='black', marker='o', s=50)
    ax[0].set_title('Toys with less number of events')
    ax[0].set_xlabel('Toys means')
    ax[0].set_ylabel('Toys std means')
    ax[0].grid(color='black', linestyle='--', linewidth=0.5, alpha=0.5)
    ax[0].set_xlim([np.min(toys_means)-np.min(toys_means)*0.05, np.max(toys_means)+np.max(toys_means)*0.05])
    ax[0].set_ylim([np.min(toys_std_means)-np.min(toys_std_means)*0.05, np.max(toys_std_means)+np.max(toys_std_means)*0.05])
    
    ax[1].scatter(tot_stats.return_mean(), tot_stats.return_std_mean(), color='black', marker='o', s=50)
    ax[1].set_title('Toy Experiment')
    ax[1].set_xlabel('Toy mean')
    ax[1].set_ylabel('Toy std mean')
    ax[1].grid(color='black', linestyle='--', linewidth=0.5, alpha=0.5)
    #ax[1].set_xlim([np.min(toys_means)-np.min(toys_means)*0.05, np.max(toys_means)+np.max(toys_means)*0.05])
    #ax[1].set_ylim([np.min(toys_std_means)-np.min(toys_std_means)*0.05, np.max(toys_std_means)+np.max(toys_std_means)*0.05])
    
    
    plt.show()
    
    return

if __name__ == "__main__":
  main ()
