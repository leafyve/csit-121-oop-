class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def __str__(self):
        return f"Rectangle: {self.__length} x {self.__width} Area = {self.area()}"


def printList():
    rectList = [Rectangle(1, 2), Rectangle(3, 4), Rectangle(5, 6)]
    for i in range(len(rectList)):  # access each object in a list
        print(rectList[i])
    for rect in rectList:  # another way of accessing each object in a list
        if rect.area() <= 10:
            print(rect)


def printDict():
    data = [
        {"length": 1, "width": 2},
        {"length": 3, "width": 4},
        {"length": 5, "width": 6},
        {"length": 7, "width": 8},
        {"length": 9, "width": 10}
    ]  # create a list of dictionaries

    # create a list of Rectangle objects using the values in data list
    rectList = []

    # create Rectangle objects and add to rectList
    for i in data:
        length = i["length"]
        width = i["width"]
        temp = Rectangle(length, width)
        rectList.append(temp)
        # combine 2 statements
        rectList.append(Rectangle(i["length"], i["width"]))

    # another way is
    for rect in rectList:
        print(rect)  # when print an object, python will look for __str__()

def main():
    # Call functions to print output
    printList()
    printDict()
    print(Rectangle(10,6))

if __name__ == '__main__':
    main()