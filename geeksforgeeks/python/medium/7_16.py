Get minimum values in rows or columns with their index position in Pandas-
Dataframe



Let’s discuss how to find minimum values in rows & columns of a Dataframe and
also their index position.

 **a) Find the minimum value among rows and columns :**

Dataframe.min() : This function returns the minimum of the values in the given
object. If the input is a series, the method will return a scalar which will
be the minimum of the values in the series. If the input is a dataframe, then
the method will return a series with a minimum of values over the specified
axis in the dataframe. By default, the axis is the index axis.

 **1) Get minimum values of every column :**  
Use min() function to find the minimum value over the index axis.

 **Code :**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# import pandas library

import pandas as pd

 

# list of Tuples

data = [

 (20, 16, 23),

 (30, None, 11),

 (40, 34, 11),

 (50, 35, None),

 (60, 40, 13)

 ]

 

# creating a DataFrame object

df = pd.DataFrame(data, index = ['a', 'b', 'c', 'd',
'e'],

 columns = ['x', 'y', 'z'])

 

# getting a series object containing 

# minimum value from each column

# of given dataframe

minvalue_series = df.min()

 

minvalue_series  
  
---  
  
 __

 __

 **Output:**

![pandas-get-minimum-1](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20200702203700/pandas-get-minimum-1.png)

 **2) Get minimum values of every row :**  
Use min() function on a dataframe with ‘axis = 1’ attribute to find the
minimum value over the row axis.

 **Code :**

 __

 __  
 __

 __

 __  
 __  
 __

# import pandas library

import pandas as pd

 

# list of Tuples

data = [

 (20, 16, 23),

 (30, None, 11),

 (40, 34, 11),

 (50, 35, None),

 (60, 40, 13)

 ]

 

# creating a DataFrame object

df = pd.DataFrame(data, index = ['a', 'b', 'c', 'd',
'e'],

 columns = ['x', 'y', 'z'])

 

# getting a series object containing 

# minimum value from each row

# of given dataframe

minvalue_series = df.min(axis = 1)

 

minvalue_series  
  
---  
  
 __

 __

 **Output:**

![pandas-get-minimum-2](https://media.geeksforgeeks.org/wp-
content/uploads/20200702203118/pandas-get-minimum-2.png)

 **3) Get minimum values of every column without skipping None Value :**  
Use min() function on a dataframe which has Na value with ‘skipna = False’
attribute to find the minimum value over the column axis.

 **Code :**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# import pandas library

import pandas as pd

 

# list of Tuples

data = [

 (20, 16, 23),

 (30, None, 11),

 (40, 34, 11),

 (50, 35, None),

 (60, 40, 13)

 ]

 

# creating a DataFrame object

df = pd.DataFrame(data, index = ['a', 'b', 'c', 'd',
'e'],

 columns = ['x', 'y', 'z'])

 

# getting a series object containing 

# minimum value from each column

# of given dataframe without

# skipping None value

minvalue_series = df.min(skipna = False)

 

minvalue_series  
  
---  
  
 __

 __

 **Output:**

![pandas-get-minimum-3](https://media.geeksforgeeks.org/wp-
content/uploads/20200702203231/pandas-get-minimum-3.png)

 **4) Get minimum value of a single column :**  
Use min() function on a series to find the minimum value in the series.

 **Code :**

 __

 __  
 __

 __

 __  
 __  
 __

# import pandas library

import pandas as pd

 

# list of Tuples

data = [

 (20, 16, 23),

 (30, None, 11),

 (40, 34, 11),

 (50, 35, None),

 (60, 40, 13)

 ]

 

# creating a DataFrame object

df = pd.DataFrame(data, index = ['a', 'b', 'c', 'd',
'e'],

 columns = ['x', 'y', 'z'])

 

# getting a minimum value

# from column 'x'

minvalue = df['x'].min()

 

minvalue  
  
---  
  
 __

 __

 **Output:**

    
    
    20

 **b) Get row index label or position of minimum values among rows and columns
:**

Dataframe.idxmin() : This function returns index of first occurrence of
minimum over requested axis. While finding the index of the minimum value
across any index, all NA/null values are excluded.

 **1) Get row index label of minimum value in every column :**  
Use idxmin() function to find the index/label of the minimum value along the
index axis.

 **Code :**

 __

 __  
 __

 __

 __  
 __  
 __

# import pandas library

import pandas as pd

 

# list of Tuples

data = [

 (20, 16, 23),

 (30, None, 11),

 (40, 34, 11),

 (50, 35, None),

 (60, 40, 13)

 ]

 

# creating a DataFrame object

df = pd.DataFrame(data, index = ['a', 'b', 'c', 'd',
'e'],

 columns = ['x', 'y', 'z'])

 

# get the index position\label of

# minimum values in every column

minvalueIndexLabel = df.idxmin()

 

minvalueIndexLabel  
  
---  
  
 __

 __

 **Output**

![pandas-get-minimum-5](https://media.geeksforgeeks.org/wp-
content/uploads/20200702203357/pandas-get-minimum-5.png)

 **2) Get Column names of minimum value in every row :**  
Use idxmin() function with ‘axis = 1’ attribute to find the index/label of
the minimum value along the column axis.

 **Code :**

 __

 __  
 __

 __

 __  
 __  
 __

# import pandas library

import pandas as pd

 

# list of Tuples

data = [

 (20, 16, 23),

 (30, None, 11),

 (40, 34, 11),

 (50, 35, None),

 (60, 40, 13)

 ]

 

# creating a DataFrame object

df = pd.DataFrame(data, index = ['a', 'b', 'c', 'd',
'e'],

 columns = ['x', 'y', 'z'])

 

# get the index position\label of

# minimum values in every row

minvalueIndexLabel = df.idxmin(axis = 1)

 

minvalueIndexLabel  
  
---  
  
 __

 __

 **Output**

![pandas-get-minimum-4](https://media.geeksforgeeks.org/wp-
content/uploads/20200702203451/pandas-get-minimum-4.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

