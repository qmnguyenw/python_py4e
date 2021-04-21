Sorting a CSV object by dates in Python



CSV stands for comma-separated values. A CSV file can be opened in Google
Sheets or Excel and will be formatted as a spreadsheet. However, a CSV file is
actually a plain-text file. It can also be opened with a text editor program
such as Atom. In this article, we are going to see how to sort a CSV object by
dates in Python

CSVs give us a good, simple way to organize data without using a database
program. It’s easy to read from and write to CSV files with Python.

## Steps to Read a CSV file

 **Step 1:** In the first step to read a CSV you need to find the file.

 **Step 2:** Import pandas library

The pandas library is exported by using import keyword and object as pd which
is a standard notation for pandas library.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import pandas as pd  
  
---  
  
 __

 __

 **Step 3:** Read the CSV file by using pandas library and assign it to a
variable.

The csv file ‘data.csv’ is loaded by using read_csv method present in the
pandas library and stored in the variable named ‘data’ and now this variable
is called a dataframe.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

data= pd.read_csv('data.csv')  
  
---  
  
 __

 __

 **Step 4:** Display the first 5 rows of the data by using head function.

The ‘.head()’ method is used to print the first 5 rows and ‘.tail()’ method is
used to print the last 5 rows of the data file.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

display(data.head())  
  
---  
  
 __

 __

 **Output:**

  

  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210220182017/Capture-660x253.PNG)

output screenshot

## Steps to sort the Data by Dates

 **Step 1:** Convert the Date column into required date time format

You can use the parameter infer_datetime_format. Example with your sample data
below:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

data['date'] = pd.to_datetime(data.date, infer_datetime_format =
True)

display(data.head())  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210220181053/Capture-660x245.PNG)

output screenshot

 **Step 2:** Use the sort_values method and giving parameter as date we sort
the values by date. To get the sorted while use head function to get first 5
rows of dataInput:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

data.sort_values(by= 'date', ascending = True, inplace =
True)

display(data.head())  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210221230355/Capture-660x301.PNG)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

