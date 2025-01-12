class Car:

    def __init__(self, colour):
        self.colour = colour
        self.speed = 0

    def accelerate(self, value):
        if self.speed + value <= 60:
            self.speed += value

    def brake(self):
        self.speed = 0

    def __str__(self):
        output = f"A {self.colour} car"
        output += f" going at {self.speed} mph"
        return output


def test_car():
    my_car = Car("red")

    my_car.accelerate(30)
    my_car.brake()

    print(my_car.colour)  # red
    print(my_car.speed)  # 0

    my_car.colour = "blue"
    print(my_car.colour)  # blue

    print(my_car)  # A blue car going at 0 mph


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


def test_my_point():
    point_a = MyPoint(1, 2)
    point_b = MyPoint(3, 4)

    print(point_a.x)  # 1
    print(point_b.y)  # 4

    point_a.x = 5
    print(point_a.x)  # 5

    point_b.move(2, -2)
    print(point_b.x)  # 5
    print(point_b.y)  # 2

    print("point_a:", point_a)  # MyPoint(5, 2)
    print("point_b:", point_b)  # MyPoint(5, 2)
