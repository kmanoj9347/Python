# parameterized Constructor
class Addition:
    first =0
    second =0
    answer=0
    #parameterized constructor
    def __init__(self,f,s):
        self.first=f
        self.second=s
    def display(self):
        print("First number = "+str(self.first))
        print("Second number = "+str(self.second))
        print("Additoin of two numbers = "+str(self.answer))
    def calculate(self):
        self.answer =self.first+self.second        
obj1=Addition(1000,2000)
obj2=Addition(10,20)
obj1.calculate()
obj2.calculate()
obj1.display()
obj2.display()