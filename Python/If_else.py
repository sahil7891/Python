a=1
b=2
if a==b:
  print("yes both are same")
elif a>b:
  print("a is greater than b")
else:
  print("a is less than b")

   #--------------------
   
#If statement:
a = 33
b = 200
if b > a:
  print("b is greater than a")


#If statement, without indentation (will raise an error):
# a = 33
# b = 200
# if b > a:
#print("b is greater than a") # you will get an error


#The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
a = 77
b = 77
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


#The else keyword catches anything which isn't caught by the preceding conditions.
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


#-----------

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")



#One line if else statement:
a = 2
b = 330
print("A") if a > b else print("B")



#One line if else statement, with 3 conditions:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")



#Test if a is greater than b, AND if c is greater than a:
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")


#Nested If: - You can have if statements inside if statements, this is called nested if statements.
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")



#if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
a = 33
b = 200

if b > a:
  pass

 #--------------------

a=input('write any number')
a=int(a)
b=input("write 2nd number")
b=int(b)
if a==b:
  print("yes both are same")
elif a>b:
  print("A is greater than B")
else:
 print("A is less than B")

#Python Match Statement**************

#Instead of writing many if..else statements, you can use the match statement.
#The match statement selects one of many code blocks to be executed.
day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")