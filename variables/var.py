#example
x = 5
y = "John"
print(x)
print(y)

#Variables do not need to be declared with any particular type, and can even change type after they have been set
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#casting - If you want to specify the data type of a variable, this can be done with casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#You can get the data type of a variable with the type() function.
x = 5
y = "John"
print(type(x))
print(type(y))

x = "John"
# is the same as
x = 'John'

a = 4
A = "Sally"
#A will not overwrite a

#Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#multiple values
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z) #Make sure the number of variables matches the number of values, or else you will get an error.

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#output
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = 5
y = 10
print(x + y)

x = 5
y = "John"
print(x, y)

#global variables
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
#
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#global key
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#exercise Create a variable named carname and assign the value Volvo to it.
carname = "Volvo"

x = 50


x = 5
y = 10
print(x + y)

x = 5
y = 10
z = x + y
print(z)

x, y, z = "Orange", "Banana", "Cherry"

x = y = z = "Orange"

def myfunc():
 global x
 x = "fantastic"