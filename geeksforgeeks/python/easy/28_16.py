SQL using Python | Set 1



In this article, database connection with the python program is discussed.
Connecting a program with a database is considered a tough task in any
programming language. It is used to connect the front-end of your application
with the back-end database. Python with its native builtin modules made this
thing easy too.  
This needs the basic understanding of SQL.

Here, we are going to connect SQLite with Python. Python has a native library
for SQLite. Let us explain how it works.

  1. To use SQLite, we must import sqlite3.
  2. Then create a connection using connect() method and pass the name of the database you want to access if there is a file with that name, it will open that file. Otherwise, Python will create a file with the given name.
  3. After this, a cursor object is called to be capable to send commands to the SQL. Cursor is a control structure used to traverse and fetch the records of the database. Cursor has a major role in working with Python. All the commands will be executed using cursor object only.
  4. To create a table in the database, create an object and write the SQL command in it with being commented. Example:- sql_comm = ”SQL statement”
  5. And executing the command is very easy. Call the cursor method execute and pass the name of the sql command as a parameter in it. Save a number of commands as the sql_comm and execute them. After you perform all your activities, save the changes in the file by committing those changes and then lose the connection.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate table creation and

# insertions with SQL

 

# importing module

import sqlite3

 

# connecting to the database 

connection = sqlite3.connect("myTable.db")

 

# cursor 

crsr = connection.cursor()

 

# SQL command to create a table in the database

sql_command = """CREATE TABLE emp ( 

staff_number INTEGER PRIMARY KEY, 

fname VARCHAR(20), 

lname VARCHAR(30), 

gender CHAR(1), 

joining DATE);"""

 

# execute the statement

crsr.execute(sql_command)

 

# SQL command to insert the data in the table

sql_command = """INSERT INTO emp VALUES (23, "Rishabh", "Bansal", "M",
"2014-03-28");"""

crsr.execute(sql_command)

 

# another SQL command to insert the data in the table

sql_command = """INSERT INTO emp VALUES (1, "Bill", "Gates", "M",
"1980-10-28");"""

crsr.execute(sql_command)

 

# To save the changes in the files. Never skip this. 

# If we skip this, nothing will be saved in the database.

connection.commit()

 

# close the connection

connection.close()  
  
---  
  
 __

 __

In this section, we have discussed how to create a table and how to add new
rows in the database.

 **Fetching the data** from record is simple as the inserting them. The
execute method uses the SQL command of getting all the data from the table
using “Select * from table_name” and all the table data can be fetched in an
object in the form of list of lists.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate SQL to fetch data.

 

# importing the module

import sqlite3

 

# connect withe the myTable database

connection = sqlite3.connect("myTable.db")

 

# cursor object

crsr = connection.cursor()

 

# execute the command to fetch all the data from the table emp

crsr.execute("SELECT * FROM emp") 

 

# store all the fetched data in the ans variable

ans = crsr.fetchall() 

 

# Since we have already selected all the data entries 

# using the "SELECT *" SQL command and stored them in 

# the ans variable, all we need to do now is to print 

# out the ans variable

print(ans)  
  
---  
  
 __

 __

It should be noted that the database file that will be created will be in the
same folder as that of the python file. If we wish to change the path of the
file, change the path while opening the file.

  

  

SQL using Python and SQLite | Set 2  
SQL using Python | Set 3 (Handling large data)

This article is contributed by **Rishabh Bansal**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

