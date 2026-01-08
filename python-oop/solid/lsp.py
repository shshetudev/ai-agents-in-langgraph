from abc import ABC, abstractmethod

# LSP: Liskov Substitution Principle
# Subtypes must be substitutable for their base types.
# Here, both Rectangle and Square can be used wherever Shape is expected.

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

class Rectangle(Shape):
    def __init__(self, width: float = 0.0, height: float = 0.0):
        self._width = width
        self._height = height

    def area(self) -> float:
        return self._width * self._height

class Square(Shape):
    def __init__(self, side: float = 0.0):
        self._side = side

    def area(self) -> float:
        return self._side * self._side

if __name__ =="__main__":
    rectangle = Rectangle()
    rectangle._width = 4
    rectangle._height = 5
    print(f"Rectangle area: {rectangle.area()}")

    square = Square()
    square._side = 4
    print(f"Square area: {square.area()}")