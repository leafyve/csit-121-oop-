# try except + loop

def test1():
    total = 0
    try: # using try statement to prevent user from entering anything but int that will affect loop
        while True:
            num = int(input('Enter a number: '))
            if num < 0:
                break
            total += num
        # After loop
        print(f'total is {total}')
    except ValueError as err: # invalid literal for int() with base 10: 'e'
        print(err)

    print('End of test1')

def test2():
    total = 0
    while True: # try except inside a while loop to ensure that exception happen the loop continues
        try:
            num = int(input('Enter a number: '))
            if num < 0:
                break # the loop only stopped with a negative number
            total += num
        except ValueError as err:
            print(err)
    # After while loop
    print(f'total is {total}') # don't want to keep printing the number in the while loop

    # nested try except wrapped around original try except block to catch other potential errors

    print('End of test1')

def main():
    # test1()
    test2()

if __name__ == '__main__':
    main()