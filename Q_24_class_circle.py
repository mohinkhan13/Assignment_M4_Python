'''
Write a Python class named Circle constructed by a radius and two 
methods which will compute the area and the perimeter of a circle
'''
class Circle:
    PI = 3.14159  

    def __init__(self, radius):
        self.radius = radius  
    def area(self):
        
        return Circle.PI * (self.radius ** 2)

    def perimeter(self):

        return 2 * Circle.PI * self.radius

circle1 = Circle(radius=5)
circle2 = Circle(radius=10)

print(f"Area of circle 1: {circle1.area():.2f}") 
print(f"Perimeter of circle 1: {circle1.perimeter():.2f}") 

print(f"Area of circle 2: {circle2.area():.2f}") 
print(f"Perimeter of circle 2: {circle2.perimeter():.2f}")
