# Write a program that, given a number N_max, generates N_toys toy experiments, each containing a sample of 
# N_max events following a chosen distribution, and calculates their mean.

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
    
    print(toys_means)
    print(np.mean(toys_means))
        
    return

if __name__ == "__main__":
  main ()
