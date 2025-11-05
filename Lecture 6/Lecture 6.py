
def try_escape_sequence():
    try:
        print('try block starts')
        num = int(input('Number: '))
        result = 10/ num
        print(f'result is {result:.2f}')
        # return 'try block return something' # meaningless because the else part is skipped, but cannot skipp finally
        print('try block end')
    except(ValueError, ZeroDivisionError) as err:
        print(err)
        return 'return statement in the except block' # finally block still e
    else:
        print('else block is executed')
        # return 'else block return something' # else and finally block still executes
    finally:
        print('finally block is executed')


def main():
    try_escape_sequence()

if __name__ == '__main__':
    main()