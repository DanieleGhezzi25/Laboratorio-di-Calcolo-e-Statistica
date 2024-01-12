# Implement an object named stats, which calculates the statistics associated with a sample of numbers 
# stored in a Python list.

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats as scipystats

def sturges(N):
    return int(np.ceil(1+3.322*np.log(N)))

class stats:
    
    def __init__(self, txt_name = None, list = None, bessel_correction = True):
        
        if bessel_correction == True:
            N = 1
        else:
            N = 0
        
        if txt_name is not None and list is None:
            if type(txt_name) != str:
                raise TypeError('Invalid type: insert a string')
            self.list = np.loadtxt(txt_name) 
            self.mean = np.mean(self.list)
            self.variance = np.var(self.list, ddof=N) # ddof = 1 applicates Bessel's correction
            self.std = np.sqrt(self.variance)
            self.std_mean = self.std/np.sqrt(len(self.list))
            self.skew = scipystats.skew(self.list)
            self.kurtosis = scipystats.kurtosis(self.list)
            
        if txt_name is None and list is not None:
            self.list = list
            self.mean = np.mean(self.list)
            self.variance = np.var(self.list, ddof=N) # ddof = 1 applicates Bessel's correction
            self.std = np.sqrt(self.variance)
            self.std_mean = self.std/np.sqrt(len(self.list))
            self.skew = scipystats.skew(self.list)
            self.kurtosis = scipystats.kurtosis(self.list)
        
        
        if txt_name is None and list is None:
            self.list = []
            self.mean = 0
            self.variance = 0
            self.std = 0
            self.std_mean = 0
            self.skew = 0
            self.kurtosis = 0
        
        return
    
    def append_value(self, value, bessel_correction = True):
        
        if type(value) == list or type(value) == np.array:
            raise TypeError('Invalide type: insert a number')
        
        if bessel_correction == True:
            N = 1
        else:
            N = 0
        
        self.list.append(value)
        self.mean = np.mean(self.list)
        self.variance = np.var(self.list, ddof=N)
        self.std = np.sqrt(self.variance)
        self.std_mean = self.std/np.sqrt(len(self.list))
        self.skew = scipystats.skew(self.list)
        self.kurtosis = scipystats.kurtosis(self.list)
        
        return
    
    def append_list(self, list, bessel_correction = True):
        
        if type(list) != list and type(list) != np.array:
            raise TypeError('Invalide type: insert a number')
        
        if bessel_correction == True:
            N = 1
        else:
            N = 0
        
        self.list.extend(list)
        self.mean = np.mean(self.list)
        self.variance = np.var(self.list, ddof=N) # ddof = 1 applicates Bessel's correction
        self.std = np.sqrt(self.variance)
        self.std_mean = self.std/np.sqrt(len(self.list))
        self.skew = scipystats.skew(self.list)
        self.kurtosis = scipystats.kurtosis(self.list)
        
        return
    
    def print_stats(self):
        print(f'Mean = {self.mean}')
        print(f'Variance = {self.variance}')
        print(f'Standard Deviation = {self.std}')
        print(f'Standard Deviation of the mean = {self.std_mean}')
        print(f'Skewness = {self.skew}')
        print(f'Kurtosis = {self.kurtosis}')
        return 
    
    def return_stats(self):
        return [self.mean, self.variance, self.std, self.std_mean, self.skew, self.kurtosis]
    
    def return_mean(self):
        return self.mean
    
    def return_variance(self):
        return self.variance
    
    def return_std(self):
        return self.std
    
    def return_std_mean(self):
        return self.std_mean
    
    def return_skew(self):
        return self.skew
    
    def return_kurtosis(self):
        return self.kurtosis
    
    def hist(self, color='red', xlabel='x', ylabel='y', title='Histogram', label='Histogram', bin_number=None, bin_intervals=None):
        
        if bin_number is None and bin_intervals is None:
            bin = np.linspace(np.min(self.list), np.max(self.list), sturges(len(self.list)))
        if bin_number is not None and bin_intervals is None:
            bin = int(bin_number)
        if bin_number is None and bin_intervals is not None:
            bin = list(bin_intervals)
        
        fig, ax = plt.subplots(1,1)  
        ax.hist(self.list, bins=bin, label=label, color=color)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_title(title)
        ax.legend()
        ax.grid(color='black', linestyle='--', linewidth=0.5, alpha=0.5)
        plt.show()
        
        return