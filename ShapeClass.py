import math

class Shape:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
    
    def calculate_area(self):
        print("Area calculation not defined.")

class Circle(Shape):
    def __init__(self, name, radius):
        Shape.__init__(self, name)
        self.__radius = radius
    def calculate_area(self):
        return math.pi * (self.__radius**2) 

class Rectangle(Shape):
    def __init__(self, name, height, width):
        Shape.__init__(self, name)
        self.__height = height
        self.__width = width
    def calculate_area(self):
        return self.__height * self.__width
    
class Triangle(Shape):
    def __init__(self, name, height, base):
        Shape.__init__(self, name)
        self.__height = height
        self.__base = base
    def calculate_area(self):
        return self.__height * self.__base * 0.5