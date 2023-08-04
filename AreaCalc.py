'''
Author: Confumi
Description: User selects either a triangle or circle for the area to be calculated
'''
print ('Area Calculator is running!')

option = input("Enter C for Circle or T for Triangle: ").upper()
if option == 'C':
  radius = float(input("Enter radius: "))
  area = 3.14159*radius**2
  print ('The area of the circle with a radius of %s is %s' %(radius, area))
elif option == 'T':
  base = float(input('Enter the base of your triangle: '))
  height = float(input('Enter the height of your triangle: '))
  area = .5 * base * height
  print ('The area of the triangle with the base %s and the height %s is %s' % (base, height, area))
else:
  print ('Sorry your input was not a valid option')

print ('The program is now terminating :)')