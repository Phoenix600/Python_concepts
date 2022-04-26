# Getting started with python 
# This is a single line comment 

# This is the place where you import all the modules 
import pickle

print(pickle.__doc__)

""" This is how we write multi-line comment in python 
    still don't belive it, but it works 
"""
 
""" These tripple quote are used for multiline quotes  : 
     A perfect example of multiline comments"""

print("Hello python, How are you?,It's been 3 years and I still hate you")


""" 
    doc-strings in python  : A docstring is short for Documentation String
    Python doc strings appear right after the defination of the function, method, class or module 
"""

def double_val (num) :
    """ @double_val() function to double the value of passed number """
    return 2*num
print(double_val.__doc__)

print("Before passing to double_val()",2)
print(double_val(2))


print(print.__doc__)



