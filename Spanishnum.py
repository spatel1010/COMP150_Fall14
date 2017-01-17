"""A tiny English to Spanish dictionary is created,
        using the Python dictionary type dict.
        Then the dictionary is used, briefly.
        """
def createDictionary():
    """Returns a Spanish dictionary"""
    spanish = dict() # creates an empty dictionary
    spanish['1'] = 'uno'
    spanish['2'] = 'dos' 
    spanish['3'] = 'tres'
    spanish['4'] = 'cautro'
    spanish['5'] = 'cinco'
    spanish['6'] = 'seis'
    spanish['7'] = 'siete'
    spanish['8'] = 'ocho'
    spanish['9'] = 'nueve'
    spanish['10'] = 'diez'
    spanish['11'] = 'once'
    spanish['12'] = 'doce'
    return spanish
def main():
    dictionary = createDictionary()
    print(dictionary['1'])
    print(dictionary['2'])
    c = '3'
    print(dictionary[c])
    d = input("input number :")
    print()
    print(dictionary[d])
print('Want to learn how to count in Spanish?')
main()
