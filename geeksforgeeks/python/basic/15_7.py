Different ways to import csv file in Pandas



CSV files are the “comma separated values”, these values are separated by
commas, this file can be view like as excel file. In Python, Pandas is the
most important library coming to data science. We need to deal with huge
datasets while analyzing the data, which usually can get in CSV file format.

Let’s see the different ways to import csv file in Pandas.

 **Method #1:** Using read_csv() method.

 __

 __  
 __

 __

 __  
 __  
 __

# importing pandas module

import pandas as pd 

 

# making data frame 

df = pd.read_csv("https://media.geeksforgeeks.org/wp-
content/uploads/nba.csv") 

 

df.head(10)   
  
---  
  
__

__

**Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/import_csv1.png)

  
Providing _file_path_.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# import pandas as pd

import pandas as pd

 

# Takes the file's folder

filepath = r"C:\Gfg\datasets\nba.csv"

 

# read the CSV file

df = pd.read_csv(filepath)

 

# print the first five rows

print(df.head())  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/import_csv2.png)  
  
**Method #2:** Using csv module.

One can directly import the csv files using csv module.

 __

 __  
 __

 __

 __  
 __  
 __

# import the module csv

import csv

import pandas as pd

 

# open the csv file

with open(r"C:\Users\Admin\Downloads\nba.csv") as csv_file: 

 

 # read the csv file

 csv_reader = csv.reader(csv_file, delimiter=',')

 

 # now we can use this csv files into the pandas

 df = pd.DataFrame([csv_reader], index=None)

 df.head()

 

# iterating values of first column

for val in list(df[1]):

 print(val)  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/import_csv3.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

