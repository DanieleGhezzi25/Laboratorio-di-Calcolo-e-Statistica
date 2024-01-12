# Study the behavior of the shape of the log-likelihood as a function of the number of events 
# comprising the generated sample.

import module_randomGen as gen
import numpy as np
import matplotlib.pyplot as plt

def exp_function(tau, x):
    return (1/tau)*np.exp(-x/tau)

def exp_loglikelihood(tau, N):
    tau_fixed = 5
    exp_values = gen.INV_generation_exponential(tau,N)
    exp_probabilities = exp_function(tau_fixed, np.array(exp_values))
    exp_likelihood = np.prod(exp_probabilities)
    if exp_likelihood > 0:
        return np.log(exp_likelihood)
    else:
        return 0

def main():
    
    N = 10
    
    tau_coord = np.arange(0.1, 10, 0.1)
    prob_coord = []
    
    for tau in tau_coord:
        prob_coord_tmp = []
        for i in range(1000):
            prob_coord_tmp.append(exp_loglikelihood(tau,N))
        prob_coord.append(np.mean(prob_coord_tmp))

    plt.plot(tau_coord, prob_coord)
    
    plt.show()
    
if __name__ ==  "__main__":
    main()