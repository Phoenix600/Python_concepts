# import moudles here
import imp 
import sys
import myFunctionModules
"""DOC string for myFunctionModules """
print(f"All namespaces in our current python script are : {dir()}")
print(f"Namespaces in module {myFunctionModules.__name__} are {dir(myFunctionModules)}")
