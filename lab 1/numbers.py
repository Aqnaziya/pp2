#examples
x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))

#Floats:
x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))
#
#convert from int to float:
x = float(1)
#convert from float to int:
y = int(2.8)
#convert from int to complex:
z = complex(1)

print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))
"""
1.0
2
(1+0j)
<class 'float'>
<class 'int'>
<class 'complex'>
"""
#
import random
print(random.randrange(1, 10))

#exercise
x = 5
x = float(x)

x = 5.5
x = int(x)

x = 5
x = complex(x)