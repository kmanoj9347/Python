#instantiating a class
class Dog:
    attr1 = "mammal"
    attr2 = "dog"

    def fun(self):
        print("I'm a",self.attr1)
        print("I'm a",self.attr2)
#Object instantiation
Rodger = Dog()
#Accessing class attributes
#and method through objects
print(Rodger.attr1)
Rodger.fun()