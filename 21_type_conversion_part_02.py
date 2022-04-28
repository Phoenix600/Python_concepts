# Import modules here 
import math 

# Moderate tpye conversion in Python 

#-----------------------------------------------------
# Converting or typecasting list into set 
#-----------------------------------------------------
sample_list  = ["H","E","L","L","O"]
# Now the smaple_list has been converted into set 
sample_set   = set(sample_list)
print(sample_set)

#------------------------------------------------------
# Converting or typecasting set into list
#------------------------------------------------------
sample_set = {2-3j,2+3j}
sample_list = list(sample_set)
print(sample_list)

#------------------------------------------------------
# Converting or typecasting tuple int list
#------------------------------------------------------
# number set
sample_tuple = ('R','Z','Img','W')
sample_list = list(sample_tuple)
print(sample_list)

#------------------------------------------------------
# Converting or typecasting set into tuple
#------------------------------------------------------
# Set of trigono metric function values at 0 degrees 
sample_set = {math.asin(0),round(math.acos(0.55),3)}
sample_tuple = tuple(sample_set)
print(sample_tuple)


#------------------------------------------------------
# Typecasting mult-pair list into dictionary
#------------------------------------------------------
sample_list0    = ['Name', 'Pranay']
sample_list1    = ['Age', 19]
sample_list2    = ['Intrest', 'Designing']
sample_list_set = [sample_list0,sample_list1,sample_list2]
sample_dictionary = dict(sample_list_set)
print(sample_dictionary)
print(sample_list_set)







