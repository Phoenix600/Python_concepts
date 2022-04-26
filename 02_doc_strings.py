# This is the place where you import all your modules at begining of py doc

import pickle


def addNum(a, b) :
    """
    @addNum() returns the sum to two numbers : 
        Parameters : 
            a (int) : A decimal integer
            b (int) : A decimal integer 
        Returns :
            Decimal sum of two intgers 
    """
    return (int(a+b))


print(addNum(12,13))

bool_choice = False
bool_choice = bool(input("[+]Type True to print the documentation of @addNum() :"))

if bool_choice == True :
    print(addNum.__doc__)

