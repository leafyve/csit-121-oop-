from math import pi, radians, cos, sin

class Circle:
    def __init__(self,a,b,r,angle):
        self.a = a
        self.b = b
        self.r = r
        self.angle = angle

    def get_a(self):
        return self.a

    def get_b(self):
        return self.b

    def get_r(self):
        return self.r

    def get_angle(self):
        return self.angle

    def set_a(self,a):
        self.a = a

    def set_b(self,b):
        self.b = b

    def set_r(self,r):
        self.r = r

    def set_angle(self,angle):
        self.angle = angle

    def __str__(self):
        return f'Point({self.a}, {self.b})'


def test_point():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    r = int(input("Enter radius: "))
    angle = int(input("Enter angle: "))
    p1 = Circle(a,b,r,angle)
    print(f"Area and Circumference:", calculate_circle(p1))
    print(f"Point X and Y", calculate_xy(p1))

def calculate_circle(self):
    area = self.r * self.r * pi
    circumference = self.r * 2 * pi
    return area,circumference

def calculate_xy(self):
    x = self.r * cos(radians(self.angle))
    y = self.r * sin(radians(self.angle))
    return x,y

def main():
    test_point()

if __name__ == '__main__':
    main()