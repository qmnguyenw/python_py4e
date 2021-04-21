Python | Data Comparison and Selection in Pandas



Python is a great language for doing data analysis, primarily because of the
fantastic ecosystem of data-centric Python packages. **_Pandas_** is one of
those packages, and makes importing and analyzing data much easier.

The most important thing in Data Analysis is comparing values and selecting
data accordingly. The “==” operator works for multiple values in a Pandas Data
frame too. Following two examples will show how to compare and select data
from a Pandas Data frame.

To download the CSV file used, Click Here.

 **Example #1:** Comparing Data  
In the following example, a data frame is made from a csv file. In the Gender
Column, there are only 3 types of values (“Male”, “Female” or NaN). Every row
of Gender column is compared to “Male” and a boolean series is returned after
that.

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

 

# storing boolean series in new

new = data["Gender"] == "Male"

 

# inserting new series in data frame

data["New"]= new

 

# display

data  
  
---  
  
 __

 __

 **Output:**  
As show in the output image, for Gender= “Male”, the value in New Column is
True and for “Female” and NaN values it is False.

  

  

![](https://media.geeksforgeeks.org/wp-content/uploads/comp_date1-1.jpg)  
  
**Example #2:** Selecting Data  
In the following example, the boolean series is passed to the data and only
Rows having Gender=”Male” are returned.

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

 

# storing boolean series in new

new = data["Gender"] != "Female"

 

# inserting new series in data frame

data["New"]= new

 

# display

data[new]

 

# OR 

# data[data["Gender"]=="Male"]

# Both are the same  
  
---  
  
 __

 __

 **Output:**  
As shown in the output image, Data frame having Gender=”Male” is returned.

![](https://media.geeksforgeeks.org/wp-content/uploads/comp_date2-1.jpg)

 **Note:** For NaN values, the boolean value is False.  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

