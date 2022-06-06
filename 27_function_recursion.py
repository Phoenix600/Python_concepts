def FACT(n) :
    if n == 1:
        return 1
    else :
        return n*FACT(n-1)

print(FACT(5))
