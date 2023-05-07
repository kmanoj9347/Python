class Bike():
    def __init__(self,*args):
        self.speed = args[0]
        self.color = args[1]

#creating objects of car class
Honda = Bike(90,'red')
yamaha=Bike(110,'Black')
Hero = Bike(95,'Grey')

print(Honda.color)
print(Hero.speed)

