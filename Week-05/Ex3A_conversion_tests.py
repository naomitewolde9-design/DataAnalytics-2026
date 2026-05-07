# Description: This script tests various numeric 
# conversion techniques
# Author: Sam Q. Newprogrammer

a = " 101.1 " # <class 'str'>
b = '55'      # <class 'str'>
c = "402 Stevens"  # <class 'str'>
d = 'Number 5 '    # <class 'str'>

#Value types: 
print(a)
print(type(a))
print()
print(b)
print(type(b))
print()
print(c)
print(type(c))
print()
print(d)
print(type(d))
print()


# Fixing a with error: (a)

af = float(a) # works
anf = int(float(a)) # works

slic_a = a[1:6] # works 101.1 without any spacing (used slicing)
print(float(slic_a)) 
print(slic_a)

# a_int = int(a) ValueError: invalid literal for int() with base 10: ' 101.1 '
print(a.strip()) #101.1, removing the leading and trailing spaces 


# Fixing with errors: (b)

bf = float(b) # works
bif = int(float(b)) # works

slic_b = b[0:3] # works
print(int(slic_b)) # works 
print(slic_b) # works 55, without the qoutations 


# fixing with errors: (c)

# cf = float(c) ValueError: could not convert string to float: '402 Stevens'
# cif = int(float(c)) ValueError: could not convert string to float: '402 Stevens'

slic_c = c[0:4] #works
print(int(slic_c)) # works
print(slic_c) # works, 402 


# Fixing with error: (d)

# df = float(d) ValueError: could not convert string to float: 'Number 5 '
# dif = int(float(d)) ValueError: could not convert string to float: 'Number 5 '

slic_d = d[7:9] # works
print(slic_d) # works, 5
print(int(slic_d)) # works
print(d.strip()) # work, Number 5