#Program to convert Inches to Centimeters
#Author: Shivam Patel


print('This program converts a measurement in',
		   'Inches to Centimeters.')
def i2c():
    i = int(input('Enter a measurement in Inches: '))
    c = i*2.54
    print('This measurement in centimeters is: ', c)
    
def main():
    i2c()
    input('press Enter to end this program')

main()
