from datetime import date

class Note:
    # Initialize the next ID as a class variable
    __next_id = 1  # Class variable to keep track of the next ID

    def __init__(self, tag, memo):
        self.__tag = tag
        self.__memo = memo
        self.__create_date = date.today()
        self.__id = Note.__next_id  # Use class variable to assign ID
        Note.__next_id += 1  # Increment the class variable for the next Note

    def get_tag(self):
        return self.__tag
    def get_memo(self):
        return self.__memo

    def __str__(self):
        return f'{self.__id} {self.__tag} {self.__memo}'

    def __eq__(self, other):
        if other is None:
            return False
        if isinstance(other, str):  # Check if 'other' is a string
            return False  # Or define behavior for comparing with strings if needed
        return (self.__tag == other.__tag and self.__memo == other.__memo)

##############################################################################
class Notebook:
    def __init__(self):
        self.__notes = []

    def add_note(self, tag=None, memo=None, note_obj=None):
        if note_obj is None:
            new_note = note_obj
        else:
            new_note = Note(tag, memo)
        if new_note in self.__notes:
            return False
        else:
            self.__notes.append(new_note)
            return True
    def __str__(self):
        output = ''
        for n in self.__notes:
            output += str(n) + '\n'
        return output

    def load(self):
        data = [['Work', 'Team meeting on Friday'],
                ['Work', 'Assignment due soon'],
                ['Friend', 'Ball game this week'],
                ['Friend', 'Movie'],
                ['Home', 'Visit relatives']]
        for value in data:
            self.__notes.append(Note(value[0], value[1]))

    def search(self, keyword):
        search_results = []
        for n in self.__notes:
            if keyword in n.get_tag() or keyword in n.get_memo():
                search_results.append(n)
        return search_results

##############################################################################
def test_search():
    nb = Notebook()
    nb.load()
    print(nb)
    print('Search for keyword Work')
    result = nb.search('Work')
    for n in result:
        print(n)

    nb.search('Assignment')
    print("Search for keyword Assignment")
    result = nb.search('Assignment')
    for n in result:
        print(n)

    nb.search('xxx')
    print("Search for keyword xxx")
    result = nb.search('xxx')
    for n in result:
        print(n)


def test_Notebook():
    nb = Notebook()
    # Add Note Object to the Notebook object
    nb.add_note("Work", "Friday 10am meeting")

    n1 = Note("School Work", "Start working on assignment 1")
    nb.add_note(note_obj=n1)
    nb.add_note(note_obj=n1)
    print(nb)
    nb.load()
    print(nb)


def test_note():
    n1 = Note('School Work', 'Start working on assignment 1')
    n2 = Note('School Work', 'Prepare for test ')
    n3 = Note('School Work', 'Prepare for test ')
    print(n1)
    print(n2)
    # Compare objects
    print(n1 == n2)
    print(n2 == n3)
    print(n2 == None)
    print(n2 == "hello python")

def main():
    # test_note()
    # test_Notebook()
    test_search()
    print("End")

if __name__ == '__main__':
    main()
