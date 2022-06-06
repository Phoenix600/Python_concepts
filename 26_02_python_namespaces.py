'''
Everything in python is Object and name is a way to access the underlying objects
'''
a = int(2)
b = a
print("The memory address of var a is ",id(a))
print("The memory address of var b is ",id(b))

b = int(3)
a = int(2)

print("The memory address if var a is ", id(a))
print("The memory address if var b is ", id(b))
