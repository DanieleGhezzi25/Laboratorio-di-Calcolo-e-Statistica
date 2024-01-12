# Use the bisection method to find the two points τ - στ and τ + στ related to Exercise 1.
# Plot the log-likelihood profile, the estimator values, and the confidence interval along with 
# the horizontal segment used for its determination.

import numpy as np
import module_randomGen as gen
import matplotlib.pyplot as plt

def exp_function(tau, x):
    return (1/tau)*np.exp(-x/tau)

def exp_likelihood(tau, exp_values):
    exp_probabilities = exp_function(tau, np.array(exp_values))
    return float(np.prod(exp_probabilities))

def exp_loglikelihood(tau, exp_values):
    exp_probabilities = exp_function(tau, np.array(exp_values))
    logarithms = np.log(exp_probabilities)
    return float(np.sum(logarithms))

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
        
        width = abs (x1-x0)             
                                   
    return (x0 + x1) / 2

def LLR(likelihood, theta, theta_hat, sample):
    return np.log(likelihood(theta,sample)/(likelihood(theta_hat,sample)))


def intersection_LLR(likelihood, sample, xmin, xmax, theta_hat, ylevel=0.5, prec = 0.0001):
    
    # uses the ratio between the likelihood function and its maximum value (LLR)
    
    def ll_prime(x): 
        # this is the function translated to find the zeros
        #return LLR(likelihood, x, theta_hat, sample) - ylevel
        return -LLR(likelihood, x, theta_hat, sample) + LLR(likelihood, theta_hat, theta_hat, sample) - ylevel

    if xmin == 0:
        xmin = xmin + 0.01

    x_average = xmin
    while xmax - xmin > prec:
        x_average = (xmin+xmax)/2
        if ll_prime(x_average)*ll_prime(xmin) > 0:
            xmin = x_average
        else: # function(x_average)*function(xmax) < 0
            xmax = x_average
    
    return x_average

def intersection_LL(loglikelihood, sample, xmin, xmax, theta_hat, ylevel=0.5, prec = 0.0001):
    
    def ll_prime(x):
        return (loglikelihood(x, sample) - loglikelihood(theta_hat, sample) + ylevel)

    if xmin == 0:
        xmin = xmin + 0.01
    
    x_average = xmin
    while xmax - xmin > prec:
        x_average = (xmin+xmax)/2
        if ll_prime(x_average)*ll_prime(xmin) > 0:
            xmin = x_average
        else: # function(x_average)*function(xmax) < 0
            xmax = x_average
    
    return x_average

# -------------------------------------------------------------- #

def main():
    
    tau = 5
    N = 200
    toy = gen.INV_generation_exponential(tau, N)        
    
    x0 = 0
    x1 = 10
    
    estimator = sezioneAureaMax_LL(exp_loglikelihood, toy, x0, x1)
    #uncertainty_minus = intersection_LLR(exp_likelihood, toy, x0, estimator+1, estimator, ylevel=0.5)
    #uncertainty_plus = intersection_LLR(exp_likelihood, toy, estimator-1, x1, estimator, ylevel=0.5)
    uncertainty_minus = intersection_LL(exp_loglikelihood, toy, x0, estimator, estimator, ylevel=0.5)
    uncertainty_plus = intersection_LL(exp_loglikelihood, toy, estimator, x1, estimator, ylevel=0.5)
    
    uncertainty = (uncertainty_plus - uncertainty_minus)/2
    
    tau_coord = np.arange(0.1, 10, 0.1)
    prob_coord_l = []
    prob_coord_ll = []
    uncer_coord_ll = []
    for i in tau_coord:
        prob_coord_ll.append(exp_loglikelihood(i, toy))
        prob_coord_l.append(exp_likelihood(i, toy))
        uncer_coord_ll.append(exp_loglikelihood(estimator, toy) - 0.5)
    
    print('===================')
    
    print('Mean:')
    print(estimator)
    print(np.mean(toy))
    
    print('===================')
    
    print('Std:')
    print(uncertainty)
    print(tau/np.sqrt(N))
    
    fig, ax = plt.subplots(1,2)
    ax[0].plot(tau_coord, prob_coord_l, color='green')
    ax[0].plot(estimator, exp_likelihood(estimator, toy), 'bo')
    ax[0].set_title('Likelihood')
    ax[0].set_xlabel('tau')
    ax[0].set_ylabel('probability')
    ax[0].grid(color='black', linestyle='--', linewidth=0.5, alpha=0.5) 
    
    ax[1].plot(tau_coord, prob_coord_ll, color='red')
    ax[1].plot(estimator, exp_loglikelihood(estimator, toy), 'bo')
    ax[1].plot(tau_coord, uncer_coord_ll, color='blue')
    ax[1].set_title('logLikelihood')
    ax[1].set_xlabel('tau')
    ax[1].set_ylabel('probability')
    ax[1].grid(color='black', linestyle='--', linewidth=0.5, alpha=0.5) 
    
    plt.show()
    
    return

if __name__ == "__main__":
    main()