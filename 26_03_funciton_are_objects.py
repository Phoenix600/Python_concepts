# in Python funcitons are also objects 

def Fact(x) :
    if x == 1:
        return x
    return x * Fact(x-1)

factorial = Fact
print(factorial(5))
