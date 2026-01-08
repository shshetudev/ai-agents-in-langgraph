class Engine:
    def start(self):
        print("Starting engine")

class Wheels:
    def rotate(self):
        print("Wheels Rotate")

class Chassis:
    def support(self):
        print("Chassis supports the car")

class Seats:
    def sit(self):
        print("Sitting on seats")

# Car is composed of the above components
class Car:
    def __init__(self):
        self._engine = Engine()
        self._wheels = Wheels()
        self._chassis = Chassis()
        self._seats = Seats()

    def start(self):
        self._engine.start()
        self._wheels.rotate()
        self._chassis.support()
        self._seats.sit()

car = Car()
car.start()