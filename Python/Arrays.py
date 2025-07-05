#Python does not have built-in support for Arrays, but Python Lists can be used instead.
#This page shows you how to use LISTS as ARRAYS, however, to work with arrays in Python you will have to import a library, like the NumPy library.
#Arrays are used to store multiple values in one single variable:


#Create an array containing car names:
cars = ["Ford", "Volvo", "BMW"]


#Get the value of the first array item:
x = cars[0]


#Modify the value of the first array item:
cars[0] = "Toyota"


#Return the number of elements in the cars array:
x = len(cars)


#Print each item in the cars array:
for x in cars:
  print(x)


#Add one more element to the cars array:
cars.append("Honda")


#Delete the second element of the cars array:
cars.pop(1)


#Delete the element that has the value "Volvo":
cars.remove("Volvo")




