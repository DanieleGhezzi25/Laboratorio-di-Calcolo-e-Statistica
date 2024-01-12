# Create a one-dimentional NumPy array containing a sequence of integer numbers from 1 to 100.
# Starting from this, create a one-dimensional NumPy array containing in each entry the sum of integer numbers 
# from 1 until the index of that entry

import numpy as np

def main ():
    sequence = []
    final_list = []
    for i in range(1,100):
        sequence.append(i)
        sequence1 = np.array(sequence)
        final_list.append(np.sum(sequence1, dtype=int))
    print(sequence)
    print(final_list)
    return

if __name__ == '__main__':
    main()