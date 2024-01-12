import numpy as np

def median(array):
    array = np.sort(array)
    length = len(array.tolist())
    return array[int(length/2)]
