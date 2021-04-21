Applying Lambda functions to Pandas Dataframe



In Pandas, we have the freedom to add different functions whenever needed like
lambda function, sort function, etc. We can apply a lambda function to both
the columns and rows of the Pandas data frame.

 **Example 1:** Applying **lambda** function to **single column** using
Dataframe.assign()

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing pandas library

import pandas as pd

 

# creating and initializing a list

values=
[['Rohan',455],['Elvish',250],['Deepak',495],

 ['Soni',400],['Radhika',350],['Vansh',450]] 

 

# creating a pandas dataframe

df = pd.DataFrame(values,columns=['Name','Total_Marks'])

 

# Applying lambda function to find 

# percentage of 'Total_Marks' column 

# using df.assign()

df = df.assign(Percentage = lambda x: (x['Total_Marks']
/500 * 100))

 

# displaying the data frame

df  
  
---  
  
 __

 __

 **Output :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200731233755/newb.png)

  

  

In the above example, the lambda function is applied to the ‘Total_Marks’
column and a new column ‘Percentage’ is formed with the help of it.

 **Example 2:** Applying **lambda** function to **multiple columns** using
Dataframe.assign()

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing pandas library

import pandas as pd

 

# creating and initializing a nested list

values_list = [[15, 2.5, 100], [20, 4.5, 50],
[25, 5.2, 80],

 [45, 5.8, 48], [40, 6.3, 70], [41, 6.4,
90],

 [51, 2.3, 111]]

 

# creating a pandas dataframe

df = pd.DataFrame(values_list, columns=['Field_1', 'Field_2',
'Field_3'])

 

# Applying lambda function to find 

# the product of 3 columns using 

# df.assign()

df = df.assign(Product=lambda x: (x['Field_1'] *
x['Field_2'] * x['Field_3']))

 

# printing dataframe

df  
  
---  
  
 __

 __

 **Output :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200731232234/newa.png)

In the above example, lambda function is applied to 3 columns i.e ‘Field_1’,
‘Field_2’, and ‘Field_3’.

 **Example 3** : Applying **lambda** function to **single row** using
Dataframe.apply()

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# importing pandas and numpy libraries

import pandas as pd

import numpy as np

 

# creating and initializing a nested list

values_list = [[15, 2.5, 100], [20, 4.5, 50],
[25, 5.2, 80],

 [45, 5.8, 48], [40, 6.3, 70], [41, 6.4,
90], 

 [51, 2.3, 111]]

 

# creating a pandas dataframe

df = pd.DataFrame(values_list, columns=['Field_1', 'Field_2',
'Field_3'],

 index=['a', 'b', 'c', 'd', 'e', 'f',
'g'])

 

 

# Apply function numpy.square() to square

# the values of one row only i.e. row 

# with index name 'd'

df = df.apply(lambda x: np.square(x) if x.name == 'd'
else x, axis=1)

 

 

# printing dataframe

df  
  
---  
  
 __

 __

