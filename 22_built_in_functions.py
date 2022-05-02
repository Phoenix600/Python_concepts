# import your modules here
from datetime import datetime


print(1,2,3,4,5,6, sep = "#", end = "*" "\n")

nowTime = datetime.now()
x = 5; y = 10
print(x)
print(y)

''' To mamke our output attractive or swapping the strings we use .format(str_A_Object,str_B_Object) '''

print("I like {0} more than {1} ".format("Tea","Coffee"))
print("I like {0} more than {1} ".format("Coffee","Tea"))
print("I like {1} more than {0} ".format("Coffee","Tea"))

string_var = (input("[+]Enter your name : "))

print("Hello {name}, {greeting}, Its almost {time}".format(name = string_var,greeting = "Have a great day!!,", time = nowTime))

