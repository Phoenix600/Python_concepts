int_a = 5
print(float(int_a))

float_b = 12.12
print(float_b)
print(int(float_b))

bool_c = False
print(bool_c)
print(int(bool_c))

"""
True and False are evaluated into 1 and 0 respectively 
"""
bool_d = True
print(bool_d)
print(int(bool_d))


## String can not be typecasted into integers directly
#string_e = "Hello"
#print(string_e)
#print(int(string_e[0]))


# To print the ascii value of any charcter use @ord() function , 
# which will convert the charcter to its character value
print(ord('d'))

string_demo = "HeloHelo"
#print(ord(string_demo))
#@ord() function require character to print it's asci value , if you pass the whole string, it will throw an error

