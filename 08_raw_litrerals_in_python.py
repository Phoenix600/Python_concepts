# Import your modules here 

a = 0b1010   # Binary Raw data or Binary Literal
b = 100      # Decinal Literal 
c = 0o310    # Octal Literal 
d = 0x12c    # Hexa decimal Literal 
e =  14 + 3.14j
f = 2+10e3

print(a)
print(b)
print(c)
print(d)
print(f)
print(f'''
        [COMPLEX NUMBER] :          {e}
        [REAL PART]      :          {e.real}
        [IMAGINARY PART] :          {e.imag}
        ''')

