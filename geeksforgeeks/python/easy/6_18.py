How to combine Groupby and Multiple Aggregate Functions in Pandas?



 **Pandas** is a Python package that offers various data structures and
operations for manipulating numerical data and time series. It is mainly
popular for importing and analyzing data much easier. It is an open-source
library that is built on top of NumPy library.

### Groupby()

Pandas dataframe.groupby() function is used to split the data in dataframe
into groups based on a given condition.

 **Example 1:**

 __

 __  
 __

 __

 __  
 __  
 __

# import library

import pandas as pd

 

# import csv file

df = pd.read_csv("https://bit.ly/drinksbycountry")

 

df.head()  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200504122035/groupbypic21.png)

 **Example 2:**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Find the average of each continent

# by grouping the data 

# based on the "continent".

df.groupby(["continent"]).mean()  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200504122531/groupbypic22.png)

### Aggregate()

Pandas dataframe.agg() function is used to do one or more operations on data
based on specified axis

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# here sum, minimum and maximum of column

# beer_servings is calculatad

df.beer_servings.agg(["sum", "min", "max"])  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200504122626/groupbypic31.png)

 **Using These two functions together:** We can find multiple aggregation
functions of a particular column grouped by another column.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# find an aggregation of column "beer_servings"

# by grouping the "continent" column.

df.groupby(df["continent"]).beer_servings.agg(["min",

 "max",

 "sum",

 "count",

 "mean"])  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200504122722/groupbypic41.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

