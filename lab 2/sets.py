#exercises
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")
  
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")


#examples
#curly brackets
thisset = {"apple", "banana", "cherry"}
print(thisset) 

#only unique values
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset) #{'banana', 'cherry', 'apple'}

#true n 1, false n 0 are the same
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset) #{True, 2, 'banana', 'cherry', 'apple'}

thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset) #{False, True, 'cherry', 'apple', 'banana'}

#String, int and boolean data types:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

myset = {"apple", "banana", "cherry"}
print(type(myset)) #<class 'set'>

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset) #{'banana', 'cherry', 'apple'} / # Note: the set list is unordered, so the result will display the items in a random order.

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
"""
apple
banana
cherry
"""
#if banana in thisset
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset) #True

#Add an item to a set, using the add() method:
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset) #{'cherry', 'banana', 'apple', 'orange'}

#add items from another set into the current set
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset) #{'apple', 'mango', 'cherry', 'pineapple', 'banana', 'papaya'}

#any iterable obj(set, list, tuple, etc)
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset) #{'banana', 'cherry', 'apple', 'orange', 'kiwi'}

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)




