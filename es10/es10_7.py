# Using the toy experiments technique, plot the probability distribution of the τ estimator.
# Overlay the generated histogram with the plot of the estimator and the confidence interval 
# found in the previous exercise.
# Compare the value of στ obtained in the previous exercise with the one calculated from the distribution
# of the numbers saved in the list.

import numpy as np
import module_randomGen as gen
import module_stats as st
import matplotlib.pyplot as plt

def sturges(N):
    return int(np.ceil(1+3.322*np.log(N)))

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
    
    x0 = 0
    x1 = 10
    
    number_of_toys = 2000
    estimator_list = []
    uncertainty_list = []
    for i in range(number_of_toys):
        toy = gen.INV_generation_exponential(tau, N)     
        estimator_list.append(sezioneAureaMax_LL(exp_loglikelihood, toy, x0, x1))
        uncertainty_minus = intersection_LL(exp_loglikelihood, toy, x0, estimator_list[i], estimator_list[i], ylevel=0.5)
        uncertainty_plus = intersection_LL(exp_loglikelihood, toy, estimator_list[i], x1, estimator_list[i], ylevel=0.5)
        uncertainty_list.append((uncertainty_plus - uncertainty_minus)/2)
    
    estimators = st.stats(array=estimator_list)
    uncertainties = st.stats(array=uncertainty_list)
    
    theta_hat = estimators.return_mean()
    toys_uncertainty = uncertainties.return_mean()
    
    # generation of 1 toy experiment for comparison with the others
    toy = gen.INV_generation_exponential(tau,N)
    toy_hat = sezioneAureaMax_LL(exp_loglikelihood, toy, x0, x1)
    uncertainty_minus = intersection_LL(exp_loglikelihood, toy, x0, toy_hat, toy_hat, ylevel=0.5)
    uncertainty_plus = intersection_LL(exp_loglikelihood, toy, toy_hat, x1, toy_hat, ylevel=0.5)
    uncertainty = (uncertainty_plus - uncertainty_minus)/2
    
    print('===================')
    
    print('Toys Mean:')
    print(theta_hat)
    print('Toys Std:')
    print(toys_uncertainty)
    
    print('===================')
    
    print('Random Toy mean:')
    print(toy_hat)
    print('Random Toy Std:')
    print(uncertainty)
    
    print('===================')
    
    fig, ax = plt.subplots(1,1)
    ax.hist(estimator_list, sturges(len(estimator_list)), color='red')
    ax.set_title('Distribution of Theta Hat')
    
    # plot lines
    limits = ax.get_ylim()
    ax.plot([toy_hat, toy_hat], limits, label='Single Toy hat', color='black')
    ax.plot([uncertainty_minus, uncertainty_minus], limits, color='black', linestyle='dashed')
    ax.plot([uncertainty_plus, uncertainty_plus], limits, color='black', linestyle='dashed')
    ax.plot([theta_hat, theta_hat], limits, label='Toys Mean', color='green')
    
    ax.legend()
    
    ax.grid(color='black', linestyle='--', linewidth=0.5, alpha=0.5) 
    
    plt.show()
    
    return

if __name__ == "__main__":
    main()