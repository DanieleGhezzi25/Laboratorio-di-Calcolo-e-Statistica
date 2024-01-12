from cmath import sqrt

def solving_2nd_equation(a,b,c):
    delta = b*b - 4*a*c
    x1 = (-b + sqrt(delta))/(2*a)
    x2 = (-b - sqrt(delta))/(2*a)
    print(x1,x2)

def main ():
    print('Solving ax^2 + bx + c = 0 equation (in complex numbers).')
    a = int(input('Insert a coefficient: '))
    b = int(input('Insert b coefficient: '))
    c = int(input('Insert c coefficient: '))
    solving_2nd_equation(a,b,c)
    
if __name__ == "__main__":
  main ()

