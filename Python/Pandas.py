# Pandas is a Python library.
# Pandas is used to analyze data.
# Pandas is a Python library used for working with data sets.
# It has functions for analyzing, cleaning, exploring, and manipulating data.
# The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis"

# Why Use Pandas?
# Pandas allows us to analyze big data and make conclusions based on statistical theories.
# Pandas can clean messy data sets, and make them readable and relevant.
# Relevant data is very important in data science.

# What Can Pandas Do?
# Pandas gives you answers about the data. Like:
#   *Is there a correlation between two or more columns?
#   *What is average value?
#   *Max value?
#   *Min value?
#   *Pandas are also able to delete rows that are not relevant, or contains wrong values, like empty or NULL values. This is called cleaning the data.

# import pandas
# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }
# myvar = pandas.DataFrame(mydataset)
# print(myvar)

# Load a CSV file into a Pandas DataFrame:
# import pandas as pd
# df = pd.read_csv('data.csv')
# print(df.to_string()) 


import pandas as pd
mydataset = {
  'cars':     ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
myvar = pd.DataFrame(mydataset)
print(myvar)

print("\n")
#****************************************************

# Pandas Series
# What is a Series?
# A Pandas Series is like a column in a table.
# It is a one-dimensional array holding data of any type.

# Create a simple Pandas Series from a list:
import pandas as pd
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)
print(myvar[0]) #Return the first value of the Series:

print("\n")


# Create your own labels:
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)
print(myvar["y"]) #Return the value of "y": eg 7


# Create a simple Pandas Series from a dictionary:
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)

print("\n")


# Create a Series using only data from "day1" and "day2":
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day2","day3"])

print(myvar)
print("\n")


# Create a DataFrame from two Series:   
import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
myvar = pd.DataFrame(data)

print(myvar)

print("\n")
print("\n")


#***************************************************

# Pandas DataFrames****************
# What is a DataFrame?
# A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.
# whenever data in 2d is called dataframe


# Create a simple Pandas DataFrame:
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
#load data into a DataFrame object:
df = pd.DataFrame(data)
print(df) 
#refer to the row index:
print(df.loc[0])   # Return row 0:
#use a list of indexes:
print(df.loc[[0, 1]])  #Return row 0 and 1:




# Add a list of names to give each row a name:
import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df) 
#refer to the named index:
print(df.loc["day2"]) #Return "day2":


# Load the CSV into a DataFrame:
import pandas as pd

print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
#*********************************************************
#Pandas Read CSV(comma separated file )************************
# Read CSV Files
# A simple way to store big data sets is to use CSV files (comma separated files).
# CSV files contains plain text and is a well know format that can be read by everyone including Pandas.
# In our examples we will be using a CSV file called 'data.csv'.
# Download data.csv. or Open data.csv


import pandas as pd
df = pd.read_csv('data.csv')  #Load a (CSV file) into a DataFrame:
print(df) 
print(pd.options.display.max_rows) #Check the number of maximum returned rows:

# Get a quick overview by printing the first 10 rows of the DataFrame:
df = pd.read_csv('data.csv')
print(df.head(10))

# Print the first 5 rows of the DataFrame:
df = pd.read_csv('data.csv')
print(df.head())

# Print the last 5 rows of the DataFrame:
print(df.tail()) 

# Print information about the data:
print(df.info()) 


# Pandas - Cleaning Data*******************************************
# Data cleaning means fixing bad data in your data set.
# Bad data could be:
# Empty cells
# Data in wrong format
# Wrong data
# Duplicates

# Return a new Data Frame with no empty cells:
import pandas as pd

df = pd.read_csv('data.csv')

new_df = df.dropna()

print(new_df.to_string())


# Remove all rows with NULL values:
import pandas as pd

df = pd.read_csv('data.csv')

df.dropna(inplace = True)

print(df.to_string())



# Replace NULL values with the number 130:
import pandas as pd

df = pd.read_csv('data.csv')

df.fillna(130, inplace = True)


# Replace NULL values in the "Calories" columns with the number 130:
import pandas as pd

df = pd.read_csv('data.csv')

df.fillna({"Calories": 130}, inplace=True)



# Calculate the MEAN, and replace any empty values with it:
import pandas as pd

df = pd.read_csv('data.csv')

x = df["Calories"].mean()

df.fillna({"Calories": x}, inplace=True)


# Calculate the MEDIAN, and replace any empty values with it:
import pandas as pd

df = pd.read_csv('data.csv')

x = df["Calories"].median()

df.fillna({"Calories": x}, inplace=True)


# Calculate the MODE, and replace any empty values with it:
import pandas as pd

df = pd.read_csv('data.csv')

x = df["Calories"].mode()[0]

df.fillna({"Calories": x}, inplace=True)


#Pandas - Cleaning Data of Wrong Format************************************

# Data of Wrong Format
# Cells with data of wrong format can make it difficult, or even impossible, to analyze data.
# To fix it, you have two options: remove the rows, or convert all cells in the columns into the same format.

# Convert to date:
# import pandas as pd

# df = pd.read_csv('data.csv')

# df['Date'] = pd.to_datetime(df['Date'], format='mixed')

# print(df.to_string())


#Pandas - Fixing Wrong Data**********************************

# Wrong Data
# "Wrong data" does not have to be "empty cells" or "wrong format", it can just be wrong, like if someone registered "199" instead of "1.99".
# Sometimes you can spot wrong data by looking at the data set, because you have an expectation of what it should be.

# Loop through all values in the "Duration" column.
# If the value is higher than 120, set it to 120:

for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120

# Delete rows where "Duration" is higher than 120:
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)

# Returns True for every row that is a duplicate, otherwise False:
print(df.duplicated())

# Remove all duplicates:
df.drop_duplicates(inplace = True)



#*************Pandas - Plotting****************
# Plotting
# Pandas uses the plot() method to create diagrams.
# We can use Pyplot, a submodule of the Matplotlib library to visualize the diagram on the screen.


# # Import pyplot from Matplotlib and visualize our DataFrame:
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot()

plt.show()


# # Scatter Plot
# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv('data.csv')

# df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')

# plt.show()



# # A scatterplot where there are no relationship between the columns:
# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv('data.csv')

# df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')

# plt.show()

# # Histogram
# df["Duration"].plot(kind = 'hist')



#f





























