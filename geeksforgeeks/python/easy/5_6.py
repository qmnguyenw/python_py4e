Loop or Iterate over all or certain columns of a dataframe in Python-Pandas



In this article, we will discuss how to loop or Iterate overall or certain
columns of a DataFrame? There are various methods to achieve this task.

Let’s first create a Dataframe and see that :  
 **Code :**

 __

 __  
 __

 __

 __  
 __  
 __

# import pandas package

import pandas as pd

 

# List of Tuples

students = [('Ankit', 22, 'A'),

 ('Swapnil', 22, 'B'),

 ('Priya', 22, 'B'),

 ('Shivangi', 22, 'B'),

 ]

# Create a DataFrame object

stu_df = pd.DataFrame(students, columns =['Name', 'Age',
'Section'],

 index =['1', '2', '3', '4'])

 

stu_df  
  
---  
  
 __

 __

 **Output :**

![pandas-iterate](https://media.geeksforgeeks.org/wp-
content/uploads/20200629200546/pandas-iterate-1.png)

Now let’s see different ways of iterate or certain columns of a DataFrame :

  

  

 **Method #1:** **UsingDataFrame.iteritems():**  
Dataframe class provides a member function iteritems() which gives an
iterator that can be utilized to iterate over all the columns of a data frame.
For every column in the Dataframe it returns an iterator to the tuple
containing the column name and its contents as series.

 **Code :**

 __

 __  
 __

 __

 __  
 __  
 __

import pandas as pd 

 

 

# List of Tuples

students = [('Ankit', 22, 'A'),

 ('Swapnil', 22, 'B'),

 ('Priya', 22, 'B'),

 ('Shivangi', 22, 'B'),

 ]

 

# Create a DataFrame object

stu_df = pd.DataFrame(students, columns =['Name', 'Age',
'Section'], 

 index =['1', '2', '3', '4'])

 

# gives a tuple of column name and series

# for each column in the dataframe

for (columnName, columnData) in stu_df.iteritems():

 print('Colunm Name : ', columnName)

 print('Column Contents : ', columnData.values)  
  
---  
  
 __

 __

 **Output:**  
![iterate over columns in dataframe-1](https://media.geeksforgeeks.org/wp-
content/uploads/20200628124555/Method11.png)

 **Method #2:** **Using [ ] operator :**  
We can iterate over column names and select our desired column.

 **Code :**

 __

 __  
 __

 __

 __  
 __  
 __

import pandas as pd 

 

 

# List of Tuples

students = [('Ankit', 22, 'A'),

 ('Swapnil', 22, 'B'),

 ('Priya', 22, 'B'),

 ('Shivangi', 22, 'B'),

 ]

 

# Create a DataFrame object

stu_df = pd.DataFrame(students, columns =['Name', 'Age',
'Section'],

 index =['1', '2', '3', '4'])

 

# Iterate over column names

for column in stu_df:

 

 # Select column contents by column

 # name using [] operator

 columnSeriesObj = stu_df[column]

 print('Colunm Name : ', column)

 print('Column Contents : ', columnSeriesObj.values)  
  
---  
  
 __

 __

 **Output:**  
![iterate over columns in dataframe-2](https://media.geeksforgeeks.org/wp-
content/uploads/20200628124557/Method21.png)

 **Method #3:** **Iterate over more than one column :**  
Assume we need to iterate more than one column. In order to do that we can
choose more than one column from dataframe and iterate over them.

 **Code :**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

import pandas as pd 

 

 

# List of Tuples

students = [('Ankit', 22, 'A'),

 ('Swapnil', 22, 'B'),

 ('Priya', 22, 'B'),

 ('Shivangi', 22, 'B'),

 ]

 

# Create a DataFrame object

stu_df = pd.DataFrame(students, columns =['Name', 'Age',
'Section'], 

 index =['1', '2', '3', '4'])

 

# Iterate over two given columns

# only from the dataframe

for column in stu_df[['Name', 'Section']]:

 

 # Select column contents by column 

 # name using [] operator

 columnSeriesObj = stu_df[column]

 print('Colunm Name : ', column)

 print('Column Contents : ', columnSeriesObj.values)  
  
---  
  
 __

 __

 **Output:**  
![iterate over columns in dataframe-3](https://media.geeksforgeeks.org/wp-
content/uploads/20200628124553/Method31.png)

 **Method #4:** **Iterating columns in reverse order :**  
We can iterate over columns in reverse order as well.

 **Code :**

 __

 __  
 __

 __

 __  
 __  
 __

import pandas as pd 

 

 

# List of Tuples

students = [('Ankit', 22, 'A'),

 ('Swapnil', 22, 'B'),

 ('Priya', 22, 'B'),

 ('Shivangi', 22, 'B'),

 ]

 

# Create a DataFrame object

stu_df = pd.DataFrame(students, columns =['Name', 'Age',
'Section'],

 index =['1', '2', '3', '4'])

 

 

# Iterate over the sequence of column names

# in reverse order

for column in reversed(stu_df.columns):

 

 # Select column contents by column

 # name using [] operator

 columnSeriesObj = stu_df[column]

 print('Colunm Name : ', column)

 print('Column Contents : ', columnSeriesObj.values)  
  
---  
  
 __

 __

 **Output:**  
![iterate over columns in dataframe-4](https://media.geeksforgeeks.org/wp-
content/uploads/20200628124559/Method41.png)

 **Method #5:** **Using index (iloc) :**  
To iterate over the columns of a Dataframe by index we can iterate over a
range i.e. 0 to Max number of columns than for each index we can select the
contents of the column using iloc[].

 **Code :**

 __

 __  
 __

 __

 __  
 __  
 __

import pandas as pd 

 

 

# List of Tuples

students = [('Ankit', 22, 'A'),

 ('Swapnil', 22, 'B'),

 ('Priya', 22, 'B'),

 ('Shivangi', 22, 'B'),

 ]

 

# Create a DataFrame object

stu_df = pd.DataFrame(students, columns =['Name', 'Age',
'Section'], 

 index =['1', '2', '3', '4'])

 

 

# Iterate over the index range from 

# 0 to max number of columns in dataframe

for index in range(stu_df.shape[1]):

 

 print('Column Number : ', index)

 

 # Select column by index position using iloc[]

 columnSeriesObj = stu_df.iloc[:, index]

 print('Column Contents : ', columnSeriesObj.values)  
  
---  
  
 __

 __

 **Output:**

![iterate over columns in dataframe-5](https://media.geeksforgeeks.org/wp-
content/uploads/20200628124601/Method5.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

