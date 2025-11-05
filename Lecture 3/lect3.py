# list of objects
def test1():
    r = range(3)
    list1 = list(r)
    print(type(r))
    print(type(list1), list1)
    list2 = list('123abc')
    print(type(list2), list2)

def test2():
    list1 = [1, 2, 3]
    list2 = list(list1)
    print(id(list1))
    print(id(list2))
    for v in list1:
        print(id(v), end=' ')
    print()
    for v in list2:
        print(id(v), end=' ')
        print()
    list1[0] += 100
    list2.append(200)
    # Check
    # [101, 2, 3]
    # [1, 2, 3, 200] comes this out because lists are immutable
    # the other list won't change, protected
    # classes of list are not protected
    print(list1)
    print(list2)
#############
class Demo:
    def __init__(self, value):
        self.__value = value

    def set_value(self, value):
        self.__value = value

    def __str__(self):
        return f'[{id(self)}] {self.__value}'
#############
def test3():
    list1 = [Demo(10), Demo(20)]
    list2 = list(list1)
    for values in list1:
        print(values, end=' ')
    print()
    # [1348180190720] 10 [1348180190912] 20 two objects
    # one contain 10 and other 20
    for values in list2:
        print(values, end=' ')
    # Output:
    # [1390905730992] 10 [1390905731184] 20
    # [1390905730992] 10 [1390905731184] 20
    # two list pointing to an object each one is a demo object
    # demo object is not immutable
    print()
    # Make changes, changing one of the values of the object
    list1[0].set_value(-1)
    list2.append(Demo(200))
    for values in list1:
        print(values, end=' ')
    print()
    # [1348180190720] 10 [1348180190912] 20 two objects
    # one contain 10 and other 20
    for values in list2:
        print(values, end=' ')

    # output:
    # [2226465942528] -1 [2226465943056] 20
    # [2226465942528] -1 [2226465943056] 20 [2226465943104] 200
    # when create new object then different address
    # if change int or str still maintain address

def main():
    # test1()
    # test2()
    test3()

if __name__ == "__main__":
    main()