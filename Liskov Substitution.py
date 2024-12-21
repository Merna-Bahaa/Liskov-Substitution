from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

def calculate_area(shape: Shape):
    return shape.area()

square = Square(4)
rectangle = Rectangle(3, 4)

print(calculate_area(square))  
print(calculate_area(rectangle))
