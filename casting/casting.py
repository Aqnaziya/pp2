#examples
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

a = "Hello"
print(a)

#You can use three double quotes:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#Or three single quotes:
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

a = "Hello, World!"
print(a[1]) #e

#we can loop through the characters in a string, with a FOR loop.
for x in "banana":
  print(x)
  
#The len() function returns the length of a string:
a = "Hello, World!"
print(len(a)) #13

#To check if a certain phrase is present in a string, we can use the keyword IN.
txt = "The best things in life are free!"
print("free" in txt) #True

#Use it in an IF statement:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.") #Yes, 'free' is present.
  
#To check if a certain phrase is NOT in a string, we can use the keyword NOT IN.
txt = "The best things in life are free!"
print("expensive" not in txt) #True

#print only if "expensive" is NOT present - Use it in an IF statement:
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.") #No, 'expensive' is NOT present.

#Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5]) #llo

#Get the characters from the start to position 5 (not included):
b = "Hello, World!"
print(b[:5]) #Hello

#Get the characters from position 2, and all the way to the end:
b = "Hello, World!"
print(b[2:]) #llo, World!

"""
Get the characters:
From: "o" in "World!" (position -5)
To, but not included: "d" in "World!" (position -2):
"""
b = "Hello, World!"
print(b[-5:-2]) #orl

#The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper()) #HELLO, WORLD!

#The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower()) #hello, world!

#The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"  Удаляет по краям

#The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J")) #Jello, World!

#The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!'] 

#To concatenate, or combine, two strings you can use the + operator.
a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

age = 36
txt = "My name is John, I am " + age
print(txt) #My name is John, I am 36

#FORMAT
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age)) #My name is John, and I am 36

#The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price)) #I want 3 pieces of item 567 for 49.95 dollars.

#You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price)) #I want to pay 49.95 dollars for 3 pieces of item 567

#The escape character allows you to use double quotes when you normally would not be allowed:
txt = "We are the so-called \"Vikings\" from the north." #We are the so-called "Vikings" from the north.

#exercise
x = "Hello World"
print(len(x)) 

txt = "Hello World"
x = txt[0] #H

txt = "Hello World"
x = txt[2:5] #llo

txt = " Hello World "
x = txt.strip() #Hello, world!

txt = "Hello World"
txt = txt.upper()

txt = "Hello World"
txt = txt.lower()

txt = "Hello World"
txt = txt.replace("H", "J")

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))








  
  
