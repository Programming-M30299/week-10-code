from graphics import *


def testPoint():
    p = Point(100, 50)

    print("p is of type:", type(p))  # Point

    print("p's x coordinate is", p.getX())  # 100
    print("p's y coordinate is", p.getY())  # 50

    p.move(10, -20)

    print("p's x coordinate is", p.getX())  # 110
    print("p's y coordinate is", p.getY())  # 30

    print("p is:", p)  # Point(110, 30)


testPoint()
