#Getting started with tuple in python 
'''
Tuple is an ordered sequence of items same as list, the only diffrence that tuple is immutable means tuple
can not be modified once created 
'''

tuple_final_marks = (56,78,98,100,78)
print(tuple_final_marks)

# Printing tuple via range 
print("Tuple can be printed via range tuple[0:3] : ",tuple_final_marks[0:3])

# tuple can not be modified , if you do try it will give you error 
# tuple are inmmutable
#tuple_final_marks[0] = 90
