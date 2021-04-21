MongoDB Python | Insert and Update Data



 **Prerequisites :** MongoDB Python Basics  
We would first understand how to insert a document/entry in a collection of a
database. Then we would work on how to update an existing document in MongoDB
using pymongo library in python. The update commands helps us to update the
query data inserted already in MongoDB database collection.

 **Insert data**

We would first insert data in MongoDB.

  *  **Step 1 – Establishing Connection** : Port number Default: 27017
    
        conn = MongoClient(‘localhost’, port-number)

If using default port-number i.e. 27017. Alternate connection method:

    
        conn = MongoClient()

  *  **Step 2 – Create Database or Switch to Existing Database:**
    
        db = conn.dabasename

Create a collection or Switch to existing collection:

  

  

    
        collection = db.collection_name

  *  **Step 3 – Insert :** To Insert Data create a dictionary object and insert data in database. Method used to insert data:
    
         insert_one() or insert_many()

After insert to find the documents inside a collection we use find() command.
The find() method issues a query to retrieve data from a collection in
MongoDB. All queries in MongoDB have the scope of a single collection.  
Note : ObjectId is different for every entry in database collection.  
Let us understand insert of data with help on code:-

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to illustrate

# inserting data in MongoDB

from pymongo import MongoClient

 

try:

 conn = MongoClient()

 print("Connected successfully!!!")

except: 

 print("Could not connect to MongoDB")

 

# database

db = conn.database

 

# Created or Switched to collection names: my_gfg_collection

collection = db.my_gfg_collection

 

emp_rec1 = {

 "name":"Mr.Geek",

 "eid":24,

 "location":"delhi"

 }

emp_rec2 = {

 "name":"Mr.Shaurya",

 "eid":14,

 "location":"delhi"

 }

 

# Insert Data

rec_id1 = collection.insert_one(emp_rec1)

rec_id2 = collection.insert_one(emp_rec2)

 

print("Data inserted with record ids",rec_id1," ",rec_id2)

 

# Printing the data inserted

cursor = collection.find()

for record in cursor:

 print(record)  
  
---  
  
 __

 __

Output:

    
    
    Connected successfully!!!
    Data inserted with record ids    
    {'_id': ObjectId('5a02227b37b8552becf5ed2a'), 
    'name': 'Mr.Geek', 'eid': 24, 'location': 'delhi'}
    {'_id': ObjectId('5a02227c37b8552becf5ed2b'), 'name':
    'Mr.Shaurya', 'eid': 14, 'location': 'delhi'}
    

**Updating data in MongoD** B

 **Methods used: update_one() and update_many()**  
 **Parameters passed:**  
\+ a filter document to match the documents to update  
\+ an update document to specify the modification to perform  
\+ an optional upsert parameter

After inserting Data in MongoDB let’s Update the Data of employee with id:24

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to illustrate

# updating data in MongoDB

# with Data of employee with id:24

from pymongo import MongoClient

 

try:

 conn = MongoClient()

 print("Connected successfully!!!")

except: 

 print("Could not connect to MongoDB")

 

# database

db = conn.database

 

# Created or Switched to collection names: my_gfg_collection

collection = db.my_gfg_collection

 

# update all the employee data whose eid is 24

result = collection.update_many(

 {"eid":24},

 {

 "$set":{

 "name":"Mr.Geeksforgeeks"

 },

 "$currentDate":{"lastModified":True}

 

 }

 )

 

 

 

print("Data updated with id",result)

 

# Print the new record

cursor = collection.find()

for record in cursor:

 print(record)  
  
---  
  
 __

 __

Output:

    
    
    Connected successfully!!!
    Data updated with id 
    {'_id': ObjectId('5a02227b37b8552becf5ed2a'), 
    'name': 'Mr.Geeksforgeeks', 'eid': 24, 'location': 
    'delhi', 'lastModified': datetime.datetime(2017, 11, 7, 21, 19, 9, 698000)}
    {'_id': ObjectId('5a02227c37b8552becf5ed2b'), 'name': 
    'Mr.Shaurya', 'eid': 14, 'location': 'delhi'}
    

To find number of documents or entries in collection the are updated use.

    
    
     print(result.matched_count) 

Here output would be 1.

![Try out the all-new GeeksforGeeks
Premium!](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210304125233/GFG-Go-Premium.png)

My Personal Notes _arrow_drop_up_

Save

