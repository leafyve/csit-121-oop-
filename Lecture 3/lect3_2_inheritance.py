# Inheritance: method
# Methods defined in the base class they become available in the subclass
# Whatever you define in base class, become the same in subclass

class DemoA:
    def method_a(self):
        print('method_a')
    def __str__(self):
        return f'{type(self).__name__} {id(self)}' # type give you back the class
        # instead of hardcoding a use the type function to give oyu exact class of the object

class DemoB(DemoA): # bracket meaning DemoB is a subclass of DemoA
     pass # you don't add any methods or attributes
    # def __str__(self):
    #     return f'DemoB {id(self)}' # override closer

class DemoC(DemoB):
    def method_c(self):
        print('method_a')
    # def __str__(self):
    #     return f'DemoC {id(self)}'

def main():
    a = DemoA()
    a.method_a()
    print(a)

    b = DemoB()
    b.method_a() # methods in a now in b
    print(b) # no str method in B but still shows str because of DemoA
    # python went to DemoA to use str method

    c = DemoC()
    c.method_a()
    c.method_c() # keeps passing down
    print(c) # it will continue the path through b then a for str method

if __name__ == '__main__':
    main()