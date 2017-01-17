# phonebook.py
# Shivam Patel
# COMP 150

def createDict():
    book = dict()
    book['Capone'] = 7735557447
    book['Vonnegut'] = 9175554525
    book['Einstein'] = 6095557676
    book['Hemingway'] = 2085554657
    return book

def main():
    phonebook = createDict()
    name = input("Enter the last name of person you would like to call ")
    number = (phonebook[name])
    print("The phone number for", name, "is", number)

main()
