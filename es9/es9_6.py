# Study the behavior of the shape of the log-likelihood as a function of the number of events 
# comprising the generated sample.

import module_randomGen as gen
import numpy as np
import matplotlib.pyplot as plt

def exp_function(tau, x):
    return (1/tau)*np.exp(-x/tau)

def exp_loglikelihood(tau, N):
    exp_values = gen.INV_generation_exponential(tau,N)
    exp_probabilities = exp_function(tau, np.array(exp_values))
    exp_likelihood = np.prod(exp_probabilities)
    return np.log(exp_likelihood)

def main():
    
    N_list = []
    loglikelihood_list = []
    tau = 2
    N = 1
    
    for i in range(100):
        log_tmp = []
        for k in range(1000):
            log_tmp.append(exp_loglikelihood(tau,N)) 
        loglikelihood_list.append(np.mean(log_tmp))
        N_list.append(N)
        N += 5
    
    fig, ax = plt.subplots(1,1)
    
    ax.plot(N_list, loglikelihood_list, color='r', label='logLikelihood values')
    ax.set_title('logLikelihood values respect to N')
    ax.set_xlabel('N')
    ax.set_ylabel('logLikelihood values')
    ax.legend()
    ax.grid(color='black', linestyle='--', linewidth=0.5, alpha=0.5) 
    
    plt.show()
    
    return

if __name__ ==  "__main__":
    main()