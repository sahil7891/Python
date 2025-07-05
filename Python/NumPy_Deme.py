# NumPy is a Python library used for working with arrays.
# NumPy is used for working with arrays.
# It also has functions for working in domain of linear algebra, fourier transform, and matrices.
# NumPy is short for "Numerical Python".

# Why Use NumPy?
# In Python we have lists that serve the purpose of arrays, but they are slow to process.
# NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.
# The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.
# Arrays are very frequently used in data science, where speed and resources are very important.

# Why is NumPy Faster Than Lists?
# NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.
# This behavior is called locality of reference in computer science.
# This is the main reason why NumPy is faster than lists. Also it is optimized to work with latest CPU architectures.


# Create a NumPy array:
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))


# Use a tuple to create a NumPy array:
import numpy as np
arr = np.array((1, 2, 3, 4, 5))
print(arr)

# Create a 2-D array containing two arrays with the values 1,2,3 and 4,5,6:
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)


# Create a 3-D array with two 2-D arrays, both containing two arrays with the values 1,2,3 and 4,5,6:
import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)


# Check how many dimensions the arrays have:
import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# NumPy Array Indexing************************
# Access Array Elements


# Get the first element from the following array:
import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[0])


# Get the second element from the following array.
import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[1])

# Get third and fourth elements from the following array and add them.
import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[2] + arr[3])


# Access the element on the first row, second column:
import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[0, 1])


# Access the element on the 2nd row, 5th column:
import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('5th element on 2nd row: ', arr[1, 4])


# Access the third element of the second array of the first array:
import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])


# Negative Indexing
# Print the last element from the 2nd dim:
import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr[1, -1])


# NumPy Array Slicing*******************************

# Slice elements from index 1 to index 5 from the following array:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])


# Slice elements from index 4 to the end of the array:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[4:])


# Slice elements from the beginning to index 4 (not included):
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[:4])


# Slice from the index 3 from the end to index 1 from the end:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[-3:-1])


# Return every other element from index 1 to index 5:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2])


# Return every other element from the entire array:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[::2])


# From the second element, slice elements from index 1 to index 4 (not included):
import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4])


# From both elements, return index 2:
import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 2])


# From both elements, slice index 1 to index 4 (not included), this will return a 2-D array:
import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 1:4])


# NumPy Data Types************************************

# Get the data type of an array object:
import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr.dtype)


# Get the data type of an array object:
import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr.dtype)



# Get the data type of an array containing strings:
import numpy as np

arr = np.array(['apple', 'banana', 'cherry'])

print(arr.dtype)


# Create an array with data type string:
import numpy as np

arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print(arr.dtype)

# Create an array with data type 4 bytes integer:
import numpy as np

arr = np.array([1, 2, 3, 4], dtype='i4')

print(arr)
print(arr.dtype)


# Change data type from float to integer by using 'i' as parameter value:
import numpy as np

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)



# Change data type from integer to boolean:
import numpy as np

arr = np.array([1, 0, 3])

newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)


# NumPy Array Copy vs View**************************

# Make a copy, change the original array, and display both arrays:
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)


# Make a view, change the original array, and display both arrays:
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)


# NumPy Array Shape*******************************
# Get the Shape of an Array

# Print the shape of a 2-D array:
import numpy as np
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)


# Create an array with 5 dimensions using ndmin using a vector with values 1,2,3,4 and verify that last dimension has value 4:
import numpy as np
arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('shape of array :', arr.shape)


# NumPy Array Reshaping**********************
# Reshape From 1-D to 2-D

# Convert the following 1-D array with 12 elements into a 2-D array.
# The outermost dimension will have 4 arrays, each with 3 elements:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(newarr)


# Convert the following 1-D array with 12 elements into a 3-D array.
# The outermost dimension will have 2 arrays that contains 3 arrays, each with 2 elements:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)

print(newarr)


# ry converting 1D array with 8 elements to a 2D array with 3 elements in each dimension (will raise an error):
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(3, 3)

print(newarr)


# NumPy Array Iterating****************************

# Iterate on the elements of the following 1-D array:
import numpy as np

arr = np.array([1, 2, 3])

