Convert CSV to HTML Table in Python



CSV file is a Comma Separated Value file that uses a comma to separate values.
It is basically used for exchanging data between different applications. In
this, individual rows are separated by a newline. Fields of data in each row
are delimited with a comma.

 **Example :**

    
    
    Name, Salary, Age, No.of years employed
    Akriti, 90000, 20, 1
    Shreya, 100000, 21, 2
    Priyanka, 25000, 45, 7
    Neha, 46000, 25, 4
    

**Note:** For more information, refer to Working with csv files in Python

#### Converting CSV to HTML Table in Python

 **Method 1 Using pandas:** One of the easiest way to convert CSV file to HTML
table is using pandas. Type the below code in the command prompt to install
pandas.

    
    
    pip install pandas 

**Example:** Suppose the CSV file looks like this –

  

  

![csv-to-html](https://media.geeksforgeeks.org/wp-
content/uploads/20200131185718/csv-to-html.png)

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to convert

# CSV to HTML Table

 

 

import pandas as pd

 

# to read csv file named "samplee"

a = pd.read_csv("read_file.csv")

 

# to save as html file

# named as "Table"

a.to_html("Table.htm")

 

# assign it to a 

# variable (string)

html_file = a.to_html()  
  
---  
  
 __

 __

 **Output:**

![csv-to-html](https://media.geeksforgeeks.org/wp-
content/uploads/20200131190002/csv-to-html-1.png)

 **Method 2 Using PrettyTable:** PrettyTable is a simple Python library
designed to make it quick and easy to represent tabular data in visually
appealing ASCII tables. Type the below command to install this module.

    
    
    pip install PrettyTable
    

**Example:** The above CSV file is used.

 __

 __  
 __

 __

 __  
 __  
 __

from prettytable import PrettyTable

 

 

# open csv file

a = open("read_file.csv", 'r')

 

# read the csv file

a = a.readlines()

 

# Seperating the Headers

l1 = a[0]

l1 = l1.split(',')

 

# headers for table

t = PrettyTable([l1[0], l1[1]])

 

# Adding the data

for i in range(1, len(a)) :

 t.add_row(a[i].split(','))

 

code = t.get_html_string()

html_file = open('Tablee.html', 'w')

html_file = html_file.write(code)  
  
---  
  
 __

 __

 **Output :**

![python-csv-to-html](https://media.geeksforgeeks.org/wp-
content/uploads/20200131191017/python-csv-to-html-2.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

