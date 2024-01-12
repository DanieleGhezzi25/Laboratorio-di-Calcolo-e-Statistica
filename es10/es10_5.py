# Graphically show that as the available sample size increases, the profile of the logarithm of the likelihood 
# function becomes narrower.
# To simplify visualization, use the logarithm of the ratio between the likelihood function and its maximum value LLR

import numpy as np
import module_randomGen as gen
import matplotlib.pyplot as plt

def exp_function(tau, x):
    if tau == 0:
        return 1
    x = np.array(list(filter(lambda t: t>=0, x)))
    return np.longdouble((1/tau)*np.exp(-x/tau))

def exp_likelihood(tau, exp_values):
    exp_probabilities = exp_function(tau, np.array(exp_values))
    return np.longdouble(np.prod(exp_probabilities))

def exp_loglikelihood(tau, exp_values):
    exp_probabilities = exp_function(tau, np.array(exp_values))
    logarithms = list(filter(lambda x: x!=0, np.longdouble(np.log(exp_probabilities))))
    return np.longdouble(np.sum(logarithms))

def sezioneAureaMax_LL (loglikelihood, sample, x0, x1, prec = 0.0001):
    
    r = (np.sqrt(5)-1)/2
    
    width = abs (x1 - x0)
     
    while (width > prec):
        x2 = x0 + r * (x1 - x0) 
        x3 = x0 + (1. - r) * (x1 - x0)  
          
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
    N = 280
    toy = gen.INV_generation_exponential(tau, N)
    
    x0 = 0
    x1 = 10
    
    estimator = sezioneAureaMax_LL(exp_loglikelihood, toy, x0, x1)
    
    print(estimator)
    print(np.mean(toy))
    
    tau_coord = np.arange(0.1, 10, 0.1)
    prob_coord_ll = []
    for i in tau_coord:
        prob_coord_ll.append(np.log(np.longdouble(exp_likelihood(i, toy)/np.longdouble(exp_likelihood(estimator, toy)))))
    
    fig, ax = plt.subplots(1,1)
    ax.plot(tau_coord, prob_coord_ll, color='red')
    ax.set_title('logLikelihood')
    ax.set_xlabel('tau')
    ax.set_ylabel('probability')
    ax.grid(color='black', linestyle='--', linewidth=0.5, alpha=0.5) 
    
    plt.show()
    
    return

if __name__ == "__main__":
    main()
