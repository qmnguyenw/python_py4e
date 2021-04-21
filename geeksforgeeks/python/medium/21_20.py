Python | Pandas Series.astype() to convert Data type of series



Python is a great language for doing data analysis, primarily because of the
fantastic ecosystem of data-centric Python packages. **_Pandas_ **is one of
those packages and makes importing and analyzing data much easier.

Pandas **astype()** is the one of the most important methods. It is used to
change data type of a series. When data frame is made from a csv file, the
columns are imported and data type is set automatically which many times is
not what it actually should have. For example, a salary column could be
imported as string but to do operations we have to convert it into float.  
 **astype()** is used to do such data type conversions.

>  **Syntax:** DataFrame.astype(dtype, copy=True, errors=’raise’)
>
>  **Parameters:**  
>  **dtype:** Data type to convert the series into. (for example str, float,
> int)  
>  **copy:** Makes a copy of dataframe/series.  
>  **errors:** Error raising on conversion to invalid data type. For example
> dict to string. ‘raise’ will raise the error and ‘ignore’ will pass without
> raising error.
>
>  **Return type:** Series with changed data types
>
>  
>
>
>  
>

To download the data set used in following example, click here.  
In the following examples, the data frame used contains data of some NBA
players. The image of data frame before any operations is attached below.  
![](https://media.geeksforgeeks.org/wp-content/uploads/nba-1-1.png)

 **Example:**  
In this example, the data frame is imported and .dtypes is called on the data
frame to view the data types of series. After that some columns are converted
using .astype() method and the dtypes are viewed again to see the changes.

 __

 __  
 __

 __

 __  
 __  
 __

# importing pandas module

import pandas as pd

 

# reading csv file from url 

data = pd.read_csv("https://media.geeksforgeeks.org/wp-
content/uploads/nba.csv")

 

# dropping null value columns to avoid errors

data.dropna(inplace = True)

 

# storing dtype before converting

before = data.dtypes

 

# converting dtypes using astype

data["Salary"]= data["Salary"].astype(int)

data["Number"]= data["Number"].astype(str)

 

# storing dtype after converting

after = data.dtypes

 

# printing to compare

print("BEFORE CONVERSION\n", before, "\n")

print("AFTER CONVERSION\n", after, "\n")  
  
---  
  
 __

 __

 **Output:**  
As shown in the output image, the data types of columns were converted
accordingly.  
![](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-
from-2018-09-29-14-06-05.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

