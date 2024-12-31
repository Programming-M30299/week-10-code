from graphix import Point


class MyPoint:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        output = f"MyPoint({self.x}, {self.y})"
        return output


class Square():

    def __init__(self, p1, side):
        self.p1 = p1
        self.side = side
        self.p2 = MyPoint(p1.x + side, p1.y + side)
        self.fill_colour = "white"
        self.outline_colour = "black"

    def move(self, dx, dy):
        self.p1.move(dx, dy)
        self.p2.move(dx, dy)

    def __str__(self):
        output = f"Square({self.p1}, {self.p2})"
        return output


def test_square():
    p1 = MyPoint(100, 50)
    square = Square(p1, 50)

    print("square's side length is", square.side)  # 50
    print("square's p1 is", square.p1)  # MyPoint(100, 50)
    print("square's p2 is", square.p2)  # MyPoint(150, 100)

    square.move(10, -20)

    print("After the move ...")
    print("square's side length is", square.side)  # 50
    print("square's p1 is", square.p1)  # MyPoint(110, 30)
    print("square's p2 is", square.p2)  # MyPoint(160, 80)

    print(square)  # Square(MyPoint(110, 30), MyPoint(160, 80))

    print("Changing square's fill colour default (white) to red ...")
    square.fill_colour = "red"
    print("square's fill colour is", square.fill_colour)  # red


def test_my_point():
    my_point = MyPoint(100, 50)
    print("my_point's x coordinate is", my_point.x)  # 100
    print("my_point's y coordinate is", my_point.y)  # 50

    my_point.x = 200
    my_point.y = my_point.y + 100
    print("my_point's x coordinate is", my_point.x)  # 200
    print("my_point's y coordinate is", my_point.y)  # 150

    my_point.move(10, -20)
    print("my_point's x coordinate is", my_point.x)  # 210
    print("my_point's y coordinate is", my_point.y)  # 130

    print("my_point is:", my_point)  # my_point is: MyPoint(210, 130)


def test_point():
    p = Point(100, 50)
    print("p is of type:", type(p))  # <class 'graphix.Point'>
    print("p's x coordinate is", p.x)  # 100
    print("p's y coordinate is", p.y)  # 50

    p.x = 200
    p.y = p.y + 100
    print("p's x coordinate is", p.x)  # 200
    print("p's y coordinate is", p.y)  # 150

    p.move(10, -20)
    print("p's x coordinate is", p.x)  # 210
    print("p's y coordinate is", p.y)  # 130

    print("p is:", p)  # p is: Point(210, 130)
