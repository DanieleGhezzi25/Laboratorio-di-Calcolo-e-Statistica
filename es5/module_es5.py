# fraction library (exercise 1-2-3)

from math import gcd

class fraction:
    
    def __init__ (self, numerator, denominator):
        
        # checks
        if denominator == 0:
            raise ValueError ("Denominator can't be zero")
        if type(numerator) != int:
            raise TypeError ('Numerator must be an integer')
        if type(denominator) != int:
            raise TypeError ('Denominator must be an integer')
        
        # inizialitation
        common_divisor = gcd(numerator, denominator)
        self.numerator = int(numerator/common_divisor)
        self.denominator = int(denominator/common_divisor)
               
        return
    
    def print(self):
        print (f'{self.numerator}/{self.denominator}')
        return
    
    def __add__ (self, other):
        
        if type(other) == fraction:
            num = self.numerator*other.denominator + other.numerator*self.denominator
            denom = self.denominator * other.denominator
        if type(other) == int:
            num = self.numerator + other*self.denominator
            denom = self.denominator            
        if type(other) != fraction and type(other) != int:
            raise TypeError ('The addend must be int or fraction')
        
        return fraction(num,denom)
    
    def __sub__ (self,other):
        
        if type(other) == fraction:
            num = self.numerator*other.denominator - other.numerator*self.denominator
            denom = self.denominator * other.denominator
        if type(other) == int:
            num = self.numerator - other*self.denominator
            denom = self.denominator   
        if type(other) != fraction and type(other) != int:
            raise TypeError ('The addend must be int or fraction')
        
        return fraction(num,denom)
    
    def __mul__ (self,other):
        
        if type(other) == fraction:
            num = self.numerator * other.numerator
            denom = self.denominator * other.denominator
        if type(other) == int:
            num = self.numerator * other
            denom = self.denominator   
        if type(other) != fraction and type(other) != int:
            raise TypeError ('The addend must be int or fraction')
        
        return fraction(num,denom)
    
    def __truediv__ (self,other):
        
        if type(other) == fraction:
            num = self.numerator * other.denominator
            denom = self.denominator * other.numerator
        if type(other) == int:
            num = self.numerator
            denom = self.denominator * other
        if type(other) != fraction and type(other) != int:
            raise TypeError ('The addend must be int or fraction')
        
        return fraction(num,denom)
        
    def turning_float(self):
        return float(self.numerator/self.denominator)
    
    def return_numerator(self):
        return int(self.numerator)
    
    def return_denominator(self):
        return int(self.denominator)
        
    
frac1 = fraction(1,2)
frac2 = fraction(3,2)
number = 3
frac3 = frac1 + frac2
frac4 = frac1 - number
frac5 = frac1 * frac2
frac6 = frac2 / frac1

frac3.print()
frac4.print()
frac5.print()
frac6.print()
print (frac5.turning_float())