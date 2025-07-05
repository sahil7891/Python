print("Hello")
print('Hello')


a = "Hello"
print(a)


c = "Hello, World!"
print(c[1])   #index no. 1 pe jo letter hoga wo print hoga eg -e 


b = """Hey friends here im teaching
python, and if you guys are interested 
in programming then join mu course"""
print(b)


for x in "banana":
  print(x)


a = "Hello, World!"
print(len(a))         #The len() function returns the length of a string:


txt = "The best things in life are free!"
print("free" in txt)  #Check if "free" is present in the following text:



txt = "The best things in life are free!"
if "free" in txt:    #Print only if "free" is present:
  print("Yes, 'free' is present.")


txt = "The best things in life are free!"
print("expensive" not in txt)   #Check if "expensive" is NOT present in the following text:


txt = "The best things in life are free!"
if "expensive" not in txt:   #print only if "expensive" is NOT present:
  print("No, 'expensive' is NOT present.")


#Python - Slicing Strings

b = "Hello, World!"
print(b[2:5])     #Get the characters from index 2 to index 5 (not included):




#Get the characters from the start to index no 5 (not included):
b = "Hello, World!"
print(b[:5])


#Get the characters from position 2, and all the way to the end:
b = "Hello, World!"
print(b[2:])


b = "Hello, World!"
print(b[-5:-2])  # - ke case me piche se index count ho eg- orld print hoga


#Python - Modify Strings

a = "Hello, World!"
print(a.upper())   #The upper() method returns the string in upper(capital) case:
print(a.lower())   #The lower() method returns the string in lower case:


#The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"


#The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("Hello", "lelo"))


#The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']


#String Concatenation

#Merge variable a with variable b into variable c:
a = "Hello"
b = "World"
c = a + b
print(c)


#To add a space between them, add a " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c)


name="hello world"                   # name me "hello world" string a jaega
print(name.find("ello") )           # to find the index no eg e ka index no 1 aega



#String Format

#age = 36
#txt = "My name is John, I am " + age
#print(txt)


age = 36
txt = f"My name is John, I am {age}"
print(txt)


#Add a placeholder for the price variable:
price = 59
txt = f"The price is {price} dollars"
print(txt)


#Display the price with 2 decimals:
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)


#Perform a math operation in the placeholder, and return the result:
txt = f"The price is {20 * 59} dollars"
print(txt)





































