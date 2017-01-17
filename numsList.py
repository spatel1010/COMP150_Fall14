#3
#Shivam Patel

nums = [ ]
start = int(input("Enter first number: "))
end = int(input("Entet second number: "))
if start < end:
    while start != end:
        nums.append(start)
        start = start + 1
elif start > end:
    while start != end:
        nums.append(start)
        start = start - 1
else:
    print("No numbers added")
print(nums)


            
