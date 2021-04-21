Data analysis using Pandas



 ** _Pandas_** is the most popular python library that is used for data
analysis. It provides highly optimized performance with back-end source code
is purely written in **_C_** or **_Python_**.

    
    
    We can analyze data in pandas with:
    
    
    
      1. **Series**
      2.  **DataFrames**
    
    

### Series:

 ** _Series_** is one dimensional(1-D) array defined in pandas that can be
used to store any data type.

 **Code #1: _Creating Series_**

 __

 __  
 __

 __

 __  
 __  
 __

# Program to create series

 

# Import Panda Library

import pandas as pd 

 

# Create series with Data, and Index

a = pd.Series(Data, index = Index)   
  
---  
  
__

__

Here, ** _Data_** can be:

  1. A **_Scalar value_** which can be integerValue, string
  2. A **_Python Dictionary_** which can be Key, Value pair
  3. A **_Ndarray_**

 **Note** : Index by default is from 0, 1, 2, …(n-1) where n is length of
data.  
  
**Code #2: _When Data contains scalar values_**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Program to Create series with scalar values

 

# Numeric data

Data =[1, 3, 4, 5, 6, 2, 9] 

 

# Creating series with default index values

s = pd.Series(Data) 

 

# predefined index values

Index =['a', 'b', 'c', 'd', 'e', 'f', 'g'] 

 

# Creating series with predefined index values

si = pd.Series(Data, Index)   
  
---  
  
__

__

**Output** :

    
    
    
    
    ![](https://media.geeksforgeeks.org/wp-content/uploads/panda1.png)
    
    Scalar Data with default Index
    
    
    
    
    ![](https://media.geeksforgeeks.org/wp-content/uploads/panda2.png)
    
    Scalar Data with Index
    
    
    

  
**Code #3: _When Data contains Dictionary_**

 __

 __  
 __

 __

 __  
 __  
 __

# Program to Create Dictionary series

dictionary ={'a':1, 'b':2, 'c':3, 'd':4,
'e':5} 

 

# Creating series of Dictionary type

sd = pd.Series(dictionary)   
  
---  
  
__

__

**Output** :

    
    
    
    
    ![](https://media.geeksforgeeks.org/wp-content/uploads/panda3.png)
    
    Dictionary type data
    
    
    

**Code #4: _When Data contains Ndarray_**

 __

 __  
 __

 __

 __  
 __  
 __

# Program to Create ndarray series

 

# Defining 2darray

Data =[[2, 3, 4], [5, 6, 7]] 

 

# Creating series of 2darray

snd = pd.Series(Data)   
  
---  
  
__

__

**Output** :

    
    
    
    
    ![](https://media.geeksforgeeks.org/wp-content/uploads/panda4.png)
    
    Data as Ndarray
    
    
    

### DataFrames:

 **DataFrames** is two-dimensional(2-D) data structure defined in pandas which
consists of rows and columns.

  

  

 **Code #1: _Creation of DataFrame_**

 __

 __  
 __

 __

 __  
 __  
 __

# Program to Create DataFrame

 

# Import Library

import pandas as pd 

 

# Create DataFrame with Data

a = pd.DataFrame(Data)   
  
---  
  
__

__

Here, Data can be:

  1. One or more **_dictionaries_**
  2. One or more **_Series_**
  3.  ** _2D-numpy Ndarray_**

  
**Code #2: When Data is Dictionaries**

 __

 __  
 __

 __

 __  
 __  
 __

# Program to Create Data Frame with two dictionaries

 

# Define Dictionary 1

dict1 ={'a':1, 'b':2, 'c':3, 'd':4} 

 

# Define Dictionary 2 

dict2 ={'a':5, 'b':6, 'c':7, 'd':8,
'e':9} 

 

# Define Data with dict1 and dict2

Data = {'first':dict1, 'second':dict2} 

 

# Create DataFrame 

df = pd.DataFrame(Data)   
  
---  
  
__

__

**Output** :

    
    
    
    
    ![](https://media.geeksforgeeks.org/wp-content/uploads/panda5.png)
    
    DataFrame with two dictionaries
    
    
    

  
**Code #3: When Data is Series**

 __

 __  
 __

 __

 __  
 __  
 __

# Program to create Dataframe of three series

import pandas as pd

 

# Define series 1

s1 = pd.Series([1, 3, 4, 5, 6, 2, 9]) 

 

# Define series 2 

s2 = pd.Series([1.1, 3.5, 4.7, 5.8, 2.9, 9.3]) 

 

# Define series 3

s3 = pd.Series(['a', 'b', 'c', 'd', 'e']) 

 

# Define Data

Data ={'first':s1, 'second':s2, 'third':s3} 

 

# Create DataFrame

dfseries = pd.DataFrame(Data)   
  
---  
  
__

__

**Output** :

    
    
    
    
    ![](https://media.geeksforgeeks.org/wp-content/uploads/panda6.png)
    
    DataFrame with three series
    
    
    

  
**Code #4: When Data is 2D-numpy ndarray**  
 **Note** : One constraint has to be maintained while creating DataFrame of 2D
arrays – Dimensions of 2D array must be same

