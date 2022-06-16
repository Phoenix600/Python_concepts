# import your modules here 
import sys
import mymodules

'''
While importing the modules, python looks at several places  :
        1. Looks for a built-in-modules 
        2. If module no found, then interpreter looks in directory defined
           in the sys.path
                
                Searching Order :   
                ----------------
                        1. The current directory 
                        2. PYTHONPATH (ENV where the list of directories)
                        3. The installation-dependent default directory 

'''
print(sys.path)
