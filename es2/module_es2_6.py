import numpy as np

def values_that_determine_tails_given_the_percentual (list, percentual):
    
    if percentual < 0 or percentual > 100:
        print('ERROR: the percentual must be between 0 and 100.')
        return 'ERROR', 'ERROR'
    
    array = np.sort(np.array(list))
    
    # if index calculus return a float, int() function returns the least int (ex. int(3.8) ---> 3). 
    # So, if the decimal unit is > 5, add 1 to the index (ex. int(3.8) ---> 3 ---> 4)
    real_index = (percentual/100)*len(array)
    index_begin = int(real_index)
    # ex. len(array) = 6, percentual = 0.3, index_begin = 1 (the real index is 1.8). 
    # because 1.8*, the best index is 2 (that is the nearest int index to 1.8)
    # if index_begin/(percentual/100) < len(array):  
    #    index_begin = index_begin + 1
    index_end = len(array)-index_begin
    
    return array[index_begin], array[index_end]
    