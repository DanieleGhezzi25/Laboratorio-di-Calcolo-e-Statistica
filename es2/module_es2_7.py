import numpy as np

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