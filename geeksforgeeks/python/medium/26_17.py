MongoDB and Python



Prerequisite : MongoDB : An introduction  
MongoDB is a cross-platform, document-oriented database that works on the
concept of collections and documents. MongoDB offers high speed, high
availability, and high scalability.  
The next question which arises in the mind of the people is “Why MongoDB”?  
 **Reasons to opt for MongoDB :**

  1. It supports hierarchical data structure (Please refer docs for details)
  2. It supports associate arrays like Dictionaries in Python.
  3. Built-in Python drivers to connect python-application with Database. Example- PyMongo
  4. It is designed for Big Data.
  5. Deployment of MongoDB is very easy.

 **MongoDB vs RDBMS**

![](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/MongoDB_and_Python_1.png)

 **MongoDB and PyMongo Installation Guide**

  1. First start MongoDB from command prompt using :  
 **Method 1:**

  

  

    
    
    mongod

or  
 **Method 2:**

    
    
    net start MongoDB

![](https://media.geeksforgeeks.org/wp-content/uploads/rough6.png)  
See port number by default is set 27017 (last line in above image).  
Python has a native library for MongoDB. The name of the available library is
“PyMongo”. To import this, execute the following command:

 __

 __  
 __

 __

 __  
 __  
 __

from pymongo import MongoClient  
  
---  
  
 __

 __

*  **Create a connection :** The very first after importing the module is to create a MongoClient.

 __

 __  
 __

 __

 __  
 __  
 __

from pymongo import MongoClient

client = MongoClient()  
  
---  
  
 __

 __

After this, connect to the default host and port. Connection to the host and
port is done explicitly. The following command is used to connect the
MongoClient on the localhost which runs on port number 27017.

 __

 __  
 __

 __

 __  
 __  
 __

client= MongoClient(‘host’, port_number)

example:- client = MongoClient(‘localhost’, 27017)  
  
---  
  
 __

 __

It can also be done using the following command:

 __

 __  
 __

 __

 __  
 __  
 __

client= MongoClient(“mongodb://localhost:27017/”)  
  
---  
  
 __

 __

*  **Access DataBase Objects :** To create a database or switch to an existing database we use:  
 **Method 1 : Dictionary-style**

 __

 __  
 __

 __

 __  
 __  
 __

mydatabase= client[‘name_of_the_database’]  
  
---  
  
 __

 __

 **Method2 :**

 __

 __  
 __

 __

 __  
 __  
 __

mydatabase= client.name_of_the_database  
  
---  
  
 __

 __

If there is no previously created database with this name, MongoDB will
implicitly create one for the user.  
Note : The name of the database fill won’t tolerate any dash (-) used in it.
The names like my-Table will raise an error. So, underscore are permitted to
use in the name.

*  **Accessing the Collection :** Collections are equivalent to Tables in RDBMS. We access a collection in PyMongo in the same way as we access the Tables in the RDBMS. To access the table, say table name “myTable” of the database, say “mydatabase”.  
 **Method 1:**

 __

 __  
 __

 __

 __  
 __  
 __

mycollection= mydatabase[‘myTable’]  
  
---  
  
 __

 __

Method 2 :

  

  

 __

 __  
 __

 __

 __  
 __  
 __

mycollection= mydatabase.myTable  
  
---  
  
 __

 __

> MongoDB store the database in the form of dictionaries as shown:>
    
    
    record = {
    title: 'MongoDB and Python', 
    description: 'MongoDB is no SQL database', 
    tags: ['mongodb', 'database', 'NoSQL'], 
    viewers: 104 
    } 

‘_id’ is the special key which get automatically added if the programmer
forgets to add explicitly. _id is the 12 bytes hexadecimal number which
assures the uniqueness of every inserted document.  
![_id](https://media.geeksforgeeks.org/wp-
content/uploads/MongoDB_and_Python_2.png)

*  **Insert the data inside a collection :**  
Methods used:

    
    
    insert_one() or insert_many()

We normally use insert_one() method document into our collections. Say, we
wish to enter the data named as record into the ’myTable’ of ‘mydatabase’.

 __

 __  
 __

 __

 __  
 __  
 __

rec= myTable.insert_one(record)  
  
---  
  
 __

 __

The whole code looks likes this when needs to be implemented.

 __

 __  
 __

 __

 __  
 __  
 __

# importing module

from pymongo import MongoClient

 

# creation of MongoClient

client=MongoClient()

 

# Connect with the portnumber and host

client = MongoClient(“mongodb://localhost:27017/”)

 

# Access database

mydatabase = client[‘name_of_the_database’]

 

# Access collection of the database

mycollection=mydatabase[‘myTable’]

 

# dictionary to be added in the database

rec={

title: 'MongoDB and Python', 

description: 'MongoDB is no SQL database', 

tags: ['mongodb', 'database', 'NoSQL'], 

viewers: 104

}

 

# inserting the data in the database

rec = mydatabase.myTable.insert(record)  
  
---  
  
 __

 __

*  **Querying in MongoDB :** There are certain query functions which are used to filer the data in the database. The two most commonly used functions are:

  1. find()  
find() is used to get more than one single document as a result of query.

 __

 __  
 __

 __

 __  
 __  
 __

for i in mydatabase.myTable.find({title: 'MongoDB and Python'})

 print(i)  
  
---  
  
 __

 __

This will output all the documents in the myTable of mydatabase whose title is
‘MongoDB and Python’.

  2.  **count()**  
count() is used to get the numbers of documents with the name as passed int he
parameters.

 __

 __  
 __

 __

 __  
 __  
 __

print(mydatabase.myTable.count({title: 'MongoDB and Python'}))  
  
---  
  
 __

 __

This will output the numbers of documents in the myTable of mydatabase whose
title is ‘MongoDB and Python’.

These two query functions can be summed to give a give the most filtered
result as shown below.

 __

 __  
 __

 __

 __  
 __  
 __

print(mydatabase.myTable.find({title: 'MongoDB and Python'}).count())  
  
---  
  
 __

 __

  3.  **To print all the documents/entries inside ‘myTable’ of database ‘mydatabase’ :** Use the following code:

 __

 __  
 __

 __

 __  
 __  
 __

from pymongo import MongoClient

 

try:

 conn = MongoClient()

 print("Connected successfully!!!")

except: 

 print("Could not connect to MongoDB")

 

# database name: mydatabase

db = conn.mydatabase

 

# Created or Switched to collection names: myTable

collection = db.myTable

 

# To find() all the entries inside collection name 'myTable'

cursor = collection.find()

for record in cursor:

 print(record)  
  
---  
  
 __

 __

This article is contributed by **Rishabh Bansal and Shaurya Uppal**.

If you like GeeksforGeeks and would like to contribute, you can also write an
article using contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

![Try out the all-new GeeksforGeeks
Premium!](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210304125233/GFG-Go-Premium.png)

My Personal Notes _arrow_drop_up_

Save

