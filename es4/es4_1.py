# Write a function that implements the linear congruential generator for pseudo-random numbers, using these parameters:
# M = 2147483647   A = 214013  C = 2531011

def linear_congruential_generator(M,A,C, seed):
    return (A*seed+C) % M

def main():
    M = 2147483647
    A = 214013
    C = 2531011
    seed = 1
    N = 10
    random_list = []
    random_list.append(linear_congruential_generator(M,A,C,seed))
    for i in range(N-1):
        random_list.append(linear_congruential_generator(M,A,C,random_list[i]))
    print(random_list)
    return

if __name__ == "__main__":
    main()