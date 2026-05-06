# The area of a circle with radius [number] is [number]
import math 
diameter = 13
# diameter = 13 / 2
print('the diameter is: ' + str(diameter))

radius = 6.5
radius2 = 6.5**2
area = round(radius2 * math.pi, 2)  
print(area)
print()
print("The radius is:  " + str(radius) + " " + 'so the radius to the 2nd power would be:  ' + str(radius2)) 
print()
print('The area of a circle with radius' + " " + str(radius) + " " + "is " + str(area)) 

#OUTPUT: 

#the diameter is: 13


#The radius is:  6.5 so the radius to the 2nd power would be:  42.25

#The area of a circle with radius 6.5 is 132.73