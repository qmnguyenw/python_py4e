Insert row at given position in Pandas Dataframe



Inserting a row in Pandas DataFrame is a very straight forward process and we
have already discussed approaches in how insert rows at the start of the
Dataframe. Now, let’s discuss the ways in which we can insert a row at any
position in the dataframe having integer based index.

 **Solution #1 :** There does not exist any in-built function in pandas which
will help us to insert a row at any specific position in the given dataframe.
So, we are going to write our own customized function to achieve the result.

 **Note :** Inserting rows in-between the rows in Pandas Dataframe is an
inefficient operation and the user should avoid it.

 __

 __  
 __

 __

 __  
 __  
 __

# importing pandas as pd

import pandas as pd

 

# Let's create the dataframe

df = pd.DataFrame({'Date':['10/2/2011', '12/2/2011',
'13/2/2011', '14/2/2011'],

 'Event':['Music', 'Poetry', 'Theatre', 'Comedy'],

 'Cost':[10000, 5000, 15000, 2000]})

 

# Let's visualize the dataframe

print(df)  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-content/uploads/1-1674.png)

Now we will write a customized function to insert a row at any given position
in the dataframe.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Function to insert row in the dataframe

def Insert_row(row_number, df, row_value):

 # Starting value of upper half

 start_upper = 0

 

 # End value of upper half

 end_upper = row_number

 

 # Start value of lower half

 start_lower = row_number

 

 # End value of lower half

 end_lower = df.shape[0]

 

 # Create a list of upper_half index

 upper_half = [*range(start_upper, end_upper, 1)]

 

 # Create a list of lower_half index

 lower_half = [*range(start_lower, end_lower, 1)]

 

 # Increment the value of lower half by 1

 lower_half = [x.__add__(1) for x in lower_half]

 

 # Combine the two lists

 index_ = upper_half + lower_half

 

 # Update the index of the dataframe

 df.index = index_

 

 # Insert a row at the end

 df.loc[row_number] = row_value

 

 # Sort the index labels

 df = df.sort_index()

 

 # return the dataframe

 return df

 

# Let's create a row which we want to insert

row_number = 2

row_value = ['11/2/2011', 'Wrestling', 12000]

 

if row_number > df.index.max()+1:

 print("Invalid row_number")

else:

 

 # Let's call the function and insert the row

 # at the second position

 df = Insert_row(row_number, df, row_value)

 

 # Print the updated dataframe

 print(df)  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-content/uploads/1-1675.png)  
In case the given row_number is invalid, say total number of rows in dataframe
are 100 then maximum value of row_number can be 101, i.e. adding row at the
last of dataframe. Any number greater than 101 will given an _error_ message.  
  
**Example #2:** Another customized function which will use Pandas.concat()
function to insert a row at any given position in the dataframe.

 __

 __  
 __

 __

 __  
 __  
 __

# importing pandas as pd

import pandas as pd

 

# Let's create the dataframe

df = pd.DataFrame({'Date':['10/2/2011', '12/2/2011',
'13/2/2011', '14/2/2011'],

 'Event':['Music', 'Poetry', 'Theatre', 'Comedy'],

 'Cost':[10000, 5000, 15000, 2000]})

 

# Let's visualize the dataframe

print(df)  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-content/uploads/1-1674.png)

A customized function to insert a row at any given position in the dataframe.

 __

 __  
 __

 __

 __  
 __  
 __

# Function to insert row in the dataframe

def Insert_row_(row_number, df, row_value):

 # Slice the upper half of the dataframe

 df1 = df[0:row_number]

 

 # Store the result of lower half of the dataframe

 df2 = df[row_number:]

 

 # Inser the row in the upper half dataframe

 df1.loc[row_number]=row_value

 

 # Concat the two dataframes

 df_result = pd.concat([df1, df2])

 

 # Reassign the index labels

 df_result.index = [*range(df_result.shape[0])]

 

 # Return the updated dataframe

 return df_result

 

# Let's create a row which we want to insert

row_number = 2

row_value = ['11/2/2011', 'Wrestling', 12000]

 

if row_number > df.index.max()+1:

 print("Invalid row_number")

else:

 

 # Let's call the function and insert the row

 # at the second position

 df = Insert_row_(2, df, row_value)

 

 # Print the updated dataframe

 print(df)  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-content/uploads/1-1675.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

