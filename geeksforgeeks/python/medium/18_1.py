Oracle Database Connection in Python



Sometimes as the part of programming, we required to work with the databases
because we want to store huge amount of information so we use databases, such
as Oracle, MySQL etc. So In this article, we will discuss the connectivity of
Oracle database with Python. This can be done through the module name
**cx_Oracle**.

 **Oracle Database**  
For communicating any database with our Python program, then we required some
connector which is nothing but the _cx_Oracle_ module.

 **For installing cx_Oracle :**

    
    
    pip install cx_Oracle

By this command, you can install cx_Oracle package but it is required to
install Oracle database first in your PC.

 **How to use this module for connection**

  

  

  *  **Import database specific module**  
Ex. import cx_Oracle

  *  **connect():** Now Establish a connection between Python program and Oracle database by using connect() function.
    
        con = cx_Oracle.connect('username/password@localhost')

  *  **cursor():** To execute sql query and to provide result some special object required is nothing but cursor() object
    
        cursor = cx_Oracle.cursor()

  *  **execute method :**  

> cursor.execute(sqlquery) – – – -> to execute single query.  
> cursor.execute(sqlqueries) – – – -> to execute a group of multiple sqlquery
> seperated by “;”

  *  **commit():** For DML(Data Manuplate Language) query in this query you have (update, insert, delete) operation we need to commit() then only the result reflecte in database.
  *  **Fetch():** This retrieves the next row of a query result set and returns a single sequence, or None if no more rows are available.
  *  **close():** After all done mendentory to close all operation
    
        cursor.close()
    con.close()
    

**Creting table:**

 __

 __  
 __

 __

 __  
 __  
 __

# importing module

import cx_Oracle 

 

 

# Create a table in Oracle database

try:

 

 con = cx_Oracle.connect('scott/tiger@localhost')

 

 # Now execute the sqlquery

 cursor = con.cursor()

 

 # Creating a table srollno heading which is number

 cursor.execute("create table student(srollno number, \

 name varchar2(10), efees number(10, 2)")

 

 print("Table Created successful")

 

except cx_Oracle.DatabaseError as e:

 print("There is a problem with Oracle", e)

 

# by writing finally if any error occurs

# then also we can close the all database operation

finally:

 if cursor:

 cursor.close()

 if con:

 con.close()  
  
---  
  
 __

 __

 **Output:**

    
    
    Table Created successful

  
**Inserting into table:**

 __

 __  
 __

 __

 __  
 __  
 __

# Program to create a table in Oracle database

import cx_Oracle

 

try:

 

 con = cx_Oracle.connect('scott/tiger@localhost')

 

 # Now execute the sqlquery

 cursor = con.cursor()

 cursor.execute("insert into student values(19585, Niranjan Shukla,
72000")

 

 # commit that insert the provided data

 con.commit()

 

 print("value inserted successful")

 

except cx_Oracle.DatabaseError as e:

 print("There is a problem with Oracle", e)

 

# by writing finally if any error occurs

# then also we can close the all database operation

finally:

 if cursor:

 cursor.close()

 if con:

 con.close()  
  
---  
  
 __

 __

 **Output:**

    
    
    value inserted successful

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

