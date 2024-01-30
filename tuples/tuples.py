#exe
fruits = ("apple", "banana", "cherry")
print(fruits[0])

fruits = ("apple", "banana", "cherry")
print(len(fruits))

fruits = ("apple", "banana", "cherry")
print(fruits[-1])

fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

#examples
#roung brackets
thistuple = ("apple", "banana", "cherry")
print(thistuple) #('apple', 'banana', 'cherry')

thistuple = ("apple", "banana", "cherry")
print(len(thistuple)) #3

#TUPLE
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#any data type
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1) #('abc', 34, True, 40, 'male')

#Using the tuple() method to make a tuple:
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple) #('apple', 'banana', 'cherry')

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1]) #cherry

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5]) #('cherry', 'orange', 'kiwi')

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4]) #('apple', 'banana', 'cherry', 'orange')

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1]) #('orange', 'kiwi', 'melon')

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple") #Yes, 'apple' is in the fruits tuple
  
#Convert the tuple into a list to be able to change it
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x) #("apple", "kiwi", "cherry")

#tuples are immutable, Convert the tuple into a list, add "orange", and convert it back into a tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple) #('apple', 'banana', 'cherry', 'orange')

#alternative
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple) #('apple', 'banana', 'cherry', 'orange')

thistuple = ("apple","banana","cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple) #('banana', 'cherry')

#The del keyword can delete the tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

#packing
fruits = ("apple", "banana", "cherry")
print(fruits) #('apple', 'banana', 'cherry')

#unpacking / extract the values back into variables
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red) 
"""
apple
banana
cherry
"""
#if values n variables don'r match
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red) 
"""
apple
banana
['cherry', 'strawberry', 'raspberry']
"""
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red) 
"""
apple
['mango', 'papaya', 'pineapple']
cherry
"""
#FOR loop
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x) 
"""
apple
banana
cherry
"""
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i]) 
"""
apple
banana
cherry
"""
#WHILE loop to go through all the index numbers:
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1 
  
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple) #('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')

