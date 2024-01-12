# Add to the previous program a histogram that visualizes the distribution of means across the toy experiments.

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
    poiss_mean = 5
    
    for i in range(N_toys):
        poissonian_distribution = gen.POISSON_generation(poiss_mean, N_max)
        toys_means.append(np.mean(poissonian_distribution))
    
    toys_means_stats = st.stats(array = toys_means)
    toys_means_stats.print_stats()
    toys_means_stats.hist()
        
    return

if __name__ == "__main__":
  main ()