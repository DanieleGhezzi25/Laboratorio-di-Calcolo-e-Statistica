# Write a program that, given the three sides of a triangle, determines whether the triangle is acute-angled, rectangular-angled or obtuse-angled.

from numpy import arccos,pi

def angle_calculator (a,b,c):
	' Calculate the angle in radiants between side a and b using the cosine theorem '
	angle = arccos((c**2 - a**2 - b**2)/(-2*a*b))
	return angle

def determine_triangle (a,b,c):
	alpha = angle_calculator(a,b,c)
	beta = angle_calculator(b,c,a)
	gamma = angle_calculator(c,a,b)
	if alpha < pi/2 and beta < pi/2 and gamma < pi/2: 
		print ('The triangle is acute-angled')
	else:
		print ('The triangle is obtuse-angled')
	
def determine_rectangular_triangle (a,b,c):
	list = [a,b,c]
	hypotenuse = list.max
	list.remove(list.max)
	if hypotenuse > list[0] + list[1]:
		print('Invalide sides')
		exit()
	if hypotenuse**2 == list[0]**2 + list[1]**2:
		print ('The triangle is rectangular-angled')
		return 1
	else:
		return 0

def main ():
	a = float(input('Insert side\'s lenght: '))
	b = float(input('Insert side\'s lenght: '))
	c = float(input('Insert side\'s lenght: '))
	
	if determine_rectangular_triangle == 1:
		return
	
	else:
		determine_triangle(a,b,c)
	
	return
	
if __name__ == "__main__":
  main ()
