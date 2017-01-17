#numDict

def createDictionary ():
    x=7
    numDict = dict()
    numDict['one'] = 1
    numDict['two'] = 2
    return numDict
def main():
    dictionary= createDictionary()
    print(dictionary['one'])
    print(dictionary['two'])
    fmtString = 'Replace the numbers {one}, {two}' 
    newString = fmtString.format(**dictionary)
    print(newString)
main()
