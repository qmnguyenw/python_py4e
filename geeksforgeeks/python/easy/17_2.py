Get all rows in a Pandas DataFrame containing given substring



Let’s see how to get all rows in a Pandas DataFrame containing given substring
with the help of different examples.

 **Code #1:** Check the values PG in column Position

 __

 __  
 __

 __

 __  
 __  
 __

# importing pandas

import pandas as pd

 

# Creating the dataframe with dict of lists

df = pd.DataFrame({'Name': ['Geeks', 'Peter', 'James',
'Jack', 'Lisa'],

 'Team': ['Boston', 'Boston', 'Boston', 'Chele',
'Barse'],

 'Position': ['PG', 'PG', 'UG', 'PG', 'UG'],

 'Number': [3, 4, 7, 11, 5],

 'Age': [33, 25, 34, 35, 28],

 'Height': ['6-2', '6-4', '5-9', '6-1', '5-8'],

 'Weight': [89, 79, 113, 78, 84],

 'College': ['MIT', 'MIT', 'MIT', 'Stanford',
'Stanford'],

 'Salary': [99999, 99994, 89999, 78889, 87779]},

 index =['ind1', 'ind2', 'ind3', 'ind4', 'ind5'])

print(df, "\n")

 

print("Check PG values in Position column:\n")

df1 = df['Position'].str.contains("PG")

print(df1)  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/get_rows1.png)

But this result doesn’t seem very helpful, as it returns the bool values with
the index. Let’s see if we can do something better.  

**Code #2:** Getting the rows satisfying condition

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# importing pandas as pd

import pandas as pd

 

# Creating the dataframe with dict of lists

df = pd.DataFrame({'Name': ['Geeks', 'Peter', 'James',
'Jack', 'Lisa'],

 'Team': ['Boston', 'Boston', 'Boston', 'Chele',
'Barse'],

 'Position': ['PG', 'PG', 'UG', 'PG', 'UG'],

 'Number': [3, 4, 7, 11, 5],

 'Age': [33, 25, 34, 35, 28],

 'Height': ['6-2', '6-4', '5-9', '6-1', '5-8'],

 'Weight': [89, 79, 113, 78, 84],

 'College': ['MIT', 'MIT', 'MIT', 'Stanford',
'Stanford'],

 'Salary': [99999, 99994, 89999, 78889, 87779]},

 index =['ind1', 'ind2', 'ind3', 'ind4', 'ind5'])

 

df1 = df[df['Position'].str.contains("PG")]

print(df1)  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/get_rows2.png)

**Code #3:** Filter all rows where either Team contains ‘Boston’ or College
contains ‘MIT’.

 __

 __  
 __

 __

 __  
 __  
 __

# importing pandas

import pandas as pd

 

# Creating the dataframe with dict of lists

df = pd.DataFrame({'Name': ['Geeks', 'Peter', 'James',
'Jack', 'Lisa'],

 'Team': ['Boston', 'Boston', 'Boston', 'Chele',
'Barse'],

 'Position': ['PG', 'PG', 'UG', 'PG', 'UG'],

 'Number': [3, 4, 7, 11, 5],

 'Age': [33, 25, 34, 35, 28],

 'Height': ['6-2', '6-4', '5-9', '6-1', '5-8'],

 'Weight': [89, 79, 113, 78, 84],

 'College': ['MIT', 'MIT', 'MIT', 'Stanford',
'Stanford'],

 'Salary': [99999, 99994, 89999, 78889, 87779]},

 index =['ind1', 'ind2', 'ind3', 'ind4', 'ind5'])

 

 

df1 = df[df['Team'].str.contains("Boston") |
df['College'].str.contains('MIT')]

print(df1)  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/get_rows3.png)  
  
**Code #4:** Filter rows checking Team name contains ‘Boston and Position must
be PG.

 __

 __  
 __

 __

 __  
 __  
 __

# importing pandas module

import pandas as pd 

 

# making data frame 

df = pd.read_csv("https://media.geeksforgeeks.org/wp-
content/uploads/nba.csv") 

 

 

df1 = df[df['Team'].str.contains('Boston') &
df['Position'].str.contains('PG')]

df1  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/get_rows4.png)  

**Code #5:** Filter rows checking Position contains PG and College must
contains like UC.

 __

 __  
 __

 __

 __  
 __  
 __

# importing pandas module

import pandas as pd 

 

# making data frame 

df = pd.read_csv("https://media.geeksforgeeks.org/wp-
content/uploads/nba.csv") 

 

 

df1 = df[df['Position'].str.contains("PG") &
df['College'].str.contains('UC')]

df1  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/get_rows5.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

