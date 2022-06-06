''' Python provides special two type of operators  
    1. Identity Operator    is , is not
    2. Membership OPerator 

'''

# Identity Operator in Python 

old_pass = "Nahi_Mahit"
new_pass = "Nahi"+ "_" + "Mahit"


my_org_pass = "This is not a password, it is my privacy"
print(old_pass is new_pass)

print(old_pass is not my_org_pass)


# Membership Operators 
'''     'in' and 'not in' are the membership operator in python . They are used to test or check whether 
        the elements or variable or value is present in a sequence or not 

        In python we reffer string,list,tuple,set and dictionary as seqence 
'''

message = "How are you?"

bool_result = '?' in message 

print(bool_result)

sample_list = ['pranay','single','150+',20]
bool_reult = 'single' in sample_list
print(f"Single Status  : {bool_result}")

dict_x = {1: 'a',2:'b'}
print('H' in dict_x)
print(1 in dict_x)





