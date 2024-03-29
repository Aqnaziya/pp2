#exercises
#(exercises of lab1 are after the examples)
print(10 > 9) # True

print(10 == 9) # False

print(10 < 9) # False

print(bool("abc")) # True

print(bool(0)) # False

#examples
print(10 > 9)  #True
print(10 == 9) #False
print(10 < 9)  #False

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  
#Evaluate a string and a number:
print(bool("Hello")) #True
print(bool(15))      #True

#Evaluate two variables:
x = "Hello"
y = 15
print(bool(x)) #True
print(bool(y)) #True

"""
Almost any value is evaluated to True if it has some sort of content.
Any string is True, except empty strings.
Any number is True, except 0.
Any list, tuple, set, and dictionary are True, except empty ones.
"""

bool("abc") #True
bool(123)   #True
bool(["apple", "cherry", "banana"]) #True

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({})) #all of them are false

#an object that is made from a class with a __len__ function that returns 0 or False
class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj)) #False

def myFunction() :
  return True
print(myFunction()) #True

#Print "YES!" if the function returns True, otherwise print "NO!":
def myFunction() :
  return True
if myFunction():
  print("YES!")
else:
  print("NO!") #True
  
#isinstance() to determine if an object is of a certain data type:
x = 200
print(isinstance(x, int)) #True


