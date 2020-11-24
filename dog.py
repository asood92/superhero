# dog.py
class Dog:
    # Required properties are defined inside the __init__ constructor method
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        print("dog initialized!")

    # Methods are defined as their own named functions inside the class
    # Remember to put the "self" parameter every time we make a class method!
    def bark(self):
        print("Woof!")

    def sit(self, name):
        self.name = name
        print(f"{self.name} sits.")

    def roll(self, name):
        self.name = name
        print(f"{self.name} rolls over.")