Replacing strings with numbers in Python for Data Analysis



Sometimes we need to convert string values in a pandas dataframe to a unique
integer so that the algorithms can perform better. So we assign unique numeric
value to a string value in Pandas DataFrame.

 **Note: Before executing create an example.csv file containing some names and
gender**

Say we have a table containing names and gender column. In gender column,
there are two categories male and female and suppose we want to assign 1 to
male and 2 to female.

Examples:

    
    
    Input : 
    ---------------------
        |  Name  |  Gender
    ---------------------
     0    Ram        Male
     1    Seeta      Female
     2    Kartik     Male
     3    Niti       Female
     4    Naitik     Male 
    
    Output :
        |  Name  |  Gender
    ---------------------
     0    Ram        1
     1    Seeta      2
     2    Kartik     1
     3    Niti       2
     4    Naitik     1 
    

  

  

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Method 1:**

    
    
    To create a dictionary containing two 
    elements with following key-value pair:
    Key       Value
    male      1
    female    2
    

Then iterate using for loop through Gender column of DataFrame and replace the
values wherever the keys are found.

 __

 __  
 __

 __

 __  
 __  
 __

# import pandas library

import pandas as pd

 

# creating file handler for 

# our example.csv file in

# read mode

file_handler = open("example.csv", "r")

 

# creating a Pandas DataFrame

# using read_csv function 

# that reads from a csv file.

data = pd.read_csv(file_handler, sep = ",")

 

# closing the file handler

file_handler.close()

 

# creating a dict file 

gender = {'male': 1,'female': 2}

 

# traversing through dataframe

# Gender column and writing

# values where key matches

data.Gender = [gender[item] for item in data.Gender]

print(data)  
  
---  
  
 __

 __

Output :

    
    
        |  Name  |  Gender
    ---------------------
     0    Ram        1
     1    Seeta      2
     2    Kartik     1
     3    Niti       2
     4    Naitik     1 
    

**Method 2:**  
Method 2 is also similar but requires no dictionary file and takes fewer lines
of code. In this, we internally iterate through Gender column of DataFrame and
change the values if the condition matches.

 __

 __  
 __

 __

 __  
 __  
 __

# import pandas library

import pandas as pd

 

# creating file handler for

# our example.csv file in

# read mode

file_handler = open("example.csv", "r")

 

# creating a Pandas DataFrame

# using read_csv function that

# reads from a csv file.

data = pd.read_csv(file_handler, sep = ",")

 

# closing the file handler

file_handler.close()

 

# traversing through Gender 

# column of dataFrame and 

# writing values where

# condition matches.

data.Gender[data.Gender == 'male'] = 1

data.Gender[data.Gender == 'female'] = 2

print(data)  
  
---  
  
 __

 __

Output :

    
    
        |  Name  |  Gender
    ---------------------
     0    Ram        1
     1    Seeta      2
     2    Kartik     1
     3    Niti       2
     4    Naitik     1 
    

****Applications****

  1. This technique can be applied in Data Science. Suppose if we are working on a dataset that contains gender as ‘male’ and ‘female’ then we can assign numbers like ‘0’ and ‘1’ respectively so that our algorithms can work on the data.
  2. This technique can also be applied to replace some particular values in a datasets with new values.

 ** **References****

  * https://pandas.pydata.org
  * https://pandas.pydata.org/pandas-docs/stable/tutorials.html

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

