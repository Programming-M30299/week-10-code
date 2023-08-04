from graphics import *


class MyPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        output = "MyPoint({0}, {1})".format(self.x, self.y)
        return output


class Square():
    def __init__(self, p1, side):
        self.p1 = p1
        self.side = side
        self.p2 = MyPoint(p1.getX() + side, p1.getY() + side)

    def getP1(self):
        return self.p1

    def getP2(self):
        return self.p2

    def getSide(self):
        return self.side

    def move(self, dx, dy):
        self.p1.move(dx, dy)
        self.p2.move(dx, dy)

    def __str__(self):
        output = "Square({0}, {1})".format(self.p1, self.p2)
        return output


def testMyPoint():
    myPoint = MyPoint(100, 50)
    print("myPoint's x coordinate is", myPoint.getX())  # 100
    print("myPoint's y coordinate is", myPoint.getY())  # 50

    myPoint.move(10, -20)

    print("myPoint's x coordinate is", myPoint.getX())  # 110
    print("myPoint's y coordinate is", myPoint.getY())  # 30

    # <__main__.MyPoint object at 0x7f9b1c0b6a90>
    print("myPoint is:", myPoint)


def testPoint():
    p = Point(100, 50)

    print("p is of type:", type(p))  # <class 'graphics.Point'>

    print("p's x coordinate is", p.getX())  # 100.0
    print("p's y coordinate is", p.getY())  # 50.0

    p.move(10, -20)

    print("p's x coordinate is", p.getX())  # 110.0
    print("p's y coordinate is", p.getY())  # 30.0

    print("p is:", p)  # Point(110.0, 30.0)


def testSquare():
    p1 = MyPoint(100, 50)
    square = Square(p1, 50)
    print(square.getSide())  # 50
    print(square.getP1())  # MyPoint(100, 50)
    print(square.getP2())  # MyPoint(150, 100)

    square.move(10, -20)
    print(square.getSide())  # 50
    print(square.getP1())  # MyPoint(110, 30)
    print(square.getP2())  # MyPoint(160, 80)

    print(square)  # Square(MyPoint(110, 30), MyPoint(160, 80))
