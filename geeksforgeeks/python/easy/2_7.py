Update column value of CSV in Python



 **Prerequisites:** Pandas

In this article, we will discuss ways in which the value(s) of a column can be
updated. The best and the optimal way to update any column value of a CSV is
to use the Pandas Library and the DataFrame functions.

Link for the CSV file in use – Click here

###  **Method 1**

 **Approach**

  * Import module
  * Open CSV file and read its data
  * Find column to be updated
  * Update value in the CSV file using to_csv() function

to_csv() **** method converts the Data Frame into CSV data as the output is
returned to the file, it takes the file object or the file name as the
parameter and the **index=False** should be mentioned so that the indices are
not written into the CSV file. But this method is very tedious and is not
reliable when you want to update similar values that are occurring multiple
times.

  

  

**Details in the file before updating:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201216110022/BeforeOutput1-660x266.JPG)

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing the pandas library

import pandas as pd

 

# reading the csv file

df = pd.read_csv("AllDetails.csv")

 

# updating the column value/data

df.loc[5, 'Name'] = 'SHIV CHANDRA'

 

# writing into the file

df.to_csv("AllDetails.csv", index=False)

 

print(df)  
  
---  
  
 __

 __

 **Details after updating:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201216110328/AfterOutput1-660x276.JPG)

###  **Method 2:**

 **Approach**

  * Import module
  * Open csv file and read its data
  * Find column to be updated
  * Update value in the csv file using replace() function

The replace() method is useful when we have to update the data that is
occurring multiple number of time. We simply just have to specify the column
name and need to pass the values as a dictionary into the replace() method
which is in the form of key and value pair, the key will have the previous
data of the column and value will have the data to be updated with.

  

  

**Before updating column data/value:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201216110328/AfterOutput1-660x276.JPG)

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing the pandas library

import pandas as pd

 

# reading the csv file

df = pd.read_csv("AllDetails.csv")

 

# updating the column value/data

df['Status'] = df['Status'].replace({'P': 'A'})

 

# writing into the file

df.to_csv("AllDetails.csv", index=False)

 

print(df)  
  
---  
  
 __

 __

 **After updating column data/value:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201216111623/AfterOutput2-660x256.JPG)

### Method 3:

In this method, we are employing csv module which is a dedicated module
centrally created for reading, writing and updating csv files.

Approach:

  * Import module
  * Read data as dictionary
  * Update the required column values storing it as a list of dictionary
  * Inserting it back, row by row
  * Closing the file.

 **File before update:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201216111623/AfterOutput2-660x256.JPG)

 **Program:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import csv

 

op = open("AllDetails.csv", "r")

dt = csv.DictReader(op)

print(dt)

up_dt = []

for r in dt:

 print(r)

 row = {'Sno': r['Sno'],

 'Registration Number': r['Registration Number'],

 'Name': r['Name'],

 'RollNo': r['RollNo'],

 'Status': 'P'}

 up_dt.append(row)

print(up_dt)

op.close()

op = open("AllDetails.csv", "w", newline='')

headers = ['Sno', 'Registration Number', 'Name',
'RollNo', 'Status']

data = csv.DictWriter(op, delimiter=',', fieldnames=headers)

data.writerow(dict((heads, heads) for heads in headers))

data.writerows(up_dt)

 

op.close()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201219230255/Screenshot310.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

