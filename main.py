from enum import Enum
#import cow
#we can also import a module using the from syntax ie
from cow import mow
#from lib import person
#Or
from lib.person import scream
#then we simply call bark without using cow
from functools import reduce

scream()
mow()

#we can run a python program by calling python main.py

#data types
#float
#int
#convert data types
age = 20
age = float(age)
print(age)

#Arithmetic operators
# +,-,*,/,%,**,//
#//-signifies flow division ie rounds something
x = 5 // 2
print(x)  #returns 2 to us

#comparison operators
a = 20
b = 40
print(a == b)  #false
print(a != b)  #true
print(a > b)  #false
print(a <= b)  #true

#boolean operators
#not,and ,or

#or
#  returns the first operand that is not a falsey value
print(0 or 1)  #returns 1
print(False or "hey")  #returns hey
print("hi" or "hey")  #returns hi
print([] or False)  #returns False
print(False or [])  #returns []

#and
#evaluates the second argument when the first argument is True

#Bitwise operators
#& -performs a binary AND
#| -performs a binary OR
#^ -performs a binary XOR
#~ -performs a binary NOT
#<< -shift left operation
#>> -shift right operation

#is
#is an identity operator (compares two objects and returns true if both are the same object)

#in
#is a membership operator. its is used to tell if a value is contained in a list or other sequencesss

#Ternary operator
#Allows you to quickly define a conditional


#without a ternary operator
def is_adult(age):
  if age > 10:
    return True
  else:
    return False


print(is_adult(20))


#with the ternary operator
def is_adult2(age):
  return True if age > 10 else False


print(is_adult2(5))

#strings
#characters enclosed in quotation marks
#strings can be concatenated

#multi-line strings
print("""sophia is
  27
  years old
  """)

#string methods
print("sophia".upper())
print("sophia".lower())
print("alwoch sophia".title())

name = "soph"
print(len(name))

#add special characters to a string using "\"
# \n splits a string into a new line

#get a specific character in a string
print(name[3])

#use a negative number to access a string from the end
print(name[-1])

#use a range to access certain parts of a string
print(name[1:3])
print(name[:3])  #from the beginning to index 2

#Booleans (bool type)
#2 values True and False and they should be capitalised
#numbers are always true except 0
#strings are always true except when empty
#lists, tuples aand dictionaries are only false when empty

#any()
#returns true if any time in an iterable is True
book1 = True
book2 = False
my_books = [book1, book2]
print(any(my_books))

#all()
#returns true if all the members of an iterable are True
print(any(my_books))

#number data Types
#int
#float
#complex

#built in functions that work with numbers
print(abs(-5.5))  #returns 5.5
print(round(5.49, 1))  #returns 5.5


#enums
#enums are readable names that are bound to a constant value
#we import enums to use them
class State(Enum):
  INACTIVE = 0
  ACTIVE = 1


print(State.ACTIVE)
print(State.ACTIVE.value)
print(State(1))

#list all the possible values in an enum
print(list(State))
print(len(State))

#lists
dogs = ["reuben", "roger", "peter"]
#check if an item is in a list
print("reuben" in dogs)
#reference items in a list using indices
print(dogs[2])
#update a member in a list
dogs[1] = "Carlos"
print(dogs)

#extract a part of a list
print(dogs[2:3])
print(len(dogs))

#add items to a list
dogs.append('Judah')
dogs.extend(["Judah", 5])
dogs += ["Judah", 5]

#remove items from a list
dogs.remove("Carlos")
dogs.pop()

#insert multiple items inside a list at a specific index
dogs[1:1] = ["Test1", "Test2"]

#sorting a list

#Tuples
#Allow you to create immutable groups of objects ie once a tuple is created, it cannot be modified

people = ("savannah", "phidy")
print(people[0])
print(people.index("savannah"))
print(len(people))
print("soph" in people)
print(people[:1])

#Dictionaries
#Allow you to create key value pairs
dog = {"name": "Roger"}
print(dog["name"])
print(dog.get("name"))
print(dog.get("color", "brown"))
dog.pop("name")
print(dog.keys())
print(list(dog.values()))
print(dog.items())
dog["favourite food"] = "meat"
print(dog)
#del dog["color"]
dogCopy = dog.copy()
print(dogCopy)


