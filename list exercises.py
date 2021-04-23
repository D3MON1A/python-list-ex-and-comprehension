# 1. What is the output of the following code

my_list = ["Hello", "Python"]
# The join() method takes all items in an iterable and joins them into one string.
# A string must be specified as the separator.
print("-".join(my_list))

# 2.  What is the output of the following list operation
sampleList = [10, 20, 30, 40, 50]
print(sampleList[-2])
print(sampleList[-4:-1])

# 3.What is the output of the following code?
sampleList = [10, 20, 30, 40]
del sampleList[0:6]
print(sampleList)

# 4. What is the output of the following list comprehension
resList = [x+y for x in ['Hello ', 'Good '] for y in ['Dear', 'Bye']]
print(resList)
# List comprehension offers a shorter syntax when you want to create a 
# new list based on the values of an existing list.
# Example:

# Based on a list of fruits, you want a new list, 
# containing only the fruits with the letter "a" in the name.
# Without list comprehension you will have to write a for 
# statement with a conditional test inside:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
# With list comprehension you can do all that with only one line of code:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

# The Syntax
# newlist = [expression for item in iterable if condition == True]
# The return value is a new list, leaving the old list unchanged.
# Example
# Only accept items that are not "apple":

newlist = [x for x in fruits if x != "apple"]
print(newlist)
# The condition if x != "apple"  will return True for all elements 
# other than "apple", making the new list contain all fruits except "apple".
# Iterable
# The iterable can be any iterable object, like a list, tuple, set etc.
# Example
# You can use the range() function to create an iterable:

newlist = [x for x in range(10)]
print(newlist)
# Same example, but with a condition:
# Accept only numbers lower than 5:

newlist = [x for x in range(10) if x < 5]
print(newlist)

# Expression
# The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:

# Example
# Set the values in the new list to upper case:
newlist = [x.upper() for x in fruits]
print(newlist)
# You can set the outcome to whatever you like:
# Example
# Set all values in the new list to 'hello':

newlist = ['hello' for x in fruits]
print(newlist)
# The expression can also contain conditions, not like 
# a filter, but as a way to manipulate the outcome:
# Example
# Return "orange" instead of "banana":

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
