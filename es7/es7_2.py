# Use the result from the first exercise to simulate a countng experiment with Poisson characteristics:
# Choose a characteristic time t0 for a radioactive decay process;
# Choose a measurement time tM for the counting window;
# In a loop, simulate N pseudo-experiments of counting, where, for each of them, a sequence of random events 
# is generated with an intertime characteristic of Poisson phenomena, until the total time elapsed is greater 
# than the measurement time, counting the number of generated events that fall within the interval.
# Fill a histogram with the simulated counts for each experiment.

import module_randomGen as gen
import module_stats as st
import numpy as np

def main():
    
    t0 = 1
    t_counting = 10
    lambda_poisson = t_counting/t0 # = 10
    
    N_experiments = 10000
    poissonian_events = []
    
    for i in range(N_experiments):
        delta_t = 0
        countings = 0
        while (delta_t <= t_counting):
            delta_t += gen.INV_generation_exponential(tau=t0)
            countings += 1
        poissonian_events.append(countings)
    
    poissonian_events_st = st.stats(list = poissonian_events)
    poissonian_events_st.hist(bin_intervals = np.arange(np.min(poissonian_events)-0.5, np.max(poissonian_events)+1.5, 1), xlabel = 'Countings', ylabel = 'N times', title = 'Poissonian Distribution', label = 'Poissonian Distribution') 
    
    return

if __name__ == "__main__":
  main ()
