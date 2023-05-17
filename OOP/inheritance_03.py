#parent class
class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def dispaly(self):
        print(self.name,self.age)
# child class
class Student(Person):
    def __init__(self,name,age):
        self.sName = name
        self.sAge = age
    #inheritin the properties of parent class
        super().__init__("Rahul",age)
    def dispalyInfo(self):
        print(self.sName,self.sAge)
obj = Student("Manoj",19)
obj.dispaly()
obj.dispalyInfo()
