# mean, variance, std, std from the mean of its element

import numpy as np
import module_es2_7 as mod

def main():
    list = [2,2,3,3]
    mean = mod.mean_f(list)
    print(mean, mod.variance_f(list), mod.std_f(list), mod.std_from_mean_f(list,mean))
    return

if __name__ == '__main__':
    main()