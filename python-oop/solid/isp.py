from abc import ABC, abstractmethod

# ISP: Interface Segregation Principle
# Clients should not be forced to depend on methods they do not use.
# Here, we separate 2D and 3D shape interfaces.

class Shape2D(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

class Shape3D(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def volume(self) -> float:
        pass

class Circle(Shape2D):
    def __init__(self, radius: float):
        self._radius = radius

    def area(self) -> float:
        import math
        return math.pi * (self._radius ** 2)

class Sphere(Shape3D):
    def __init__(self, radius: float):
        self._radius = radius

    def area(self) -> float:
        import math
        return 4 * math.pi * (self._radius ** 2)

    def volume(self) -> float:
        import math
        return (4/3) * math.pi * (self._radius ** 3)


if __name__ == '__main__':
    circle = Circle(5)
    print(f"Circle area: {circle.area()}")

    sphere = Sphere(5)
    print(f"Sphere area: {sphere.area()}")
    print(f"Sphere volume: {sphere.volume()}")