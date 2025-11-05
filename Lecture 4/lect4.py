# Inheritance

"""
Base class: Vehicle: license_plate, capacity
                    str, get_road_tax ($1.5 per cc)
Subclass: Bus: reg_no
            get_road_tax: <= 3000 CC 70%
                            above 60%
"""
class Vehicle:
    __dollar_per_cc = 1.5 # class variable

    def __init__(self, license_no, capacity):
        self.__license_no = license_no
        self.__capacity = capacity

    def get_license_no(self):
        return self.__license_no
    def get_capacity(self):
        return self.__capacity
    def get_road_tax(self):
        return self.__capacity * Vehicle.__dollar_per_cc
    def __str__(self):
        return f'{self.__license_no} {self.__capacity} ${self.get_road_tax():.2f}'
    def __eq__(self, other): # two vehicles are the same if they have the same license plate number
        if other is None:
            return False # nothing don't need to compare
        if not isinstance(other, Vehicle):  # reference to vehicle class
            return False  # Or define behavior for comparing with strings if needed
        return self.__license_no == other.__license_no

class Bus(Vehicle): # can inherit from multiple classes
    def __init__(self, license_no, capacity, reg_no):
        super().__init__(license_no, capacity) # calling init method from base class
        self.__reg_no = reg_no # attributes only applicable to a bus

    def get_reg_no(self):
        return self.__reg_no

    def get_road_tax(self):
        # if Vehicle.get_capacity(self) <=3000:
        #     return Vehicle.get_road_tax(self) * 0.6 # you are calling your own self
        original = super().get_road_tax() # calling a method you are overriding
        if self.get_capacity() <= 3000: # this method is defined in base class, you inherit it
            return original * 0.7 # assign back
        else:
            return original * 0.6 # assign back
        # return original # calculating the result but throwing away the result, not assigning to original


##########
def test_all():
    all_vehicles = []
    data = [['v1', 3000],
            ['v2', 2000],
            ['v3', 3000, "r3"],
            ['v4', 4000, "r4"],
            ['v5', 1800],
            ['v5', 1800],
            ['v6', 2000]] # nested list
        # Create Vehicle or Bus object from each sublist
        # Add the object to all_vehicle
        # Do not add duplicate objects
    for value in data:
        # if vehicle

def test_bus():
    b1 = Bus("b1", 3000, "r1")
    print(b1) # str method will call the get road tax method in the subclass instead of baseclass as this is a Bus object, override
    b2 = Bus("b1", 3000, "r1")
    print(b1 == b2) # criteria of comparing bus based on license number from eq method in base class

def test_vehicle():
    v1 = Vehicle("v1", 3000)
    print(v1)
    v2 = Vehicle("v1", 4000)
    print(v1 == v2)

def main():
    # test_vehicle()
    # test_bus()
    test_all()
    print('End')

if __name__ == '__main__':
    main()