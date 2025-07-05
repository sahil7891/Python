#Variables are containers for storing data values.
#Creating Variables
#Python has no command for declaring a variable.
#A variable is created the moment you first assign a value to it.

x = 4         # x is of type int
x = "Sallary" # x is now of type str
print(x)


x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x,y,z)


x = 5
y = "John"
print(type(x))  #int
print(type(y))  #string


x = "John"
# is the same as // dono hi string h
x = 'John'


a = 4
A = "Sally"
#A will not overwrite a
print(a,A)


# Asign multiple values
x, y, z = "Orange", "Banana", "Cherry" #Python allows you to assign values to multiple variables in one line:
print(x)
print(y)
print(z)


x = y = z = "Orange"  #you can assign the same value to multiple variables in one line:
print(x)
print(y)
print(z)


fruits = ["apple", "banana", "cherry"]  #If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
x, y, z = fruits
print(x)
print(y)
print(z)


x = "Python is awesome"  #The Python print() function is often used to output variables.
print(x)


x = "Python"
y = "is"
z = "awesome"
print(x, y, z)  #In the print() function, you output multiple variables, separated by a comma:
print(x + y + z) #You can also use the + operator to output multiple variables:


name='Hello'
NAME='Bro'
print(name,NAME)


x = 5
y = 10
print(x + y) #For numbers, the + character works as a mathematical operator:


x = 5
y = "John"
#print(x + y) #In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
print(x, y)  #The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:

#Global Variables
x = "awesome"  #Create a variable outside of a function, and use it inside the function
def myfunc():
  print("Python is " + x)
myfunc()



x = "awesome" #Create a variable inside a function, with the same name as the global variable
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)



def myfunc(): #If you use the global keyword, the variable belongs to the global scope:
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)



x = "awesome" #To change the value of a global variable inside a function, refer to the variable by using the global keyword:
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)

#------------------------------

A=1
print(A)           
print("hellow",A)
B=3
print(A+B)  #4

print(157+9)

print("two one are ",1*2)


#Data types
""""
Text Type:	       str
Numeric Types:	   int, float, complex
Sequence Types:	   list, tuple, range
Mapping Type:	   dict
Set Types:	       set, frozenset
Boolean Type:	   bool
Binary Types:	   bytes, bytearray, memoryview
None Type:   	   NoneType
"""
