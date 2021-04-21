Python | Pandas dataframe.ffill()



Python is a great language for doing data analysis, primarily because of the
fantastic ecosystem of data-centric python packages. **_Pandas_** is one of
those packages and makes importing and analyzing data much easier.

Pandas **dataframe.ffill()** function is used to fill the missing value in
the dataframe. ‘ffill’ stands for ‘forward fill’ and will propagate last valid
observation forward.

>  **Syntax:** DataFrame.ffill(axis=None, inplace=False, limit=None,
> downcast=None)
>
>  **Parameters:**  
>  **axis :** {0, index 1, column}  
>  **inplace :** If True, fill in place. Note: this will modify any other
> views on this object, (e.g. a no-copy slice for a column in a DataFrame).  
>  **limit :** If method is specified, this is the maximum number of
> consecutive NaN values to forward/backward fill. In other words, if there is
> a gap with more than this number of consecutive NaNs, it will only be
> partially filled. If method is not specified, this is the maximum number of
> entries along the entire axis where NaNs will be filled. Must be greater
> than 0 if not None.  
>  **Downcast:** a dict of item->dtype of what to downcast if possible, or the
> string ‘infer’ which will try to downcast to an appropriate equal type (e.g.
> float64 to int64 if possible)
>
>  **Returns :** filled : DataFrame
>
>  
>
>
>  
>

 **Example #1:** Use ffill() function to fill the missing values along the
index axis.  
 **Note :** When ffill() is applied across the index then any missing value
is filled based on the corresponding value in the previous row.

 __

 __  
 __

 __

 __  
 __  
 __

# importing pandas as pd

import pandas as pd

 

# Creating the dataframe 

df=pd.DataFrame({"A":[5,3,None,4],

 "B":[None,2,4,3],

 "C":[4,3,8,5],

 "D":[5,4,2,None]})

 

# Print the dataframe

df  
  
---  
  
 __

 __

![](https://media.geeksforgeeks.org/wp-content/uploads/1-487.png)

Let’s fill the missing value over the index axis

 __

 __  
 __

 __

 __  
 __  
 __

# applying ffill() method to fill the missing values

df.ffill(axis = 0)  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-content/uploads/1-488.png)  
Notice, values in the first row is still NaN value because there is no row
above it from which non-NA value could be propagated.  
  
**Example #2:** Use ffill() function to fill the missing values along the
column axis.  
 **Note :** When ffill is applied across the column axis, then missing values
are filled by the value in previous column in the same row.

 __

 __  
 __

 __

 __  
 __  
 __

# importing pandas as pd

import pandas as pd

 

# Creating the dataframe 

df=pd.DataFrame({"A":[5,3,None,4],

 "B":[None,2,4,3],

 "C":[4,3,8,5],

 "D":[5,4,2,None]})

 

# Print the dataframe

df  
  
---  
  
 __

 __

![](https://media.geeksforgeeks.org/wp-content/uploads/1-487.png)

Let’s fill the missing value over the column axis

 __

 __  
 __

 __

 __  
 __  
 __

# applying ffill() method to fill the missing values

df.ffill(axis = 1)  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-content/uploads/1-489.png)  
Notice, vlaues in the first column is NaN value, because there is no cell
left to it and so this cell cannot be filled using the previous cell value
along the column axis.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

