#BrokenBank
#Shivam Patel
#COMP-150

balance = 1000

print('Welcome to your friendly local bank')
first = input("Please enter your first name")
last = input('Plese enter your second name')
accnt = input('What is your account number?')
cash = input('How much money would you like?')
cash = cash*5

fullName = first + last
print('Here you go fullName, here is', cash,'dollars')
print('Your remaining balance is', balance-cash)
print('Have a wonderful day!')
input('Press any key to end program')
