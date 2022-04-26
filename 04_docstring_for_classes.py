# Import your modules here :

# class
class Person :
    """
    A class reprsents a person 
    ''' 
    [Attributes] 
    Name : str
        first name of the person
    Surname : str
        Family name of the person 
    Age : int
        Age of the person 

    {Methods} 
    info(addtionl=""):
        prints the person's name and age.
    """
    def __init__(self,name,surname,age):
        """
        Constructs all the neccessary attributes for the person object
        """
        self.name = name 
        self.surname = surname
        self.age = age
    
    def info(addtional=""):
        """ Prints the person's information """
        print(f'''
        [1] Name        :   {self.name}
        [2] Surname     :   {self.surname}
        [3] Age         :   {self.age}
        ''')
