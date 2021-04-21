Python | Delete rows/columns from DataFrame using Pandas.drop()



Python is a great language for doing data analysis, primarily because of the
fantastic ecosystem of data-centric Python packages. **_Pandas_** is one of
those packages and makes importing and analyzing data much easier.

Pandas provide data analysts a way to delete and filter data frame using
**.drop()** method. Rows or columns can be removed using index label or
column name using this method.

>  **Syntax:**  
>  DataFrame.drop(labels=None, axis=0, index=None, columns=None, level=None,
> inplace=False, errors=’raise’)
>
>  **Parameters:**
>
>  **labels:** String or list of strings referring row or column name.  
>  **axis:** int or string value, 0 ‘index’ for Rows and 1 ‘columns’ for
> Columns.  
>  **index or columns:** Single label or list. index or columns are an
> alternative to axis and cannot be used together.  
>  **level:** Used to specify level in case data frame is having multiple
> level index.  
>  **inplace:** Makes changes in original Data Frame if True.  
>  **errors:** Ignores error if any value from the list doesn’t exists and
> drops rest of the values when errors = ‘ignore’
>
>  
>
>
>  
>
>
>  **Return type:** Dataframe with dropped values

To download the CSV used in code, click here.  

 **Example #1: Dropping Rows by index label**  
In his code, A list of index labels is passed and the rows corresponding to
those labels are dropped using .drop() method.

 __

 __  
 __

 __

 __  
 __  
 __

# importing pandas module

import pandas as pd

 

# making data frame from csv file

data = pd.read_csv("nba.csv", index_col ="Name" )

 

# dropping passed values

data.drop(["Avery Bradley", "John Holland", "R.J. Hunter",

 "R.J. Hunter"], inplace = True)

 

# display

data  
  
---  
  
 __

 __

 **Output:**  
As shown in the output images, the new output doesn’t have the passed values.
Those values were dropped and the changes were made in the original data frame
since inplace was True.  
  
 **Data Frame before Dropping values-**  
![](https://media.geeksforgeeks.org/wp-content/uploads/pandas_drop1.jpg)  
  
 **Data Frame after Dropping values-**  
![](https://media.geeksforgeeks.org/wp-content/uploads/pandas_drop2.jpg)  
  

**Example #2 : Dropping columns with column name**

In his code, Passed columns are dropped using column names. axis parameter
is kept 1 since 1 refers to columns.

 __

 __  
 __

 __

 __  
 __  
 __

# importing pandas module

import pandas as pd

 

# making data frame from csv file

data = pd.read_csv("nba.csv", index_col ="Name" )

 

# dropping passed columns

data.drop(["Team", "Weight"], axis = 1, inplace = True)

 

# display

data  
  
---  
  
 __

 __

 **Output:**  
As shown in the output images, the new output doesn’t have the passed columns.
Those values were dropped since axis was set equal to 1 and the changes were
made in the original data frame since inplace was True.  
  
 **Data Frame before Dropping Columns-**  
![](https://media.geeksforgeeks.org/wp-content/uploads/pandas_drop3.jpg)  
  
 **Data Frame after Dropping Columns-**  
![](https://media.geeksforgeeks.org/wp-content/uploads/pandas_drop4.jpg)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

