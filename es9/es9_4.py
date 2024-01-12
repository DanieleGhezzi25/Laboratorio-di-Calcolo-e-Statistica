# Write a function likelihood that calculates the likelihood as the parameter t0 varies, 
# for a sample of pseudo-random events generated according to the instructions of Exercise 1.
# How does the result depend on the number of events in the sample?

import module_randomGen as gen
import numpy as np

def exp_function(tau, x):
    return (1/tau)*np.exp(-x/tau)

def exp_likelihood(tau, N):
    exp_values = gen.INV_generation_exponential(tau,N)
    exp_probabilities = exp_function(tau, np.array(exp_values))
    return np.prod(exp_probabilities)

def main():
    
    tau1 = 1
    tau2 = 5
    tau3 = 10
    
    N1 = 100
    N2 = 1000
    N3 = 10000
    
    print(f'Tau = {tau1}, N = {N2}  ===>  p = {exp_likelihood(tau1, N1)}')
    print(f'Tau = {tau2}, N = {N2}  ===>  p = {exp_likelihood(tau2, N2)}')
    print(f'Tau = {tau3}, N = {N2}  ===>  p = {exp_likelihood(tau3, N3)}')
    print('------------------------------------------------')
    print(f'Tau = {tau2}, N = {N1}  ===>  p = {exp_likelihood(tau2, N1)}')
    print(f'Tau = {tau2}, N = {N2}  ===>  p = {exp_likelihood(tau2, N2)}')
    print(f'Tau = {tau2}, N = {N3}  ===>  p = {exp_likelihood(tau2, N3)}')
    
    return

if __name__ == '__main__':
    main()
    
    
