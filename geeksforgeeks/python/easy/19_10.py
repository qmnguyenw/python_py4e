Python | Pandas Series.lt()



Python is a great language for doing data analysis, primarily because of the
fantastic ecosystem of data-centric Python packages. **_Pandas_** is one of
those packages and makes importing and analyzing data much easier.

Pandas **Series.lt()** is used to compare two series and return Boolean
value for every respective element.  

>  **Syntax:** Series.lt(other, level=None, fill_value=None, axis=0)
>
>  **Parameters:**  
>  **other:** other series to be compared with  
>  **level:** int or name of level in case of multi level  
>  **fill_value:** Value to be replaced instead of NaN  
>  **axis:** 0 or ‘index’ to apply method by rows and 1 or ‘columns’ to apply
> by columns.
>
>  **Return type:** Boolean series
>
>  
>
>
>  
>

 **Note:** The results are returned on the basis of comparison caller series <
other series.

To download the data set used in following example, click here.

In the following examples, the data frame used contains data of some NBA
players. The image of data frame before any operations is attached below.  
![](https://media.geeksforgeeks.org/wp-content/uploads/nba-1-1.png)

 **Example #1:**

In this example, the Age column and Weight columns are compared using .lt()
method. Since values in weight columns are very large as compared to Age
column, hence the values are divided by 10 first. Before comparing, Null rows
are removed using .dropna() method to avoid errors.

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

data = pd.read_csv("https://media.geeksforgeeks.org/wp-
content/uploads/nba.csv") 

 

# removing null values to avoid errors 

data.dropna(inplace = True) 

 

# other series

other = data["Weight"]/10

 

# calling method and returning to new column

data["Age < Weight"]= data["Age"].lt(other)

 

# display

data  
  
---  
  
 __

 __

 **Output:**  
As shown in the output image, the new column has True wherever value in Age
column is less than Weight/10.  
![](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-
from-2018-10-12-02-08-43.png)  
  
**Example #2:** Handling NaN values

In this example, two series are created using pd.Series(). The series
contains null value too and hence 10 is passed to fill_value parameter to
replace null values by 10.

 __

 __  
 __

 __

 __  
 __  
 __

# importing pandas module

import pandas as pd 

 

# importing numpy module

import numpy as np

 

# creating series 1

series1 = pd.Series([11, 21, 2, 43, 9, 27,
np.nan, 110, np.nan])

 

# creating series 2

series2 = pd.Series([16, np.nan, 2, 23, 5, 40,
np.nan, 0, 19])

 

# setting null replacement value

na_replace = 10

 

# calling and storing result

result = series1.lt(series2, fill_value = na_replace)

 

# display

result  
  
---  
  
 __

 __

 **Output:**  
As it can be seen in output, NaN values were replaced by 5 and the comparison
is performed after the replacement and new values are used for comparison.

    
    
    0     True
    1    False
    2    False
    3    False
    4    False
    5     True
    6    False
    7    False
    8     True
    dtype: bool
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

