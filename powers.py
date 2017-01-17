#powers.py
#Shivam Patel
#COMP 150
    

def power(x,num):
    for number in range(num):
        print("The", number, "power of", x, "is", x**number )

    
def main():
    x = int(input("Enter first number "))
    num = int(input("Enter second number "))
    power(x,num)

main()
