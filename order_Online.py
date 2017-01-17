#order_Online.py
#Shivam Patel

print("Welcome to Restaurant")
print("Menu:")
print("Fries")
print("Burger")
print("Wrap")
print("Soda")
print("1.Order delivery")
print("2.Order pickup")
print("3.Exit")

choice = 0
while choice != 3:
    choice = int(input("Enter order method (1,2 or 3): "))
    if choice == 1:
        address = input("Enter your delivery address")
        order = input("Enter your order")
        print( order, "needs to be delivered to", address)
    elif choice == 2:
        order = input("Enter your order")
        print(order,"will be picked up")
    else:
        print("Order canceled")
        
                 