#closures
#we use nonlocal to access variables of the outer function in a nested function
def counter():
  count = 0

  def increment():
    nonlocal count
    count = count + 1
    return count

  return increment


increment = counter()

print(increment())
print(increment())
print(increment())

#loops
#in python, there are two kinds of loops, while loops and for loops
count = 0
while count < 10:
  print("The count is less than 10")
  count += 1

print("After the loop")

#forloop
#we use a forloop to tell python to print something for a predetermined amount of time
item = [1, 2, 3, 4, 5, 6]
for item in item:
  print(item)

#we can also get the index of the items by wrapping the items in the enumerate function
calls = [5, 6, 7, 8]
for index, call in enumerate(calls):
  print(index, call)

#we can also use the range function
for item in range(10):
  print(item)

#Breaks and continue
#both while and for-loops can be interrupted using either break or continue
#continue stops the iteration and tells python to execute the next one
#break stops the iteration all together and goes on with the next instruction or ends the loop
computers = ["lenovo", "hp", "mac", "dell"]
for computer in computers:
  if computer == "mac":
    break
  if computer == "lenovo":
    continue
  print(computer)

#Classes
#we can write our own classes in python and in classes, instantiate objects
#an object is an instance of a class
#a class is the type of an object
#using self as an argument of a method in a class will point to the current object instance and must be specified when defining a method. everytime we create a method in a class we must start with self as an argument
#Theres a special method called __init__ which is a constructor we use to initialise variables in a class
#classes can inherit other classes


class Animal:

  def walk(self):
    print('walking....')


class Dog(Animal):

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def bark(self):
    print("woof!!")


#create an instance of a class
roger = Dog("roger", 12)
print(type(roger))

print(roger.age)
print(roger.name)

roger.bark()
roger.walk()

#modules
#Every python file is a module
#we can import a module from other modules
#in a typical python project, we have one entry point of other files and the rest are modules

#lambda functions
#Lambda functions, also called anonymous functions are tiny functions that have no name and only have one expression as their body
#They are defined using the lambda key word
lambda num: num * 2
lambda a, b: a * b

#lambda functions cannot be invoked directly but can be assigned to a variable eg
add = lambda a, b: a + b
print(add(56, 67))


#map(),filter() and reduce
#The map function is used to run a function upon each iteration, in an iterable item like a list and creates a new list with the same number of items but the values of each item can be changed
def myFunc(n):
  return len(n)


myList = ('apple', 'banana', 'cherry')
x = map(myFunc, myList)
print(list(x))

#double the numbers in a list using the map() function
#we can also put the lambda function straight into the map()
numbers = [1, 2, 3, 4, 5, 6]
double = lambda n: n * 2

result = map(double, numbers)
print(list(result))

#The filter method
#The filter method takes in an iterable and returns a filtered object which is also another iterable but without some of the original items
isEven = lambda n: n % 2 == 0

even_numbers = filter(isEven, numbers)
print(list(even_numbers))

#Reduce
#we have to import reduce from functools
expenses = [("dinner", 80), ("bills", 50)]

total_expenses = reduce(lambda a, b: a[1] + b[1], expenses)
print(total_expenses)


#Recursion
#A recursive function in python is one that calls itself
def factorial(n):
  if n == 1: return 1
  return n * factorial(n - 1)


print(factorial(3))

#Decorators
#decorators are used to alter how a function works. we use the @ followed by the decorator name

#use cases
#- logging
#- caching
#- verifying permissions
#- when we need to run the same code on mulltiple functions


def logtime(func):

  def wrapper():
    print("before")
    val = func()
    print("after")
    return val

  return wrapper


@logtime
def hello():
  print("Helllow.....!")


hello()

#DocStrings
#help us explain what our code is about. they basically supplement comments
"""This is a docString"""

#we can get info on functions we write with docStrings using the help() function


#Annotations
#Python is dynamically typed so we dont normally specify types, however, annotations do help us achieve something like that.
#the followiing function receives an int and returns an int
def increment(n: int) -> int:
  return n + 1


print(increment(7))

#Exception handling
#for exception handling in python, we wrap lines of code in a try block and then python will alert us on which error occured using an except block

try:
  result = 2 / 0
except ZeroDivisionError:
  print("cannot divide by zero")
#except <specify second error type in here>
#else: when there is no error
finally:
  result = 1

print(result)
