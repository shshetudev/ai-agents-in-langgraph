# Step 1: Define a class named Dog -> create bark method
# Step 2: Define a class named GoodDog -> create a constructor(first_name, last_name, breed) -> create bark method -> create get_full_name method
# Step 4: Create a class named Owner -> create a constructor(name, address, contact_number)
# Step 3: Define a class named ExcellentDog -> create a constructor(first_name, last_name, breed, owner) -> create bark method -> create get_full_name method

class Dog:
    def bark(self):
        print("Whoof Whoof")

dog = Dog()
dog.bark()


class GoodDog:
    def __init__(self, first_name, last_name, breed):
        self.first_name = first_name
        self.last_name = last_name
        self.breed = breed

    def bark(self):
        print("Woof Woof")

    def get_full_name(self):
        return f"{self.first_name}" + " " + f"{self.last_name}"

scottyDog = GoodDog("Angus", "Biggsby", "Scottish Terrier")
scottyDog.bark()


class Owner:
    def __init__(self, name, address, contact_number):
        self.name = name
        self.address = address
        self.contact_number = contact_number

class ExcellentDog:
    def __init__(self, first_name, last_name, breed, owner: Owner):
        self.first_name = first_name
        self.last_name = last_name
        self.breed = breed
        self.owner = owner

    def bark(self):
        print("Woof Woof Woof")
    # getter method
    def get_full_name(self):
        return f"{self.first_name}" + " " + f"{self.last_name}"


owner = Owner("Owner_ABC", "Owner_ABC Home", "0123456789")
scottyDog = ExcellentDog("ABC", "DEF", "Scottish Terrier", owner)
print(scottyDog.owner.name)