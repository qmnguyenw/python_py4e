Rename specific column(s) in Pandas



Given a pandas Dataframe, let’s see how to rename specific column(s) names
using various methods.

First, let’s create a Dataframe:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import pandas package

import pandas as pd

 

# defining a dictionary

d = {"Name": ["John", "Mary", "Helen"],

 "Marks": [95, 75, 99],

 "Roll No": [12, 21, 9]}

 

# creating the pandas data frame

df = pd.DataFrame(d)

 

df  
  
---  
  
 __

 __

 **Output:**

![Dataframe](https://media.geeksforgeeks.org/wp-
content/uploads/20200724194359/Screenshot1062.png)

  

  

 **Method 1:** Using **Dataframe.rename()**.

This method is a way to rename the required columns in Pandas. It allows us to
specify the columns’ names to be changed in the form of a dictionary with the
keys and values as the current and new names of the respective columns.

**Example 1:** Renaming a single column.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import pandas package

import pandas as pd

 

# defining a dictionary

d = {"Name": ["John", "Mary", "Helen"],

 "Marks": [95, 75, 99],

 "Roll No": [12, 21, 9]}

 

# creating the pandas data frame

df = pd.DataFrame(d)

 

# displaying the columns 

# before renaming

print(df.columns)

 

# renaming the column "A"

df.rename(columns = {"Name": "Names"}, 

 inplace = True)

 

# displaying the columns after renaming

print(df.columns)  
  
---  
  
 __

 __

 **Output:**

![rename column](https://media.geeksforgeeks.org/wp-
content/uploads/20200724194358/Screenshot1061.png)

 **Example 2:** Renaming multiple columns.

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# import pandas package

import pandas as pd

 

# defining a dictionary

d = {"Name": ["John", "Mary", "Helen"],

 "Marks": [95, 75, 99],

 "Roll No": [12, 21, 9]}

 

# creating the pandas dataframe

df = pd.DataFrame(d)

 

# displaying the columns before renaming

print(df.columns)

 

# renaming the columns

df.rename({"Name": "Student Name", 

 "Marks": "Marks Obtained", 

 "Roll No": "Roll Number"}, 

 axis = "columns", inplace = True)

 

# displaying the columns after renaming

print(df.columns)  
  
---  
  
 __

 __

