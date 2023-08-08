class Car:
    def __init__(self, colour, numberPlate):
        self.colour = colour
        self.numberPlate = numberPlate
        self.speed = 0

    def getNumberPlate(self):
        return self.numberPlate

    def getcolour(self):
        return self.colour

    def getSpeed(self):
        return self.speed

    def setColour(self, colour):
        if colour in ["red", "green", "blue", "yellow"]:
            self.colour = colour

    def brake(self):
        self.speed = 0

    def accelerate(self):
        if self.speed <= 60:
            self.speed += 10

    def __str__(self):
        output = "Car with number place " + self.numberPlate
        output += " is " + self.colour
        output += " and is going " + str(self.speed) + " mph"
        return output


def testCar():
    myCar = Car("red", "ABC123")

    print("My car is", myCar.getcolour())
    myCar.setColour("blue")
    print("My car is now", myCar.getcolour())

    print("My car is going", myCar.getSpeed(), "mph")
    myCar.accelerate()
    print("My car is now going", myCar.getSpeed(), "mph")
    myCar.brake()
    print("After braking, my car's speed is", myCar.getSpeed(), "mph")

    print(myCar)


testCar()
