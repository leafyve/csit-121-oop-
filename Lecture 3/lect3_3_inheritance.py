# Inheritance: init
# must put in the correct statement to call the constructor of the base class

class DemoA:
    def __init__(self):
        self.__a = 10
        print(f'** DemoA.init {id(self)}') # if anything missing will look for first class that has constructor

    def __str__(self):
        return f'DemoA {id(self)}'
class DemoB(DemoA):
    def __init__(self):
        super().__init__() # everyone gets to call the methods
        self.__b = 20
        print(f'** DemoB.init {id(self)}') #

    def __str__(self):
        return f'DemoB {id(self)}' # they call all the same constructor (same object id)
class DemoC(DemoB):
    def __init__(self):
        super().__init__() # super function give you reference to base class, call the init method in base class
        # inside C we manage to call the constructor of B
        self.__c = 30
        print(f'** DemoC.init {id(self)}')

    def __str__(self):
        return f'DemoC {id(self)}' # rightfully every class will have its own constructor

def main():
    a = DemoA()
    print(a)
    b = DemoB()
    print(b)
    c = DemoC()
    print(c) # C now has ABC attributes
    # Print the attributes in each object
    print(vars(a)) # function vars give you the attributes in the class
    print(vars(b)) # function id give you id
    print(vars(c)) # function type gives you the class
    # Output:
    # {'_DemoA__a': 10}
    # {'_DemoB__b': 20}
    # {'_DemoC__c': 30} # but you want to initialize the base class attributes as well so use super

if __name__ == '__main__':
    main()