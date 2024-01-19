# Insert the source code of the previous exercise into a loop that performs the comparison as the number of events considered for 
# the fit varies, from 20 to 10000, with a regular log-scale increment.
# 1) Use different plots to show the behavior of the parameters and their uncertainties as the number of events changes, 
#    for both types of estimators.
# 2) Add to the comparison the fit performed with the least squares method.
# 3) Which estimator is less biased at low statistics?

import numpy as np
import matplotlib.pyplot as plt
from iminuit.cost import ExtendedBinnedNLL, UnbinnedNLL, LeastSquares
from iminuit import Minuit
import scipy.stats as sci

# -------------------------------------------------------- #

def model_function(x, mu, sigma):
    return sci.norm.pdf(x,mu,sigma)

def cdf_model_function(bin_edges, N_events, mu, sigma):
    return N_events * sci.norm.cdf(bin_edges,mu,sigma)

def leastsq_model_function(x, N_events, mu, sigma, bin_width) :
    return N_events * sci.norm.pdf(x,mu,sigma) * bin_width

# -------------------------------------------------------- #

# Generating N number of events
true_mu = 0
true_sigma = 1
N_events = 20
N_f = 100000

list_mu_binned = []
list_sigma_binned = []
list_chi2_binned = []

list_mu_unbinned = []
list_sigma_unbinned = []
list_chi2_unbinned = []

list_mu_leastsq = []
list_sigma_leastsq = []
list_chi2_leastsq = []

N_list = []

while N_events < N_f:
    
    for j in range(5):
        
        list_mu_binned_tmp = []
        list_sigma_binned_tmp = []
        list_chi2_binned_tmp = []

        list_mu_unbinned_tmp = []
        list_sigma_unbinned_tmp = []
        list_chi2_unbinned_tmp = []

        list_mu_leastsq_tmp = []
        list_sigma_leastsq_tmp = []
        list_chi2_leastsq_tmp = []      
        
        data = np.random.normal(true_mu,true_sigma,N_events)

        # BINNED FIT
        bin_edges = 20
        bin_content, bin_edges = np.histogram(data, bin_edges) # number of event per bin
        my_cost_binned_func = ExtendedBinnedNLL(bin_content, bin_edges, cdf_model_function)
        my_minuit_binned = Minuit(my_cost_binned_func, N_events = N_events, mu = np.mean(data), sigma = np.std(data))
        my_minuit_binned.limits["mu","sigma"]=(0,None)
        my_minuit_binned.migrad()
        list_mu_binned_tmp.append(my_minuit_binned.values[1])
        list_sigma_binned_tmp.append(my_minuit_binned.values[2])
        list_chi2_binned_tmp.append(1. - sci.chi2.cdf(my_minuit_binned.fval, df = my_minuit_binned.ndof))

        # UNBINNED FIT
        my_cost_unbinned_func = UnbinnedNLL(data, model_function)
        my_minuit_unbinned = Minuit(my_cost_unbinned_func, mu = np.mean(data), sigma = np.std(data))
        my_minuit_unbinned.limits["mu","sigma"]=(0,None)
        my_minuit_unbinned.migrad()
        list_mu_unbinned_tmp.append(my_minuit_unbinned.values[0])
        list_sigma_unbinned_tmp.append(my_minuit_unbinned.values[1])
        list_chi2_unbinned_tmp.append(1. - sci.chi2.cdf(my_minuit_unbinned.fval, df = my_minuit_unbinned.ndof))

        # LEAST SQUARES FIT
        bin_probabilities = np.array(bin_content)/N_events
        bin_centres = []
        sigma_y = []
        for i in range(len(bin_edges)-1):
            bin_centres.append(((bin_edges[i+1]-bin_edges[i])/2)+bin_edges[i])
            num = np.sqrt(N_events*bin_probabilities[i]*(1-bin_probabilities[i]))
            if num == 0:
                num = 0.1
            sigma_y.append(num) # binomial fluctuation per bin
        bin_width = abs(bin_edges[1]-bin_edges[0])

        my_cost_leastsq_func = LeastSquares(bin_centres, bin_content, sigma_y, leastsq_model_function) # bin_centres, bin_content, sigma_y, func_approx
        my_minuit_leastsq = Minuit(my_cost_leastsq_func, N_events=N_events, mu = np.mean(data), sigma = np.std(data), bin_width=bin_width)
        my_minuit_unbinned.limits["mu","sigma"]=(0,None)
        my_minuit_leastsq.migrad()
        list_mu_leastsq_tmp.append(my_minuit_leastsq.values[1])
        list_sigma_leastsq_tmp.append(my_minuit_leastsq.values[2])
        list_chi2_leastsq_tmp.append(1. - sci.chi2.cdf(my_minuit_leastsq.fval, df = my_minuit_leastsq.ndof))

    list_mu_binned.append(np.mean(list_mu_binned_tmp))
    list_sigma_binned.append(np.mean(list_sigma_binned_tmp))
    list_chi2_binned.append(np.mean(list_chi2_binned_tmp))

    list_mu_unbinned.append(np.mean(list_mu_unbinned_tmp))
    list_sigma_unbinned.append(np.mean(list_sigma_unbinned_tmp))
    list_chi2_unbinned.append(np.mean(list_chi2_unbinned_tmp))

    list_mu_leastsq.append(np.mean(list_mu_leastsq_tmp))
    list_sigma_leastsq.append(np.mean(list_sigma_leastsq_tmp))
    list_chi2_leastsq.append(np.mean(list_chi2_leastsq_tmp)) 
    
    N_list.append(N_events)
    N_events = int(N_events*np.exp(1)) # useful for 'while cicle'
    
print(f'binned mu: {list_mu_binned}, \nunbinned mu: {list_mu_unbinned}, \nleastsq mu: {list_mu_leastsq}')
print(f'binned sigma: {list_sigma_binned}, \nunbinned sigma: {list_sigma_unbinned}, \nleastsq sigma: {list_sigma_leastsq}')
print(f'binned p-value: {list_chi2_binned}, \nunbinned p-value: {list_chi2_unbinned}, \nleastsq p-value: {list_chi2_leastsq}')

fig, ax = plt.subplots(1,2)

ax[0].plot(N_list, list_mu_unbinned, label='Unbinned', marker='.', color='red')
ax[0].plot(N_list, list_mu_binned, label='Binned', marker='.', color='green')
ax[0].plot(N_list, list_mu_leastsq, label='Least Squares', marker='.', color='blue', alpha=0.6)
ax[0].set_xlabel('N')
ax[0].set_ylabel('Mu')
ax[0].set_xscale('log')
ax[0].legend()
ax[0].grid(color='black', linestyle='--', linewidth=0.5, alpha=0.5)

ax[1].plot(N_list, list_sigma_unbinned, label='Unbinned', marker='.', color='red')
ax[1].plot(N_list, list_sigma_binned, label='Binned', marker='.', color='green')
ax[1].plot(N_list, list_sigma_leastsq, label='Least Squares', marker='.', color='blue', alpha=0.6)
ax[1].set_xlabel('N')
ax[1].set_ylabel('Sigma')
ax[1].set_xscale('log')
ax[1].legend()
ax[1].grid(color='black', linestyle='--', linewidth=0.5, alpha=0.5)

plt.show()
