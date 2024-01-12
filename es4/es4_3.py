# Show that initializing the seed of a pseudo-random integer generator is equivalent to looking into a sequence of pseudo-random numbers at any point.

def linear_congruential_generator(M,A,C, seed):
    return (A*seed+C) % M

def main():
    M = 2147483647
    A = 214013
    C = 2531011
    N = 10
    random_list1 = []
    random_list2 = []
    
    seed = 1
    random_list1.append(linear_congruential_generator(M,A,C,seed))
    
    for i in range(N-1):
        random_list1.append(linear_congruential_generator(M,A,C,random_list1[i]))
    
    seed2 = random_list1[5]
    random_list2.append(linear_congruential_generator(M,A,C,seed2))
    
    for i in range(N):
        random_list2.append(linear_congruential_generator(M,A,C,random_list2[i]))
    
    print(random_list1)
    print(random_list2)
    
    return

if __name__ == "__main__":
    main()