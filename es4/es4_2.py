# module LCG (linear congruential generator)

class LGC:
    
    def __init__ (self, seed, M, A, C, N_times=0):
        
        random_list = []
        
        if N_times != 0:
            for i in range(N_times):
                seed = (A*seed+C) % M
                random_list.append(seed)
            self.random_list = random_list
            self.seed = random_list[N_times-1] # it gives the last element of the list
        
        self.random_list = random_list
        self.seed = seed
        
        return
    
    def random (self, M, A, C, N_times):
        if N_times == 0:
            raise ValueError('N times could not be 0!')
        seed = self.seed
        for i in range(N_times):
            seed = (A*seed+C) % M
            self.random_list.append(seed)
        return
    
    def change_seed(self, new_seed):
        self.seed = new_seed
        return
    
    def print(self):
        print(self.random_list)
        return

M = 2147483647
A = 214013
C = 2531011
seed = 1

list = LGC(seed, M, A, C, N_times=0)
list.print()
list.random(M, A, C, N_times=10)
list.print()
list.change_seed(3)
list.random(M, A, C, N_times=10)
list.print()
