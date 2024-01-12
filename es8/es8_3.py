# Use the stats class developed during the previous Lectures to compare the standard deviation of the mean 
# calculated for each individual toy with the standard deviation of the sample of means.

import sys
import module_randomGen as gen
import module_stats as st
import numpy as np

def main():
    
    # Toy experiment with Poissonian Distribution
    
    if len(sys.argv) < 3:
        print('Usage', sys.argv[0], 'N_toys N_max')
        exit()
        
    N_toys = int(sys.argv[1])
    N_max = int(sys.argv[2])
    
    toys_means = []
    toys_std_means = []
    poiss_mean = 5
    
    for i in range(N_toys):
        poissonian_distribution = gen.POISSON_generation(poiss_mean, N_max)
        poissonian_distribution_stats = st.stats(array = poissonian_distribution)
        toys_std_means.append(poissonian_distribution_stats.return_std_mean())
        toys_means.append(poissonian_distribution_stats.return_mean())
    
    toys_means_stats = st.stats(array = toys_means)
    
    print(toys_std_means)
    print(f'Toy std mean: {toys_means_stats.return_std_mean()}')
        
    return

if __name__ == "__main__":
  main ()
