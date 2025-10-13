# The application that uses Note and Notebook classes
from lab2 import Note, Notebook

def main():
    nb = Notebook()
    nb.load()
    menu = '1 Show\n2 Add\n3 Search\n4 Quit'
    while True:
        print(menu)
        option = int(input('Choose and option: '))
        if option == 4:
            break
        elif option == 1:
            print(nb)
        elif option == 3:
            keyword = input('Search Keyword: ')
            result = nb.search(keyword)
            if len(result) == 0:
                print('No results found')
            else:
                for n in result:
                    print(n)

    print("End of main")

if __name__ == '__main__':
    main()
