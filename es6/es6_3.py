# Implement a function that calculates the factorial of a number using a recursive function.

def fac(n):
    if n<2:
        return 1
    return n*fac(n-1)

print(fac(7))