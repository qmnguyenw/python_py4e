MongoDB Python – Insert and Replace Operations



 **Prerequisites :**MongoDB Python Basics  
This article focus on how to replace document or entry inside a collection. We
can only replace the data already inserted in the database.  
 **Method used :** replace_one() and replace_many()  
Aim: Replace entire data of old document with new document

 **Insertion In MongoDB**

We would first insert data in MongoDB.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to illustrate

# Insert in MongoDB

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

emp_rec3 = {

 "name":"Mr.Coder",

 "eid":14,

 "location":"gurugram"

 } 

 

# Insert Data

rec_id1 = collection.insert_one(emp_rec1)

rec_id2 = collection.insert_one(emp_rec2)

rec_id3 = collection.insert_one(emp_rec3)

print("Data inserted with record ids",rec_id1," ",rec_id2,rec_id3)

 

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
    {'_id': ObjectId('5a02227b37b8552becf5ed2a'), 'name': 
    'Mr.Geek', 'eid': 24, 'location': 'delhi'}
    {'_id': ObjectId('5a02227c37b8552becf5ed2b'), 'name': 
    'Mr.Shaurya', 'eid': 14, 'location': 'delhi'}
    {'_id': ObjectId('5a02227c37b8552becf5ed2c'), 'name': 
    'Mr.Coder', 'eid': 14, 'location': 'gurugram'}
    

**Replace_one()**

  

  

After inserting the data let’s replace the Data of employee whose name :
Mr.Shaurya

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to illustrate

# Replace_one() in MongoDB

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

 

# replace one of the employee data whose name is Mr.Shaurya

result = collection.replace_one(

 {"name":"Mr.Shaurya"},

 {

 "name":"Mr.GfG",

 "eid":45,

 "location":"noida"

 

 }

 )

 

print("Data replaced with id",result)

 

# Print the new record

cursor = collection.find()

for record in cursor:

 print(record)  
  
---  
  
 __

 __

    
    
    Connected successfully!!!
    Data replaced with id 
    {'_id': ObjectId('5a02227b37b8552becf5ed2a'), 'name': 
    'Mr.Geek', 'eid': 24, 'location': 'delhi'}
    {'_id': ObjectId('5a02227c37b8552becf5ed2b'), 'name': 
    'Mr.GfG', 'eid': 45, 'location': 'noida'}
    {'_id': ObjectId('5a02227c37b8552becf5ed2c'), 'name': 
    'Mr.Coder', 'eid': 14, 'location': 'gurugram'}

We have successfully replaced the document of employee name:’Mr.Shaurya’ and
replaced the entire document with new one, name:’Mr.GfG’ (present).

 **Replace_many()**

 _Considering the data is same as inserted._  
Replace all the data entries with eid:14.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to illustrate

# Replace_many() in MongoDB

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

 

# replace one of the employee data whose name is Mr.Shaurya

result = collection.replace_many(

 {"eid":14},

 {

 "name":"Mr.GfG",

 "eid":45,

 "location":"noida"

 

 }

 )

 

print("Data replaced with id",result)

 

# Print the new record

cursor = collection.find()

for record in cursor:

 print(record)  
  
---  
  
 __

 __

Output would have been:

    
    
    Connected successfully!!!
    Data replaced with id 
    {'_id': ObjectId('5a02227b37b8552becf5ed2a'), 'name': 
    'Mr.Geek', 'eid': 24, 'location': 'delhi'}
    {'_id': ObjectId('5a02227c37b8552becf5ed2b'), 'name': 
    'Mr.GfG', 'eid': 45, 'location': 'noida'}
    {'_id': ObjectId('5a02227c37b8552becf5ed2c'), 'name': 
    'Mr.GfG', 'eid': 45, 'location': 'noida'}
    

Here we can see both entries with eid:14 got replace with new data. (ObjectId
will be different even if data is same).

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

