# default constructor
class Person:
    def __init__(self):
        self.name="John"
        self.age=19
    def display_info(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
person =Person()
person.display_info()