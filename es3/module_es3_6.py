import numpy as np
from matplotlib import pyplot as plt

def mean_f (list):
    array = np.array(list)
    return np.sum(array)/len(list)

def variance_f (list):
    mean = mean_f(list)
    sum = 0
    for i in range(len(list)):
         sum += (list[i]-mean)**2
    return sum/len(list)

def variance_from_mean_f(list, mean):
    sum = 0
    for i in range(len(list)):
         sum += (list[i]-mean)**2
    return sum/len(list)

def std_f (list):
    return np.sqrt(variance_f(list))

def std_from_mean_f(list,mean):
    return np.sqrt(variance_from_mean_f(list,mean))

def std_mean_f(list):
    return std_f(list)/np.sqrt(len(list))

def std_mean_from_mean_f(list,mean):
    return std_from_mean_f(list,mean)/np.sqrt(len(list))


# --------------------------- #

def sturges(N):
    return int(np.ceil(1+3.322*np.log(N)))

def sample_hist(name_file):
    
    sample = np.loadtxt(name_file)
    
    bin_intervals = np.linspace(np.min(sample), np.max(sample), sturges(len(sample)))
    
    fig, ax = plt.subplots(nrows=1, ncols=1)
    
    ax.hist(sample, bins=bin_intervals, color='blue')
    ax.set_xlabel('Data')
    ax.set_ylabel('Event')
    ax.set_title('Histogram')
    
    mean = mean_f(sample)
    variance = variance_from_mean_f(sample,mean)
    std = std_from_mean_f(sample,mean)  
    std_mean = std_mean_from_mean_f(sample,mean)
    
    print(f"mean = {mean}, variance = {variance}, std = {std}, std mean = {std_mean}")
    
    plt.show()
    
    return mean, variance, std, std_mean
    