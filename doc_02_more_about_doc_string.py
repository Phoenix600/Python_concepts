# You can aslo rea the doc_string using the @help(<query>) function

class Person :
    """
    A class to represent the person .

    ...

     ATTRIBUTES 
    -------------
    name        : str 
                    first name of the person 
    surname     : str
                    family name of ther person 
    age         : int 
                    Age of the person 

     METHODS 
    ---------
    info(addtional="") :
        Prints the persons name and age 
    """

    def __init__(self,name,surname,age) : 
        """
        Constructs all the neccessary attributes for the person object 

        PARAMETERS
        ----------
        name        : str 
                        first name of the person
        surname     : str 
                        family name of ther person
        age         : int
                        age of the person

        """
        self.name       = name 
        self.surname    = surname
        self.age        = age



print(help(Person))
