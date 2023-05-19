#polymorphism using inheritance and method overriding.
class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement this method")
class Dog(Animal):
        def speak(self):
            return "Woof!"
class Cat (Animal):
    def speak(self):
        return "Meow!"
animals = [Dog(),Cat()]
for animal in animals:
    print(animal.speak())