# Import all your modules here 
# <---------- Here ----------->

int_num = 12
bool_flag = False
float_num = 12.12
complex_num = 12 + 17j

"""
 Every data-type in python is a class and variable is instance of class or aka object.
 To check data-type class information , we use @type() function
 Similarly @isinstance() function is used to check if object belongs to a particular class or 
 not
"""
print(type(int_num))
print(type(float_num))
print(type(bool_flag))
print(type(complex_num))



# Checking whether the data type belongs to particular class or not  using @isinstance() funciton
print(isinstance(int_num,int))
print(isinstance(float_num, float))
print(isinstance(bool_flag,bool))
print(isinstance(complex_num,complex))
