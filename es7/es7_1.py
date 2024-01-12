# Generate a sample of pseudo-random numbers distributed according to an exponential density 
# distribution with a characteristic time t0 of 5 seconds.
# Visualize the distribution of the obtained sample in a histogram using the inverse function method.
# Write all functions responsible for random number generation in a library, implemented in separate files 
# from the main program.

import module_randomGen as gen
import module_stats as st

def main():
    
    N = 10000
    tau = 5
    exponential_distribution = st.stats(list = gen.INV_generation_exponential(tau, N))
    exponential_distribution.hist()
    
    return

if __name__ == "__main__":
  main ()


