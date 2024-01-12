# Study the behavior of the shape of the log-likelihood as a function of the number of events 
# comprising the generated sample.

import module_randomGen as gen
import numpy as np
import matplotlib.pyplot as plt

def exp_function(tau, x):
    return (1/tau)*np.exp(-x/tau)

def exp_likelihood(tau, exp_values):
    exp_probabilities = exp_function(tau, np.array(exp_values))
    exp_likelihood = np.prod(exp_probabilities) 
    return exp_likelihood

def main():
    
    N = 200
    
    tau_fixed = 3
    exp_values = gen.INV_generation_exponential(tau_fixed,N)
    
    tau_coord = np.arange(0.01, 10, 0.1)
    prob_coord = []
    
    for tau in tau_coord:
        prob_coord_tmp = []
        for i in range(100):
            prob_coord_tmp.append(exp_likelihood(tau,exp_values))
        prob_coord.append(np.mean(prob_coord_tmp))
        
    prob_coord_log = np.log(prob_coord)
    
    fig, ax = plt.subplots(1,2)
    
    ax[0].plot(tau_coord, prob_coord, color='r', label='Likelihood')
    ax[0].set_title('Likelihood')
    ax[0].set_xlabel('tau')
    ax[0].set_ylabel('probability')
    ax[0].legend()
    ax[0].grid(color='black', linestyle='--', linewidth=0.5, alpha=0.5) 
    
    ax[1].plot(tau_coord, prob_coord_log, color='r', label='logLikelihood')
    ax[1].set_title('logLikelihood')
    ax[1].set_xlabel('tau')
    ax[1].set_ylabel('probability')
    ax[1].legend()
    ax[1].grid(color='black', linestyle='--', linewidth=0.5, alpha=0.5) 
    
    plt.show()
    
    return
    
if __name__ ==  "__main__":
    main()
    