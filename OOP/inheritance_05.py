#multiple inheritance
#Base class1
class Mother:
    mothername =""
    def mother(self):
        print(self.mothername)
#Base class2
class Father:
    fathername =""
    def father(self):
        print(self.fathername)
#Derived class
class Son(Mother,Father):
    def parents(self):
        print("Father Name :",self.fathername)
        print("Mother Name :",self.mothername)
s1 =Son()
s1.fathername = "Seena"
s1.mothername = "Ani"
s1.parents()