for x in arr:
  print(x)


# Iterate on the elements of the following 2-D array:
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  print(x)

# Iterate on each scalar element of the 2-D array:
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  for y in x:
    print(y)

# Iterate through the following 3-D array:
import numpy as np

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)


# Iterate through the array as a string:
import numpy as np

arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)


# Enumerate on following 1D arrays elements:
import numpy as np

arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
  print(idx, x)


# Enumerate on following 2D array's elements:
import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr):
  print(idx, x)


# NumPy Joining Array
# Joining NumPy Arrays

# Join two arrays
import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)

# Join two 2-D arrays along rows (axis=1):
import numpy as np

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)


# NumPy provides a helper function: hstack() to stack along rows.
import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.hstack((arr1, arr2))

print(arr)

# Stacking Along Columns
# NumPy provides a helper function: vstack()  to stack along columns.
import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.vstack((arr1, arr2))

print(arr)


# Stacking Along Height (depth)
# NumPy provides a helper function: dstack() to stack along height, which is the same as depth.
import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.dstack((arr1, arr2))

print(arr)


# NumPy Splitting Array*************************

# Split the array in 3 parts:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)


# Split the array in 4 parts:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 4)

print(newarr)


# Access the splitted arrays:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr[0])
print(newarr[1])
print(newarr[2])


# Split the 2-D array into three 2-D arrays.
import numpy as np

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 3)

print(newarr)


# Split the 2-D array into three 2-D arrays.
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3)

print(newarr)


# Split the 2-D array into three 2-D arrays along columns.
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3, axis=1)

print(newarr)


# NumPy Searching Arrays************************

# Find the indexes where the value is 4:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x)

# Find the indexes where the values are even:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 0)

print(x)

# Find the indexes where the values are odd:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 1)

print(x)


# Find the indexes where the value 7 should be inserted:
import numpy as np

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)

print(x)

# Find the indexes where the value 7 should be inserted, starting from the right:
import numpy as np

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7, side='right')

print(x)


# Find the indexes where the values 2, 4, and 6 should be inserted:
import numpy as np

arr = np.array([1, 3, 5, 7])

x = np.searchsorted(arr, [2, 4, 6])

print(x)

# NumPy Sorting Arrays*************************

# Sort the array:
import numpy as np

arr = np.array([3, 2, 0, 1])

print(np.sort(arr))


# Sort the array alphabetically:
import numpy as np

arr = np.array(['banana', 'cherry', 'apple'])

print(np.sort(arr))

# Sort a boolean array:
import numpy as np

arr = np.array([True, False, True])

print(np.sort(arr))


# Sort a 2-D array:
import numpy as np

arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr))

# NumPy Filter Array***************************************

# Create an array from the elements on index 0 and 2:
import numpy as np

arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr[x]

print(newarr)

#------------------------------------------------------------------
# Create a filter array that will return only values higher than 42:
import numpy as np

arr = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)
#------------------------------------------------------------

# Create a filter array that will return only values higher than 42:
import numpy as np

arr = np.array([41, 42, 43, 44])

filter_arr = arr > 42

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)


# Create a filter array that will return only even elements from the original array:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

filter_arr = arr % 2 == 0

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

# Random Numbers in NumPy********************

# Generate a random integer from 0 to 100:
from numpy import random

x = random.randint(100)

print(x)


# Generate a 1-D array containing 5 random integers from 0 to 100:
from numpy import random

x=random.randint(100, size=(5))

print(x)

# Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:
from numpy import random

x = random.randint(100, size=(3, 5))

print(x)


# The rand() method also allows you to specify the shape of the array.
# Generate a 1-D array containing 5 random floats:
from numpy import random

x = random.rand(5)

print(x)

# Generate a 2-D array with 3 rows, each row containing 5 random numbers:
from numpy import random

x = random.rand(3, 5)

print(x)

# Return one of the values in an array:
from numpy import random

x = random.choice([3, 5, 7, 9])

print(x)


# Generate a 2-D array tha consists of the values in the array parameter (3, 5, 7, and 9):
from numpy import random

x = random.choice([3, 5, 7, 9], size=(3, 5))

print(x)
#k