Python MySQL – Where Clause



 **Where clause** is used in MySQL database to filter the data as per the
condition required. You can fetch, delete or update a particular set of data
in MySQL database by using where clause.

 **Syntax**

> SELECT column1, column2, …. cloumnN FROM [TABLE NAME] WHERE [CONDITION];

The above syntax is used for displaying a certain set of data following the
condition.

 **Example:** Consider the following database named college and having a table
name as a student.

  

  

 **Schema of the database:**

![python-db-schema](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20200227134245/python-db-schema.png)  
  
**Database:**

![python-db-table](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20200227134341/python-db-table.png)  

### Where Clause In Python

Steps to use where clause in Python is:

  1. First form a connection between MySQL and Python program. It is done by importing mysql.connector package and using mysql.connector.connect() method, for passing the user name, password, host (optional default: localhost) and, database (optional) as parameters to it.
  2. Now, create a cursor object on the connection object created above by using cursor() method. A database cursor is a control structure that enables traversal over the records in a database.
  3. Then, execute the where clause statement by passing it through execute() method.

 __

 __  
 __

 __

 __  
 __  
 __

import mysql.connector

 

#Establishing connection

conn = mysql.connector.connect(user='your_username',

 host='localhost',

 password ='your_password',

 database='College')

 

# Creating a cursor object using 

# the cursor() method

mycursor = conn.cursor();

 

# SQL Query

sql = "select * from Student where Roll_no >= 3;"

 

# Executing query

mycursor.execute(sql)

 

myresult = mycursor.fetchall()

 

for x in myresult:

 print(x)

 

# Closing the connection

conn.close()  
  
---  
  
 __

 __

 **OUTPUT:**

![python-where-mysql](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20200227134524/python-where-mysql.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

