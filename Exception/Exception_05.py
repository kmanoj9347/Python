class MyError(Exception):
   #Constructor or Initializer
    def __init__(self,value):
        self.value = value
#__str__ is to print() the value
    def __str__(self):
        return(repr(self.value))
try:
    raise(MyError(3*2))
#value of Eception is stored in error
except MyError as error:
    print('A New Exception occured: ',error.value)
    