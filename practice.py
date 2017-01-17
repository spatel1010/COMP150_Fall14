li = range(0,21)
for num in li:
    print('I <3 Programming')

def sumList(nums):
    total =0
    for num in nums:
        total = total * num
        
    return total

def main():
    totalOut = sumList([1,2,3,5])
    print("The total is: ", totalOut)

main()
    
