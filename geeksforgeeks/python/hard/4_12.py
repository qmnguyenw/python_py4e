Nested Queries in PyMongo



 **MongoDB** is a NoSQL document-oriented database. It does not give much
importance for relations or can also be said as it is schema-free.

PyMongo is a Python module that can be used to interact between the mongo
database and Python applications. The data that is exchanged between the
Python application and the mongo database is in Binary JSON format.

## Nested Queries in PyMongo

To fetch a particular record from the MongoDB document, querying plays an
important role. Getting the right data as soon as possible to make the right
decision is necessary. Here are some of the multiple query request techniques.

### Query operators in PyMongo

To use $and, $or and $not MongoDB operators, the outer dictionary key
must be one of the query operators; and dictionary parameters must be in a
Python list and that Python list must be the value of the key.

 **Syntax :**

  

  

    
    
    query = { 
              '$and' : [
                   { operand_query_1},
                   { operand_query_2} 
                       ]
             }

 **Example 1 :** Create a collection called lecturers and retrieve using
find().

 __

 __  
 __

 __

 __  
 __  
 __

import pprint

from pymongo import MongoClient

 

 

client = MongoClient()

 

Database = client["GFG"]

lecturers = Database["lecture"]

 

lecturers.insert_many([

 {"l_id":56, "d_id":1, "salary":50000},

 {"l_id":57, "d_id":3, "salary":40000},

 {"l_id":58, "d_id":4, "salary":90000},

 {"l_id":59, "d_id":2, "salary":50000},

 {"l_id":52, "d_id":1, "salary":70000},

 {"l_id":53, "d_id":5, "salary":30000}

])

 

# retrieving the documents

for x in lecturers.find():

 pprint.pprint(x)  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200601215043/2020-06-01-6.png)

 **Query 1 :** Display the lecturer records with salary less than 50000 and
arrange in ascending order.

 __

 __  
 __

 __

 __  
 __  
 __

# lecturer records with salary less

# than 50000 and arrange in ascending order.

pprint.pprint(list(lecturers.find({"salary":

 {'$lt':50000}}).sort('salary', 1)))  
  
---  
  
 __

 __

 **Output :**

![](https://media.geeksforgeeks.org/wp-content/uploads/20200601220350/1a6.png)

 **Query 2 :** Display lecturer records with salary greater than 40000 in
department_id 1 and sort according to their salary in descending order.

 __

 __  
 __

 __

 __  
 __  
 __

# lecturer records with salary greater than 40000

# in department_id 1 and sort according to their 

# salary in descending order.

pprint.pprint(list(lecturers.find({'$and':

 [{"d_id":1},

 {"salary":

 {'$gte':50000}}]}).sort("salary", -1)))  
  
---  
  
 __

 __

 **Output :**

![](https://media.geeksforgeeks.org/wp-content/uploads/20200601220436/1b4.png)

  

  

 **Example 2 :** Create a collection called books and retrieve using find().

 __

 __  
 __

 __

 __  
 __  
 __

import pprint

from pymongo import MongoClient

import datetime

 

 

client = MongoClient()

Database = client["GFG"]

books = Database["book"]

 

books.insert_many([

 {"author":"Samsuel", "book_id":54, "ratings":3,

 "publish":datetime.datetime(1999, 12, 6)},

 

 {"author":"Thomson", "book_id":84, "ratings":4,

 "publish":datetime.datetime(1996, 7, 12)},

 

 {"author":"Piyush Agarwal", "book_id":34,
"ratings":1,

 "publish":datetime.datetime(2000, 9, 6)},

 

 {"author":"Shreya Mathur", "book_id":12,
"ratings":2, 

 "publish":datetime.datetime(2017, 8, 8)},

 

 {"author":"Antony Sharma", "book_id":98,
"ratings":4, 

 "publish":datetime.datetime(2003, 11, 5)},

])

 

# retrieving the documents

for x in books.find():

 pprint.pprint(x)  
  
---  
  
 __

 __

 **Output :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200601215606/2020-06-01-7.png)

 **Query 1 :** Display the record of books with ratings greater than 3
published after 2000.

 __

 __  
 __

 __

 __  
 __  
 __

# books with ratings greater than 3 published after 2000

pprint.pprint(list(books.find({'$and':

 [{"ratings":

 {'$gt':3}},

 {"publish":

 {'$gt':datetime.datetime(2000, 12, 31)

 }

 }

 ]

 }

 )

 )

 )  
  
---  
  
 __

 __

 **Output :**

![](https://media.geeksforgeeks.org/wp-content/uploads/20200601220732/2a2.png)

 **Query 2 :** Display the record of the books with ratings greater than 1 and
published between the year 1999 and 2016, sort in decreasing order.

 __

 __  
 __

 __

 __  
 __  
 __

# between 1999-2016

query ={'$and':

 [{"publish":

 {'$gte':datetime.datetime(1999, 1, 1)}}, 

 {"publish":

 {'$lte':datetime.datetime(2016, 12, 31)}}]}

 

# books with ratings greater than 1

# and published between the year 

# 1999-2016, sort in decreasing order.

pprint.pprint(list(books.find({'$and':

 [{"ratings":

 {'$gt':1}},

 query]}).sort("publish", -1)))  
  
---  
  
 __

 __

 **Output :**

![](https://media.geeksforgeeks.org/wp-content/uploads/20200601220900/2b3.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

