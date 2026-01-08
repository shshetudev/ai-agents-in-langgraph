from abc import ABC, abstractmethod
import math

# OCP: Open/Closed Principle
# Software entities should be open for extension but closed for modification.
# Here, we can add new shapes without modifying existing code.

class Shape(ABC):
    @abstractmethod
    def calculate_area(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, radius: float):
        self._radius = radius

    def calculate_area(self) -> float:
        return math.pi * (self._radius ** 2)

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height

    def calculate_area(self) -> float:
        return self._width * self._height

if __name__  == "__main__":
    circle = Circle(10)
    rectangle = Rectangle(4, 5)

    print(f"Circle area: {circle.calculate_area()}")
    print(f"Rectangle area: {rectangle.calculate_area()}")