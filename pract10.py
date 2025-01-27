from graphix import Point


class MyPoint:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return f"MyPoint({self.x}, {self.y})"


class Square:

    def __init__(self, p1, side):
        self.p1 = p1
        self.side = side
        self.p2 = MyPoint(p1.x + side, p1.y + side)

    def move(self, dx, dy):
        self.p1.move(dx, dy)
        self.p2.move(dx, dy)

    def __str__(self):
        output = f"Square({self.p1}, {self.p2})"
        return output


def test_square():
    p = MyPoint(100, 50)
    square = Square(p, 50)

    print("square's side length is", square.side)  # 50
    print("square's p1 is", square.p1)  # MyPoint(100, 50)
    print("square's p2 is", square.p2)  # MyPoint(150, 100)

    square.side = 100
    print("After changing square's side length to 100 ...")
    print("square's side length is", square.side)  # 100

    square.move(10, -20)
    print("After the move ...")
    print("square's side length is", square.side)  # 100
    print("square's p1 is", square.p1)  # MyPoint(110, 30)
    print("square's p2 is", square.p2)  # MyPoint(160, 80)

    print(square)  # Square(MyPoint(110, 30), MyPoint(160, 80))


def test_my_point():
    my_point = MyPoint(100, 50)
    print("my_point's x coordinate is", my_point.x)  # 100
    print("my_point's y coordinate is", my_point.y)  # 50

    my_point.move(10, -20)
    print("my_point's x coordinate is", my_point.x)  # 210
    print("my_point's y coordinate is", my_point.y)  # 130

    print("my_point is:", my_point)  # my_point is: MyPoint(210, 130)


def test_point():
    p = Point(100, 50)
    print("p is of type:", type(p))  # <class 'graphix.Point'>
    print("p's x coordinate is", p.x)  # 100
    print("p's y coordinate is", p.y)  # 50

    p.move(10, -20)
    print("p's x coordinate is", p.x)  # 210
    print("p's y coordinate is", p.y)  # 130

    print("p is:", p)  # p is: Point(210, 130)
