class Animal:
    def __init__(self, name, species):
        self._name = name
        self._species = species

    def make_sound(self):
        print("The animal makes sound")

class Dog(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def make_sound(self):
        print("Meow!")

if __name__ == "__main__":
    dog = Dog("Buddy", "Canine")
    dog.make_sound()
    cat = Cat("Whiskers", "Feline")
    cat.make_sound()