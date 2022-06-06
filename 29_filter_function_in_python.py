# import your modules here 

# Define your functions here 


# Write your code here 
# getting started with filter function 

my_list = [1,2,3,4,5,6,7,8,9,10]

print(my_list)

my_list = list(filter(lambda x : (x%2 == 0), my_list))

print(my_list)


''' More about filter funtion
    filter(arg1,arg2)       :   @filter() takes two args. First arg as funtion and other as list 
'''
