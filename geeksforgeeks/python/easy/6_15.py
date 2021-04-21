Create a database in MongoDB using Python



 **MongoDB** is a general-purpose, document-based, distributed database built
for modern application developers and the cloud. It is a document database,
which means it stores data in JSON-like documents. This is an efficient way to
think about data and is more expressive and powerful than the traditional
table model.

MongoDB has no separate command to create a database. Instead, it uses the use
command to create a database. The use command is used to switch to the
specific database. If the database name specified after the use keyword does
not exist, then a new database is created with the specified name.

## Creating a database using Python in MongoDB

To use Python in MongoDB, we are going to import PyMongo. From that,
MongoClient can be imported which is used to create a client to the database.
Using the client, a new database can be created.

 **Example:**

 **List of databases using MongoDB shell (before):**

  

  

![python-create-database-mongodb1](https://media.geeksforgeeks.org/wp-
content/uploads/20200506191746/python-create-database-mongodb1.png)

 __

 __  
 __

 __

 __  
 __  
 __

# import MongoClient

from pymongo import MongoClient

 

 

# Creating a client

client = MongoClient('localhost', 27017)

 

# Greating a database name GFG

db = client['GFG']

print("Database is created !!")  
  
---  
  
 __

 __

 **Output:**

    
    
    Database is created!!
    

In the above example, it is clearly shown how a database is created. When
creating a client, the local host along with its port number, which is 27017
here, is passed to the MongoClient. Then, by using the client, a new database
named ‘GFG’ is created.

We can check if the database is present in the list of databases using the
following code:

 __

 __  
 __

 __

 __  
 __  
 __

list_of_db= client.list_database_names()

 

if "mydbase" in list_of_db:

 print("Exists !!")  
  
---  
  
 __

 __

 **Output:**

    
    
    Exists!!
    

**List of Databases in MongoDB shell (after):**

![python-mongodvb-create-database-2](https://media.geeksforgeeks.org/wp-
content/uploads/20200506192100/python-mongodvb-create-database-2.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

