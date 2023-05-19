class CSStudent:
    stream = 'cse' #class Variable
    def __init__(self,name,roll):
        self.name = name   #Instance Varaible
        self.roll = roll   #Instance Varaible
#Objects of CSStudent class
a = CSStudent('Manoj',1) 
b = CSStudent('Nani',2)
print(a.stream)
print(b.stream)
print(a.name)
print(b.name)
print(a.roll)
print(b.roll)
#Class variable can be accessed using class name also.
print(CSStudent.stream) #prints "cse"
#Now if we change the stream for just a it won't be changed for b
a.stream = 'ece'
print(a.stream)
print(b.stream)
#To change the stream for all instance of the class we can change it
#directly from the class.
CSStudent.stream = 'mech'
print(a.stream) #prints 'ece'
print(b.stream) #prints 'mech'