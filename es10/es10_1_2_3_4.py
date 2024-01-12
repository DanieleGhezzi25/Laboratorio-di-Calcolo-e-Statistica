# 1) Write a library of functions to determine the parameter τ of an exponential distribution from a list of numbers 
#    filled with pseudo-random numbers distributed according to an exponential probability density distribution.
#    Compare the result obtained with the mean of the numbers saved in the list.
#    How does the result depend on the initial interval passed to the sezione_aurea_max_LL function?
# 2) Plot the profile of the likelihood function and the point identified as its maximum.
# 3) Modify the sezione_aurea_max_LL function, adding the printing of the interval endpoint values at each iteration,
#    to observe the narrowing of the interval during program execution.

import numpy as np
import module_randomGen as gen
import matplotlib.pyplot as plt

def exp_function(tau, x):
    return (1/tau)*np.exp(-x/tau)

def exp_likelihood(tau, exp_values):
    exp_probabilities = exp_function(tau, np.array(exp_values))
    return np.prod(exp_probabilities)

def exp_loglikelihood(tau, exp_values):
    exp_probabilities = exp_function(tau, np.array(exp_values))
    logarithms = np.log(exp_probabilities)
    return np.sum(logarithms)

def sezioneAureaMax_LL (loglikelihood, sample, x0, x1, prec = 0.0001):
    
    r = (np.sqrt(5)-1)/2
    
    width = abs (x1 - x0)
     
    while (width > prec):
        x2 = x0 + r * (x1 - x0) 
        x3 = x0 + (1. - r) * (x1 - x0)  
      
        # si restringe l'intervallo tenendo fisso uno dei due estremi e spostando l'altro        
        if (loglikelihood(x3, sample) < loglikelihood(x2, sample)): 
            x0 = x3
            x1 = x1         
        else :
            x1 = x2
            x0 = x0          
        
        print(f'min = {x2}, max = {x3}')
        
        width = abs (x1-x0)             
                                   
    return (x0 + x1) / 2
# -------------------------------------------------------------- #

def main():
    
    tau = 5
    N = 100
    toy = gen.INV_generation_exponential(tau, N)
    
    tau_coord = np.arange(0.1, 10, 0.1)
    prob_coord_l = []
    prob_coord_ll = []
    for i in tau_coord:
        prob_coord_ll.append(exp_loglikelihood(i, toy))
        prob_coord_l.append(exp_likelihood(i, toy))
    
    x0 = 0
    x1 = 10
    
    estimator = sezioneAureaMax_LL(exp_loglikelihood, toy, x0, x1)
    
    print(estimator)
    print(np.mean(toy))
    
    fig, ax = plt.subplots(1,2)
    ax[0].plot(tau_coord, prob_coord_l, color='green')
    ax[0].plot(estimator, exp_likelihood(estimator, toy), 'bo')
    ax[0].set_title('Likelihood')
    ax[0].set_xlabel('tau')
    ax[0].set_ylabel('probability')
    ax[0].grid(color='black', linestyle='--', linewidth=0.5, alpha=0.5) 
    
    ax[1].plot(tau_coord, prob_coord_ll, color='red')
    ax[1].plot(estimator, exp_loglikelihood(estimator, toy), 'bo')
    ax[1].set_title('logLikelihood')
    ax[1].set_xlabel('tau')
    ax[1].set_ylabel('probability')
    ax[1].grid(color='black', linestyle='--', linewidth=0.5, alpha=0.5) 
    
    plt.show()
    
    return

if __name__ == "__main__":
    main()
