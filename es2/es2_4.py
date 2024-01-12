# Compare the time performances of element-wise operations performed between two lists with respect to the same operation performed in compact form between two NumPy arrays
# After which size the differences start being significant?

import time
import numpy as np
    
def main():
    vec1 = np.arange(0,1000000,1)
    vec2 = np.arange(0,2000000,2)
    start_time_vec = time.time()
    sum_vec = vec1 + vec2
    end_time_vec = time.time()
    
    list1 = vec1.tolist()
    list2 = vec2.tolist()
    final_list = []
    start_time_list = time.time()
    for i in range(len(list1)):
        final_list.append(list1[i] + list2[i])    
    end_time_list = time.time()
    
    print(f"{sum_vec[999999]}, time array = {(1000*(end_time_vec-start_time_vec)):.3f}ms")
    print(f"{final_list[999999]} time list = {(1000*(end_time_list-start_time_list)):.3f}ms")
    
    return

if __name__ == '__main__':
    main()