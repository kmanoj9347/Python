class car():
    def __init__(self,**kwargs):
        self.speed = kwargs['s']
        self.color = kwargs['c']
audi = car(s = 200,c='red')
bmw  = car(s =250,c='black')
kia = car(s=190,c='white')

print("Color of audi :",audi.color)
print("Speed of bmw:",bmw.speed)