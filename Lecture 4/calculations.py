class Calculations:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_sum(self):
        """Returns the sum of a and b"""
        return self.a + self.b

    def get_difference(self):
        """Returns the difference between a and b (a - b)"""
        return self.a - self.b

    def get_product(self):
        """Returns the product of a and b"""
        return self.a * self.b

    def get_quotient(self):
        """Returns the quotient of a divided by b (a / b)"""
        return self.a / self.b