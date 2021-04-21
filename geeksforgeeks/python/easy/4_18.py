How to Convert Integer to Datetime in Pandas DataFrame?



Let’s discuss how to convert an Integer to Datetime in it. Now to convert
Integers to Datetime in Pandas DataFrame, we can use the following syntax:

> df[‘DataFrame Column’] = pd.to_datetime(df[‘DataFrame Column’],
> format=specify your format)

 **Note:** The integers data must match the format specified.

 **Example #1:**

## Python

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# importing pandas package

import pandas as pd

 

# creating a dataframe

values = {'Dates': [20190902, 20190913, 20190921],

 'Attendance': ['Attended', 'Not Attended', 'Attended']

 }

 

df = pd.DataFrame(values, columns=['Dates', 'Attendance'])

 

# display

print(df)

print(df.dtypes)  
  
---  
  
 __

 __

