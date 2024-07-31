'''
Write a Python class named Rectangle constructed by a length and 
width and a method which will compute the area of a rectangle
'''

class Rectangle:
    def __init__(self, length, width):
        self.length = length  
        self.width = width   

    def area(self):
        return self.length * self.width

rect1 = Rectangle(length=10, width=5)
rect2 = Rectangle(length=7, width=3)

print(f"Area of rectangle 1: {rect1.area()}")  # Output: Area of rectangle 1: 50
print(f"Area of rectangle 2: {rect2.area()}")  # Output: Area of rectangle 2: 21
