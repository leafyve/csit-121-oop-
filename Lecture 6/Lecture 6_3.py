# User defined exception
class TemperatureException(Exception):
    pass

def main():
    while True:
        try:
            value = input('Enter temperature or enter 0 to exit: ')
            temp = int(value)
            if temp < 0:
                break
            if temp > 40:
                raise TemperatureException(f'Temperature {temp} is > 40')
            print(f'Temperature {temp} is recorded')
        except ValueError as err:
            print(f'Invalid value {value}')
            print(err)
        except TemperatureException as err: # handling different exceptions in one trp except block
            print(err)
if __name__ == '__main__':
    main()