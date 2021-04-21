How to rename multiple column headers in a Pandas DataFrame?



In this article, we are going to rename multiple column headers using
**rename()** **** method. The rename method used to rename a single column as
well as rename multiple columns at a time. And pass columns that contain the
new values and inplace = true as an argument. We pass inplace = true because
we just modify the working data frame if we pass inplace = false then it
returns a new data frame.

 **Approach:**

  * Import pandas.
  * Create a data frame with multiple columns.
  * Create a dictionary and set key = old name, value= new name of columns header.
  * Assign the dictionary in columns .
  * Call the rename method and pass columns that contain dictionary and inplace=true as an argument.

 **Below is the implementation:**

 **Example 1:**

## Python

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# import pandas

import pandas as pd

 

# create data frame

df = pd.DataFrame({'First Name': ["Mukul", "Rohan",
"Mayank",

 "Vedansh", "Krishna"],

 

 'Location': ["Saharanpur", "Rampur", "Agra", 

 "Saharanpur", "Noida"],

 

 'Pay': [56000.0, 55000.0, 61000.0, 45000.0,
62000.0]})

 

# print original data frame

display(df)

 

# create a dictionary

# key = old name

# value = new name

dict = {'First Name': 'Name',

 'Location': 'City',

 'Pay': 'Salary'}

 

# call rename () method

df.rename(columns=dict,

 inplace=True)

 

# print Data frame after rename columns

display(df)  
  
---  
  
 __

 __

