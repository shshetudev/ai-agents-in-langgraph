class Vehicle:
    def __init__(self, brand, model, year):
        self._brand = brand
        self._model = model
        self._year = year

    def start(self):
        print(f"Vehicle Brand: {self._brand}, Model: {self._model}, Year: {self._year} started")

    def stop(self):
        print(f"Vehicle Brand: {self._brand}, Model: {self._model}, Year: {self._year} stopped")


class Car(Vehicle):
    def __init__(self, brand, model, year, num_of_doors, num_of_wheels):
        super().__init__(brand, model, year)
        self._num_of_doors = num_of_doors
        self._num_of_wheels = num_of_wheels


class Bike(Vehicle):
    def __init__(self, brand, model, year, num_of_wheels):
        super().__init__(brand, model, year)
        self._num_of_wheels = num_of_wheels


# Test cases
if __name__ == "__main__":
    car = Car("Toyota", "Camry", 2020, 4, 4)
    bike = Bike("Yamaha", "YZF-R3", 2021, 2)

    print(car.__dict__)
    print(bike.__dict__)

    car.start()
    car.stop()

    bike.start()
    bike.stop()

