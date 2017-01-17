print('This program returns the sum of the numbers contained in a list')

def sumList(nums):
    total =0
    for num in nums:
        total = total+num
        
    return total

def main():
    totalOut = sumList([10,2,4,3])
    print("The total is: ", totalOut)

main()
    
