from graphics import *


def testPoint():
    p = Point(100, 50)

    print("p is of type:", type(p))  # <class 'graphics.Point'>

    print("p's x coordinate is", p.getX())  # 100.0
    print("p's y coordinate is", p.getY())  # 50.0

    p.move(10, -20)

    print("p's x coordinate is", p.getX())  # 110.0
    print("p's y coordinate is", p.getY())  # 30.0

    print("p is:", p)  # Point(110.0, 30.0)


testPoint()
