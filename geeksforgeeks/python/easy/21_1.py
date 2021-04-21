Python | Pandas DataFrame.isin()



Python is a great language for doing data analysis, primarily because of the
fantastic ecosystem of data-centric python packages. **_Pandas_** is one of
those packages and makes importing and analyzing data much easier.

Pandas **isin()** method is used to filter data frames. isin() method
helps in selecting rows with having a particular(or Multiple) value in a
particular column.

>  **Syntax:** DataFrame.isin(values)
>
>  **Parameters:**  
>  **values:** iterable, Series, List, Tuple, DataFrame or dictionary to check
> in the caller Series/Data Frame.
>
>  **Return Type:** DataFrame of Boolean of Dimension.
>
>  
>
>
>  
>

To download the CSV file used, Click Here.  

 **Example #1: Single Parameter filtering**  
In the following Example, Rows are checked and a boolean series is returned
which is True wherever Gender=”Male”. Then the series is passed to data frame
to see new filtered data frame.

 __

 __  
 __

 __

 __  
 __  
 __

# importing pandas package

import pandas as pd

 

# making data frame from csv file

data = pd.read_csv("employees.csv")

 

# creating a bool series from isin()

new = data["Gender"].isin(["Male"])

 

# displaying data with gender = male only

data[new]  
  
---  
  
 __

 __

 **Output:**  
As shown in the output image, only Rows having gender = “Male” are returned.  
![](https://media.geeksforgeeks.org/wp-content/uploads/isin_1.jpg)

**Example #2: Multiple parameter Filtering**  
In the following example, the data frame is filtered on the basis of Gender as
well as Team. Rows having Gender=”Female” and Team=”Engineering”,
“Distribution” or “Finance” are returned.

 __

 __  
 __

 __

 __  
 __  
 __

# importing pandas package

import pandas as pd

 

# making data frame from csv file

data = pd.read_csv("employees.csv")

 

# creating filters of bool series from isin()

filter1 = data["Gender"].isin(["Female"])

filter2 = data["Team"].isin(["Engineering", "Distribution",
"Finance" ])

 

# displaying data with both filter applied and mandatory 

data[filter1 & filter2]  
  
---  
  
 __

 __

 **Output:**  
As shown in the output image, Rows having Gender=”Female” and
Team=”Engineering”, “Distribution” or “Finance” are returned.

![](https://media.geeksforgeeks.org/wp-content/uploads/isin_2.jpg)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

