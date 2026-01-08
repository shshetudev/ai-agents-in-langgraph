from abc import ABC, abstractmethod

# DIP: Dependency Inversion Principle
# High-level modules should not depend on low-level modules.
# Both should depend on abstractions.
# Here, the Car class depends on the Engine abstraction rather than concrete engine implementations.

class Engine(ABC):
    @abstractmethod
    def start(self) -> None:
        pass

class BasicEngine(Engine):
    def start(self) -> None:
        print("Basic engine started")

class FastEngine(Engine):
    def start(self) -> None:
        print("Activated power boot!")
        print("Fast engine started")

class Car:
    def __init__(self, engine: Engine):
        self.engine = engine

    def start(self):
        self.engine.start()
        print("Car started")

if __name__     == "__main__":
    # we can now inject any class that inherits the abstract Engine class, making our code more flexible.
    # Because it is no longer tightly coupled to a particular concrete engine.
    fast_engine = FastEngine()
    car = Car(fast_engine)
    car.start()

    basic_engine = BasicEngine()
    car = Car(basic_engine)
    car.start()