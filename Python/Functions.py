#A function is a block of code which only runs when it is called.
#You can pass data, known as parameters, into a function.
#A function can return data as a result

#Creating a Function :- In Python a function is defined using the def keyword:
def my_function():
  print("Hello from a function")


#To call a function, use the function name followed by parenthesis:
def my_function():
  print("Hello from a function")

my_function()



#Arguments
#Information can be passed into functions as arguments.
#Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
#The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")



#This function expects 2 arguments, and gets 2 arguments:
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")



#This function expects 2 arguments, but gets only 1:
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil")



#If the number of arguments is unknown, add a * before the parameter name:
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")



#You can also send arguments with the key = value syntax.
#This way the order of the arguments does not matter.
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")



#If the number of keyword arguments is unknown, add a double ** before the parameter name:
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")



#The following example shows how to use a default parameter value.
#If we call the function without argument, it uses the default value:
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


#To let a function return a value, use the return statement:
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))



#Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:
def my_function(x):
  print(x)

my_function(x = 3)



#To specify that a function can have only keyword arguments, add *, before the arguments:
def my_function(*, x):
  print(x)

my_function(x = 3)



#Without the *, you are allowed to use positional arguments even if the function expects keyword arguments:
def my_function(x):
  print(x)

my_function(3)



#But with the *, you will get an error if you try to send a positional argument:
def my_function(*, x):
  print(x)

my_function(3)


#********************Python Lambda*************************8
#A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression.
#The expression is executed and the result is returned:

#Add 10 to argument a, and return the result:

x = lambda a : a + 10
print(x(5))


#Multiply argument a with argument b and return the result:
x = lambda a, b : a * b
print(x(5, 6))


#Summarize argument a, b, and c and return the result:
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))



#***********************************************
"""""
Python OOP

What is OOP?
OOP stands for Object-Oriented Programming.
Python is an object-oriented language, allowing you to structure your code using classes and objects for better organization and reusability.


What are Classes and Objects?
Classes and objects are the two core concepts in object-oriented programming.

A class defines what an object should look like, and an object is created based on that class. For example:

Class	   Objects
Fruit	-  Apple, Banana, Mango
Car	    -  Volvo, Audi, Toyota

"""""

