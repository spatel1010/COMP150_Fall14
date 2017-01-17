#happyBirthdayInput.py
#Shivam Patel
#COMP-150
#A happy birthday program with multiple functions

def birthdayInput() :
    perons = input("Please enter the person you wish to sing happy birthday to: " )
    age = input("How old are you today? ")
    present = input("What would you like for your birthday?")
    
def happyBirthday(person):
    person = input('Please enter the person you wish to sing happy birthday to: ')
    print('Happy birthday to you!')
    print('Happy birthday to you!')
    print('Happy birthday dear', person)
    print('Happy birthday to you')

def birthdayAge():
    age = input('How old are you today?')
    print('I hope your', age, 'birthday is a great one!')

def main():
    name = input("enter the name of the person you wish to sing to: ")
    birthdayInput ()
    happyBirthday(name)
    birthdayAge()

main()
