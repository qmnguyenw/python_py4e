Python | Pandas dataframe.insert()



Pandas insert method allows the user to insert a column in a dataframe or
series(1-D Data frame). A column can also be inserted manually in a data frame
by the following method, but there isn’t much freedom here.  
For example, even column location can’t be decided and hence the inserted
column is always inserted in the last position.

 **Syntax:**

    
    
    DataFrameName.insert(loc, column, value, allow_duplicates = False)

 **Parameters:**

>  **loc:** loc is an integer which is the location of column where we want to
> insert new column. This will shift the existing column at that position to
> the right.  
>  **column:** column is a string which is name of column to be inserted.  
>  **value:** value is simply the value to be inserted. It can be int, string,
> float or anything or even series / List of values. Providing only one value
> will set the same value for all rows.  
>  **allow_duplicates :** allow_duplicates is a boolean value which checks if
> column with same name already exists or not.

Find the link to csv file used from here.

  

  

#### Inserting a column with static value:

####

 __

 __  
 __

 __

 __  
 __  
 __

# importing pandas module

import pandas as pd

 

# reading csv file

data = pd.read_csv("pokemon.csv")

 

# displying dataframe - Output 1

data.head()  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/pandas_1.jpg)

 **After Inserting column:**

 __

 __  
 __

 __

 __  
 __  
 __

# importing pandas module

import pandas as pd

 

# reading csv file

data = pd.read_csv("pokemon.csv")

 

# displying dataframe - Output 1

data.head()

 

# inserting column with static value in data frame

data.insert(2, "Team", "Any")

 

# displaying data frame again - Output 2

data.head()  
  
---  
  
 __

 __

![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/pandas2.jpg)

#### Passing series with different value for each row:

In this example, a series is created and some values are passed to the series
through a for loop. After that, the series is passed in pandas insert function
to append series in the Data frame with values passed.

 __

 __  
 __

 __

 __  
 __  
 __

# importing pandas module

import pandas as pd

 

# creating a blank series

Type_new = pd.Series([])

 

# reading csv file

data = pd.read_csv("pokemon.csv")

 

 

# running a for loop and asigning some values to series

for i in range(len(data)):

 if data["Type"][i] == "Grass":

 Type_new[i]="Green"

 

 elif data["Type"][i] == "Fire":

 Type_new[i]="Orange"

 

 elif data["Type"][i] == "Water":

 Type_new[i]="Blue"

 

 else:

 Type_new[i]= data["Type"][i]

 

 

# inserting new column with values of list made above 

data.insert(2, "Type New", Type_new)

 

# list output

data.head()  
  
---  
  
 __

 __

##### Output:

![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/pandas3-1.jpg)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

