Python MySQL – Create Database



Python Database API ( Application Program Interface ) is the Database
interface for the standard Python. This standard is adhered to by most Python
Database interfaces. There are various Database servers supported by Python
Database such as MySQL, GadFly, mSQL, PostgreSQL, Microsoft SQL Server 2000,
Informix, Interbase, Oracle, Sybase etc. To connect with MySQL database server
from Python, we need to import the mysql.connector interface.  
 **Syntax:**  

    
    
    CREATE DATABASE DATABASE_NAME
    
    

**Example:**  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# importing rquired libraries

import mysql.connector

dataBase = mysql.connector.connect(

 host ="localhost",

 user ="user",

 passwd ="gfg"

)

# preparing a cursor object

cursorObject = dataBase.cursor()

# creating database

cursorObject.execute("CREATE DATABASE geeks4geeks")  
  
---  
  
 __

 __

 **Output:**  

![python-mysql-create-db](https://media.geeksforgeeks.org/wp-
content/uploads/20200304161950/python-mysql-create-db.png)

  

  

The above program illustrates the creation of MySQL database geeks4geeks in
which host-name is localhost, the username is user and password is gfg.  
Let’s suppose we want to create a table in the database, then we need to
connect to a database. Below is a program to create a table in the geeks4geeks
database which was created in the above program.  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# importing required library

import mysql.connector

# connecting to the database

dataBase = mysql.connector.connect(

 host = "localhost",

 user = "user",

 passwd = "gfg",

 database = "geeks4geeks" ) 

# preparing a cursor object

cursorObject = dataBase.cursor()

# creating table 

studentRecord = """CREATE TABLE STUDENT (

 NAME VARCHAR(20) NOT NULL,

 BRANCH VARCHAR(50),

 ROLL INT NOT NULL,

 SECTION VARCHAR(5),

 AGE INT

 )"""

# table created

cursorObject.execute(studentRecord) 

# disconnecting from server

dataBase.close()  
  
---  
  
 __

 __

 **Output:**  

![PYTHON-MYSQL-CREATE-DB1](https://media.geeksforgeeks.org/wp-
content/uploads/20200304162535/PYTHON-MYSQL-CREATE-DB1.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

