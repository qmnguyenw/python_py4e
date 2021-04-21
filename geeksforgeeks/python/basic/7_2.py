Data profiling in Pandas using Python



 **Pandas** is one of the most popular Python library mainly used for data
manipulation and analysis. When we are working with large data, many times we
need to perform **Exploratory Data Analysis**. We need to get the detailed
description about different columns available and there relation, null check,
data types, missing values, etc. So, Pandas profiling is the python module
which does the EDA and gives detailed description just with a few lines of
code.

 **Installation:**

    
    
    pip install pandas-profiling

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

#import the packages

import pandas as pd

import pandas_profiling

 

# read the file

df = pd.read_csv('Geeks.csv')

 

# run the profile report

profile = df.profile_report(title='Pandas Profiling Report')

 

# save the report as html file

profile.to_file(output_file="pandas_profiling1.html")

 

# save the report as json file

profile.to_file(output_file="pandas_profiling2.json")  
  
---  
  
 __

 __

 **Output:**

![python-data-profiling-1](https://media.geeksforgeeks.org/wp-
content/uploads/20200422152309/python-data-profiling-1.png)

  

  

 **HTML File:**

![python-data-profiling-html-file](https://media.geeksforgeeks.org/wp-
content/uploads/20200422152427/python-data-profiling-html-file.png)

 **JSON File:**

![python-data-profiling-json-file](https://media.geeksforgeeks.org/wp-
content/uploads/20200422152541/python-data-profiling-json-file.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

