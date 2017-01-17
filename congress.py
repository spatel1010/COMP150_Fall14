#congress.py
#Shivam Patel

print("Are you elible to be a U.S. Senator or Representative? ")
age = int(input("What is your age: "))
citizen = int(input("How long have you been a U.S. citizen: "))
if age >= 30 and citizen >= 9:
    print("You are eligible for both House and Senate!")
elif age >=25 and citizen >= 7:
    print("You are elgible for the House only")
else:
    print("You are not eligible for either the House or Senate.")
