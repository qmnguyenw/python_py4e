Creating a dataframe using Excel files



Let’s see how to read excel files to Pandas dataframe objects using
**Pandas**.

 **Code #1 :** Read an excel file using read_excel() method of pandas.

 __

 __  
 __

 __

 __  
 __  
 __

# import pandas lib as pd

import pandas as pd

 

# read by default 1st sheet of an excel file

dataframe1 = pd.read_excel('SampleWork.xlsx')

 

print(dataframe1)  
  
---  
  
 __

 __

 **Output :**

    
    
            Name  Age    Stream  Percentage
    0      Ankit   18      Math          95
    1      Rahul   19   Science          90
    2    Shaurya   20  Commerce          85
    3  Aishwarya   18      Math          80
    4   Priyanka   19   Science          75
    

  
**Code #2 :** Reading Specific Sheets using 'sheet_name' of read_excel()
method.

 __

 __  
 __

 __

 __  
 __  
 __

# import pandas lib as pd

import pandas as pd

 

# read 2nd sheet of an excel file

dataframe2 = pd.read_excel('SampleWork.xlsx', sheet_name = 1)

 

print(dataframe2)  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
           Name  Age    Stream  Percentage
    0     Priya   18      Math          95
    1  shivangi   19   Science          90
    2      Jeet   20  Commerce          85
    3    Ananya   18      Math          80
    4   Swapnil   19   Science          75
    

  
**Code #3 :** Reading Specific Columns using 'usecols' parameter of
read_excel() method.

 __

 __  
 __

 __

 __  
 __  
 __

# import pandas lib as pd

import pandas as pd

 

require_cols = [0, 3]

 

# only read specific columns from an excel file

required_df = pd.read_excel('SampleWork.xlsx', usecols =
require_cols)

 

print(required_df)  
  
---  
  
 __

 __

 **Output :**

    
    
            Name  Percentage
    0      Ankit          95
    1      Rahul          90
    2    Shaurya          85
    3  Aishwarya          80
    4   Priyanka          75
    

  
**Code #4 :** Handling missing data using 'na_values' parameter of the
read_excel() method.

 __

 __  
 __

 __

 __  
 __  
 __

# import pandas lib as pd

import pandas as pd

 

# Handling missing values of 3rd sheet of an excel file.

dataframe = pd.read_excel('SampleWork.xlsx', na_values =
"Missing",

 sheet_name = 2)

 

print(dataframe)  
  
---  
  
 __

 __

 **Output :**

    
    
           Name  Age   Stream  Percentage
    0     Priya   18     Math          95
    1  shivangi   19  Science          90
    2      Jeet   20      NaN          85
    3    Ananya   18     Math          80
    4   Swapnil   19  Science          75
    

  
**Code #5 :** Skip starting rows when Reading an Excel File using 'skiprows'
parameter of read_excel() method.

 __

 __  
 __

 __

 __  
 __  
 __

# import pandas lib as pd

import pandas as pd

 

# read 2nd sheet of an excel file after

# skipping starting two rows 

df = pd.read_excel('SampleWork.xlsx', sheet_name = 1, skiprows
= 2)

 

print(df)  
  
---  
  
 __

 __

 **Output :**

    
    
      shivangi  19   Science  90
    0     Jeet  20  Commerce  85
    1   Ananya  18      Math  80
    2  Swapnil  19   Science  75
    

  
**Code #6 :** Set the header to any row and start reading from that row, using
'header' parameter of the read_excel() method.

 __

 __  
 __

 __

 __  
 __  
 __

# import pandas lib as pd

import pandas as pd

 

# setting the 3rd row as header.

df = pd.read_excel('SampleWork.xlsx', sheet_name = 1, header
= 2)

 

print(df)  
  
---  
  
 __

 __

 **Output :**

    
    
      shivangi  19   Science  90
    0     Jeet  20  Commerce  85
    1   Ananya  18      Math  80
    2  Swapnil  19   Science  75
    

  
**Code #7 :** Reading Multiple Excel Sheets using 'sheet_name' parameter of
the read_excel()method.

 __

 __  
 __

 __

 __  
 __  
 __

# import pandas lib as pd

import pandas as pd

 

# read both 1st and 2nd sheet.

df = pd.read_excel('SampleWork.xlsx', na_values = "Mssing",

 sheet_name =[0, 1])

 

print(df)  
  
---  
  
 __

 __

 **Output :**

    
    
    OrderedDict([(0,         Name  Age    Stream  Percentage
    0      Ankit   18      Math          95
    1      Rahul   19   Science          90
    2    Shaurya   20  Commerce          85
    3  Aishwarya   18      Math          80
    4   Priyanka   19   Science          75),
    
    (1,        Name  Age    Stream  Percentage
    0     Priya   18      Math          95
    1  shivangi   19   Science          90
    2      Jeet   20  Commerce          85
    3    Ananya   18      Math          80
    4   Swapnil   19   Science          75)])
    

  
**Code #8 :** Reading all Sheets of the excel file together using
'sheet_name' parameter of the read_excel() method.

 __

 __  
 __

 __

 __  
 __  
 __

# import pandas lib as pd

import pandas as pd

 

# read all sheets together.

all_sheets_df = pd.read_excel('SampleWork.xlsx', na_values =
"Missing",

 sheet_name = None)

 

print(all_sheets_df)  
  
---  
  
 __

 __

 **Output :**

    
    
    OrderedDict([('Sheet1',         Name  Age    Stream  Percentage
    0      Ankit   18      Math          95
    1      Rahul   19   Science          90
    2    Shaurya   20  Commerce          85
    3  Aishwarya   18      Math          80
    4   Priyanka   19   Science          75),
    
    ('Sheet2',        Name  Age    Stream  Percentage
    0     Priya   18      Math          95
    1  shivangi   19   Science          90
    2      Jeet   20  Commerce          85
    3    Ananya   18      Math          80
    4   Swapnil   19   Science          75), 
    
    ('Sheet3',        Name  Age   Stream  Percentage
    0     Priya   18     Math          95
    1  shivangi   19  Science          90
    2      Jeet   20      NaN          85
    3    Ananya   18     Math          80
    4   Swapnil   19  Science          75)])
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

