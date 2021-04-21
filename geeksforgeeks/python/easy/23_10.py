SQL using Python and SQLite | Set 2



Databases offer numerous functionalities by which one can manage large amounts
of information easily over the web, and high-volume data input and output over
a typical file such as a text file. SQL is a query language and is very
popular in databases. Many websites use MySQL. SQLite is a “light” version
that works over syntax very much similar to SQL.

SQLite is a self-contained, high-reliability, embedded, full-featured, public-
domain, SQL database engine. It is the most used database engine in the world
wide web.  
Python has a library to access SQLite databases, called sqlite3, intended for
working with this database which has been included with Python package since
version 2.5.

In this article we will discuss, how to query database using commands like
Update and Delete and also to visualize data via graphs.  
It is recommended to go through SQL using Python | Set 1

 **Updation and Deletion Operation**

 __

 __  
 __

 __

 __  
 __  
 __

# code for update operation

import sqlite3

 

# database name to be passed as parameter

conn = sqlite3.connect('mydatabase.db')

 

# update the student record

conn.execute("UPDATE Student SET name = 'Sam' where unix='B113059'")

conn.commit()

 

print "Total number of rows updated :", conn.total_changes

 

cursor = conn.execute("SELECT * FROM Student")

for row in cursor:

 print row,

 

conn.close()  
  
---  
  
 __

 __

Output:

  

  

    
    
    Total number of rows updated : 1
    (u'B113053', u'Geek', u'2017-01-11 13:53:39', 21.0), 
    (u'B113058', u'Saan', u'2017-01-11 13:53:39', 21.0), 
    (u'B113059', u'Sam', u'2017-01-11 13:53:39', 22.0)
    

__

__  
__

__

__  
__  
__

# code for delete operation

import sqlite3

 

# database name to be passed as parameter

conn = sqlite3.connect('mydatabase.db')

 

# delete student record from database

conn.execute("DELETE from Student where unix='B113058'")

conn.commit()

print "Total number of rows deleted :", conn.total_changes

 

cursor = conn.execute("SELECT * FROM Student")

for row in cursor:

 print row,

 

conn.close()  
  
---  
  
 __

 __

Output:

    
    
    Total number of rows deleted : 1
    (u'B113053', u'Geek', u'2017-01-11 13:53:39', 21.0),
     (u'B113059', u'Sam', u'2017-01-11 13:53:39', 22.0)
    

**Data input by User**

 __

 __  
 __

 __

 __  
 __  
 __

# code for executing query using input data

import sqlite3

 

# creates a database in RAM

con = sqlite3.connect(":memory:")

cur = con.cursor()

cur.execute("create table person (name, age, id)")

 

print ("Enter 5 students names:")

who = [raw_input() for i in range(5)]

print ("Enter their ages respectively:")

age = [int(raw_input()) for i in range(5)]

print ("Enter their ids respectively:")

p_id = [int(raw_input()) for i in range(5)]

n = len(who)

 

for i in range(n):

 

 # This is the q-mark style:

 cur.execute("insert into person values (?, ?, ?)", (who[i], age[i],
p_id[i]))

 

 # And this is the named style:

 cur.execute("select * from person")

 

 # Fetches all entries from table

 print cur.fetchall()  
  
---  
  
 __

 __

Output:

    
    
    (u'Navin', 34, 113053)
    (u'Basu', 42, 113058)
    (u'Firoz', 65, 113059)
    (u'Tim', 47, 113060)
    (u'Varun', 54, 113061)
    

**Graphing with SQLite**

 __

 __  
 __

 __

 __  
 __  
 __

# graph visualization using matplotlib library

import matplotlib.pyplot as plt

 

def graph_data(p_id,age):

 

 # plotting the points 

 plt.plot(p_id, age, color='yellow', linestyle='dashed',
linewidth = 3,

 marker='*', markerfacecolor='blue', markersize=12)

 

 # naming the x axis

 plt.xlabel('Persons Id')

 

 # naming the y axis

 plt.ylabel('Ages')

 

 # plt.plot(p_id,age)

 plt.show()

 

print ("Enter 5 students names:")

who = [raw_input() for i in range(5)]

print ("Enter their ages respectively:")

age = [int(raw_input()) for i in range(5)]

print ("Enter their ids respectively:")

p_id = [int(raw_input()) for i in range(5)]

 

# calling graph function

graph_data(p_id,age)  
  
---  
  
 __

 __

In this way we can perform such operations using SQL query to communicate with
Database and plot a Graph significantly to draw out its characteristic.

SQL using Python | Set 1  
SQL using Python | Set 3 (Handling large data)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

