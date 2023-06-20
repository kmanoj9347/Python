#Operator overLoading
class A:
    def __init__(self,a):
        self.a=a

    #adding two objects
    def __add__(self,o):
        return self.a+o.a
obj1 =A(1)
obj2 =A(2)
obj3 =A('Good')
obj4 =A('Morning')

print(obj1+obj2)
print(obj3+obj4)
#Actual working when Binary Operator is used.
print(A.__add__(obj1,obj2))
print(A.__add__(obj3,obj4))