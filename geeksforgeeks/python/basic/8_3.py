Connect MySQL database using MySQL-Connector Python



While working with Python we need to work with databases, they may be of
different types like MySQL, SQLite, NoSQL, etc. In this article, we will be
looking forward to how to connect MySQL databases using MySQL
Connector/Python.

MySQL Connector module of Python is used to connect MySQL databases with the
Python programs, it does that using the Python Database API Specification v2.0
(PEP 249). It uses the Python standard library and has no dependencies.

## Connecting to the Database

In the following example we will be connecting to MySQL database using
connect()

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to connect

# to mysql databse

 

 

import mysql.connector

 

 

# Connecting from the server

conn = mysql.connector.connect(user = 'username',

 host = 'localhost',

 database = 'databse_name')

 

print(conn)

 

# Disconnecting from the server

conn.close()  
  
---  
  
 __

 __

 **Output:**

  

  

![python-mysql-connect-1](https://media.geeksforgeeks.org/wp-
content/uploads/20200304152526/python-mysql-connect-1.png)

Also for the same, we can use connection.MySQLConnection() class instead of
connect():

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to connect

# to mysql databse

 

 

from mysql.connector import connection

 

# Connecting to the server

conn = connection.MySQLConnection(user = 'username', 

 host = 'localhost',

 database = 'database_name')

 

print(conn)

 

# Disconnecting from the server

conn.close()  
  
---  
  
 __

 __

 **Output:**

![python-mysql-connect-2](https://media.geeksforgeeks.org/wp-
content/uploads/20200304152800/python-mysql-connect-2.png)

Another way is to pass the dictionary in the connect() function using ‘**’
operator:

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to connect

# to mysql databse

 

 

from mysql.connector import connection

 

 

dict = {

 'user': 'root',

 'host': 'localhost',

 'database': 'College'

}

 

# Connecting to the server

conn = connection.MySQLConnection(**dict)

 

print(conn)

 

# Disconnecting from the server

conn.close()  
  
---  
  
 __

 __

 **Output:**

![python-mysql-connect-3](https://media.geeksforgeeks.org/wp-
content/uploads/20200304153027/python-mysql-connect-3.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

