Concatenate Pandas DataFrames Without Duplicates



In this article, we are going to concatenate two dataframes using _pandas_
module.

In order to perform concatenation of two dataframes, we are going to use the
_pandas.concat().drop_duplicates()_ method in _pandas_ module.

 **Step-by-step Approach:**

  * Import module.
  * Load two sample dataframes as variables.
  * Concatenate the dataframes using ****_pandas.concat().drop_duplicates()_ **** method.
  * Display the new dataframe generated.

 **Below are some examples which depict how to perform concatenation between
two dataframes using** _ **pandas**_ **module without duplicates:**

 **Example 1:**

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Importing pandas library

import pandas as pd

 

# loading dataframes

dataframe1 = pd.DataFrame({'columnA': [20, 30, 40],

 'columnB': [200, 300, 400]})

 

dataframe2 = pd.DataFrame({'columnA': [50, 20, 60],

 'columnB': [500, 200, 600]})

 

# Concatenating dataframes without duplicates

new_dataframe = pd.concat([dataframe1, dataframe2]).drop_duplicates()

 

# Display concatenated dataframe

new_dataframe  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201215221609/Screenshot184.png)

Here, we have concatenated two dataframes using _pandas.concat()_ method.

 **Example 2:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Importing pandas library

import pandas as pd

 

# loading dataframes

dataframe1 = pd.DataFrame({'name': ['rahul', 'anjali',
'kajal'],

 'age': [23, 28, 30]})

 

dataframe2 = pd.DataFrame({'name': ['devesh', 'rashi',
'anjali'],

 'age': [20, 15, 28]})

 

# Concatenating two dataframes wtithout duplicates

new_dataframe = pd.concat([dataframe1, dataframe2]).drop_duplicates()

 

# Resetting index

new_dataframe = new_dataframe.reset_index(drop=True)

 

# Display dataframe generated

new_dataframe  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201215222029/Screenshot185.png)

  

  

As shown in the output image, we get the concatenation of dataframes without
removing duplicates.

 **Example 3:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Importing pandas libraray

import pandas as pd

 

# Loading dataframes

dataframe1 = pd.DataFrame({'empname': ['rohan', 'hina',
'alisa', ],

 'department': ['IT', 'admin', 'finance', ],

 'designation': ['Sr.developer', 'administrator',
'executive', ]})

 

dataframe2 = pd.DataFrame({'empname': ['rishi', 'huma',
'alisa', ],

 'department': ['cyber security', 'HR', 'finance', ],

 'designation': ['penetration tester', 'HR executive',
'executive', ]})

 

# Concatenating two dataframes wtithout duplicates

new_dataframe = pd.concat([dataframe1, dataframe2]).drop_duplicates()

 

# Resetting index

new_dataframe = new_dataframe.reset_index(drop=True)

 

# Display dataframe generated

new_dataframe  
  
---  
  
 __

 __

 **Output:**

Here is another example, which depicts how to concatenate two dataframes.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

