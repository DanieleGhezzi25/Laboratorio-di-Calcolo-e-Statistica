# Random Generation Functions.
# Includes the following generators: 
# 1. Uniform Distribution 2. Try and Catch Algorithm 3. Inverse Algorithm (for exponential function)
# 4. Central Limit Theorem Algorithm 5. Poissonian Distribution Algorithm

import numpy as np
from scipy import stats
import random

# -------------------------------------------------- #

def UNIF_generation(xmin, xmax, N):
    random_list = []
    for i in range(N):
        random_list.append(random.uniform(xmin, xmax))
    return random_list

# -------------------------------------------------- #

def TAC_generation(xmin, xmax, ymax, function, N=1):
    
    if N==1:
        x = random.uniform(xmin, xmax)
        y = random.uniform(0, ymax)
        while (y > function(x)):
            x = random.uniform(xmin, xmax)
            y = random.uniform(0, ymax)
        return x
    
    else:
        list = []
        for i in range(N):
            x = random.uniform(xmin, xmax)
            y = random.uniform(0, ymax)
            while (y > function(x)):
                x = random.uniform(xmin, xmax)
                y = random.uniform(0, ymax)
            list.append(x)
        return list

# -------------------------------------------------- #    

def INV_generation_exponential(tau, N=1):
    # the cdf is y = 1 - gamma*exp(-gamma*x)
    gamma = 1/tau
    if N == 1:
        y = random.uniform(0, 1)
        return (np.log(1-y))/(-gamma)
    else:
        y_array = np.array(UNIF_generation(0,1,N))
        return list((np.log(1-y_array))/(-gamma))

# -------------------------------------------------- #

def CLT_generation(mean, variance, N, number_of_variables):
    
    delta = np.sqrt(3*N*variance) # demonstrated
    interval_min = mean - delta
    interval_max = mean + delta
    random_gaussian_variables = []
    
    for j in range(number_of_variables):
        yi = 0
        for i in range(N):
            yi += random.uniform(interval_min, interval_max)
        random_gaussian_variables.append(yi/N)
    
    return random_gaussian_variables  

# -------------------------------------------------- #

def POISSON_generation(mean, N_experiments):

    t0 = 1
    t_counting = mean # because mean = lambda = t/t0
    poissonian_events = []
    
    for i in range(N_experiments):
        delta_t = 0
        countings = 0
        while (delta_t <= t_counting):
            delta_t += INV_generation_exponential(tau=t0)
            countings += 1
        poissonian_events.append(countings)
    
    return poissonian_events
