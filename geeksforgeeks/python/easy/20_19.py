Python | Pandas Dataframe.duplicated()



Python is a great language for doing data analysis, primarily because of the
fantastic ecosystem of data-centric python packages. **_Pandas_** is one of
those packages and makes importing and analyzing data much easier.

An important part of Data analysis is analyzing _Duplicate Values_ and
removing them. Pandas **duplicated()** method helps in analyzing duplicate
values only. It returns a boolean series which is True only for Unique
elements.

 **Syntax:**

    
    
    DataFrame.duplicated(subset=None, keep='first')

 **Parameters:**

>  **subset:** Takes a column or list of column label. It’s default value is
> none. After passing columns, it will consider them only for duplicates.  
>  **keep:** Controls how to consider duplicate value. It has only three
> distinct value and default is ‘first’.  
>  **– > **If ‘first’, it considers first value as unique and rest of the same
> values as duplicate.  
>  **– > **If ‘last’, it considers last value as unique and rest of the same
> values as duplicate.  
>  **– > **If False, it consider all of the same values as duplicates.
>
>  
>
>
>  
>

To download the CSV file used, Click Here.  
  
 **Example #1:** Returning a boolean series

In the following example, a boolean series is returned on the basis of
duplicate values in the First Name column.

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

 

# sorting by first name

data.sort_values("First Name", inplace = True)

 

# making a bool series

bool_series = data["First Name"].duplicated()

 

# displaying data

data.head()

 

# display data

data[bool_series]  
  
---  
  
 __

 __

 **Output:**  
As shown in the output image, since the keep parameter was default that is
‘first’, hence whenever the name is occured, the first one is considered
Unique and res Duplicate.

![](https://media.geeksforgeeks.org/wp-content/uploads/out1-13.jpg)

**Example #2:** Removing duplicates  
In this example, the keep parameter is set to False, so that only Unique
values are taken and the duplicate values are removed from data.

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

 

# sorting by first name

data.sort_values("First Name", inplace = True)

 

# making a bool series

bool_series = data["First Name"].duplicated(keep = False)

 

# bool series

bool_series

 

# passing NOT of bool series to see unique values only

data = data[~bool_series]

 

# displaying data

data.info()

data  
  
---  
  
 __

 __

 **Output:**  
Since the duplicated() method returns False for Duplicates, the NOT of the
series is taken to see unique value in Data Frame.

![](https://media.geeksforgeeks.org/wp-content/uploads/out3-6.jpg)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

