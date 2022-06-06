# import your modules here 
import numpy as np

# define functions here 
def sampleFunction():
    pass

# write main code here 

'''
In this code file we are going to learn List Comprehnsion which offers a shofter syntax when you
want to create a new list based on the values of new list 
'''
my_fav_fruits_list = ["Apple","Banana","Cherry","Kiwi","Mango","Peach","Strawberry"]

for fruit in my_fav_fruits_list :
    print(f"Pranay's favorite food is {fruit}")


print("Pranay DON'T eat all these : ")

'''
[+] we have this previous lists and we want to create the new list as follows 
    A) The new list will contain only fruits with the letter "a" in the name 
    without list compression you will have to write a for statement with
    conditional test inside.
'''


# empty list to add list elements acc. to condtions
only_eats = []

'''
Sometimes writing this kinda boring and doesn't trigger your mind,
**** python provides comprehension techniques to make your code more shorter ****
'''

for fruit in my_fav_fruits_list :
    if 'a' in fruit :
        only_eats.append(fruit)


for eats in only_eats :
    print(f"Pranay only eats {eats}")


''' List Comprehnsion Syntax '''
'''List = [exp for item in iterable_list_or_sequence if condition == True]'''

my_phones = ['BlackBerry','Samsung','iphone','Nokia','Oppo','Vivo']

old_phones = [x for x in my_phones if 'o' in my_phones]
print(old_phones)
