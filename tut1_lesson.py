from math import sqrt

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x
X
    def get_y(self):
        return self.y

    def set_x(self,x):
        self.x = x

    def set_y(self,y):
        self.y = y

    def get_distance(self):
        sum_sq = self.x**2 + self.y**2
        return sqrt(sum_sq)

    def __str__(self):
        return f'Point({self.x}, {self.y})'

    def __eq__(self, other): # comparing points eq = equal
        return (self.get_x() == other.get_x() and
                self.get_y() == other.get_y())

################
class Circle:
    def __init__(self,radius, x, y):
        self.radius = radius
        self.center = Point(x,y)

    def __str__(self):
        return f'Circle with radius {self.radius} at {self.center.__str__()}'

    def __eq__(self, other):
        return (self.radius == other.radius
                and self.center == other.center)
############
def test_equal_circle():
    c1 = Circle(1,1,1)
    c2 = Circle(2,1,1)
    c3 = Circle(2,1,1)
    print(c1 == c2)
    print(c2 == c3)


def test_circle():
    c1 = Circle(2, 1, 2)
    print(c1)

def test_equal():
    p1 = Point(1,2)
    p2 = Point(1,2)
    p3 = p2
    print(p1 == p2) # p1.__eq__(p2)
    print(p2 == p3) # p2.__eq__(p3)
    print(p3 == p1)


def test_point():
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    p1 = Point(x,y)
    print(p1)
    print(p1.get_x()) # method .get()
    print(p1.get_distance())

def main():
    # test_point()
    # test_equal()
    test_circle()
    test_equal_circle()

if __name__ == '__main__':
    main()