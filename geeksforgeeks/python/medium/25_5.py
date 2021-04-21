MYSQLdb Connection in Python



In this article, I have discussed how to connect to MySQL database remotely
using python. For any application, it is very important to store the database
on a server for easy data access. It is quite complicated to connect to the
database remotely because every service provider doesn’t provide remote access
to the MySQL database. Here I am using python’s MySQLdb module for connecting
to our database which is at any server that provides remote access.  

**What is MYSQLdb?**

MySQLdb is an interface for connecting to a MySQL database server from Python.
It implements the Python Database API v2.0 and is built on top of the MySQL C
API.  
 **Packages to Install**  

    
    
    mysql-connector-python
    mysql-python

If using anaconda  

    
    
    conda install -c anaconda mysql-python
    conda install -c anaconda mysql-connector-python

else  

  

  

    
    
    pip install MySQL-python
    pip install MySQL-python-connector

 **Import-Package**  

    
    
    import MYSQLdb

**How to connect to** a **remote MySQL database using python?**

Before we start you should know the basics of SQL. Now let us discuss the
methods used in this code:

  * **connect():** This method is used for creating a connection to our database it has four arguments: 

  1. Server Name
  2. Database User Name
  3. Database Provider
  4. Database Name

  *  **cursor():** This method creates a cursor object that is capable of executing SQL queries on the database.
  *  **execute():** This method is used for executing SQL queries on the database. It takes a sql query( as string) as an argument.
  *  **fetchone():** This method retrieves the next row of a query result set and returns a single sequence, or None if no more rows are available.
  *  **close() :** This method close the database connection.  

**Free remote mysql database providers:**  
1.www.freemysqlhosting.net  
2.www.heliohost.org  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

'''This code would not be run on geeksforgeeks IDE

because required module

are not installed on IDE. Also this code requires

a remote MySQL databaseconnection with valid

Hostname, Dbusername Password and Dbname'''

# Module For Connecting To MySQL database

import MySQLdb

# Function for connecting to MySQL database

def mysqlconnect():

 #Trying to connect

 try:

 db_connection= MySQLdb.connect

 ("Hostname","dbusername","password","dbname")

 # If connection is not successful

 except:

 print("Can't connect to database")

 return 0

 # If Connection Is Successful

 print("Connected")

 # Making Cursor Object For Query Execution

 cursor=db_connection.cursor()

 # Executing Query

 cursor.execute("SELECT CURDATE();")

 # Above Query Gives Us The Current Date

 # Fetching Data

 m = cursor.fetchone()

 # Printing Result Of Above

 print("Today's Date Is ",m[0])

 # Closing Database Connection

 db_connection.close()

# Function Call For Connecting To Our Database

mysqlconnect()  
  
---  
  
 __

 __

    
    
    Connected
    Today's Date Is  2017-11-14

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to illustrate and create a

# table in database

import mysql.connector as mysql

# Open database connection

db =
mysql.connect(host="localhost",user="root",password="tiger",database="python")

cursor = db.cursor()

# Drop table if it already exist using execute()

cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# Create table as per requirement

sql = "CREATE TABLE EMPLOYEE ( FNAME CHAR(20) NOT NULL, LNAME CHAR(20),
AGE INT )"

cursor.execute(sql) #table created

# disconnect from server

db.close()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-content/uploads/20201221004430/1.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

