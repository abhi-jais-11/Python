#function to calculate the area of circle 
from math import pi
def circle_area(r):
    return pi*r**2

radius=5
ans=circle_area(radius)
print("Area of circle of radius {0} is {1:.2f}".format(radius,ans))