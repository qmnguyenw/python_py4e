Understanding Python Pickling with example



Prerequisite: Pickle Module

Python pickle module is used for serializing and de-serializing a Python
object structure. Any object in Python can be pickled so that it can be saved
on disk. What pickle does is that it “serializes” the object first before
writing it to file. Pickling is a way to convert a python object (list, dict,
etc.) into a character stream. The idea is that this character stream contains
all the information necessary to reconstruct the object in another python
script.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to illustrate store

# efficiently using pickle module 

# Module translates an in-memory Python object 

# into a serialized byte stream—a string of 

# bytes that can be written to any file-like object.

 

import pickle

 

def storeData():

 # initializing data to be stored in db

 Omkar = {'key' : 'Omkar', 'name' : 'Omkar Pathak',

 'age' : 21, 'pay' : 40000}

 Jagdish = {'key' : 'Jagdish', 'name' : 'Jagdish
Pathak',

 'age' : 50, 'pay' : 50000}

 

 # database

 db = {}

 db['Omkar'] = Omkar

 db['Jagdish'] = Jagdish

 

 # Its important to use binary mode

 dbfile = open('examplePickle', 'ab')

 

 # source, destination

 pickle.dump(db, dbfile) 

 dbfile.close()

 

def loadData():

 # for reading also binary mode is important

 dbfile = open('examplePickle', 'rb') 

 db = pickle.load(dbfile)

 for keys in db:

 print(keys, '=>', db[keys])

 dbfile.close()

 

if __name__ == '__main__':

 storeData()

 loadData()  
  
---  
  
 __

 __

 **Output:**

    
    
    omkarpathak-Inspiron-3542:~/Documents/Python-Programs$ python P60_PickleModule.py
    Omkar => {'age': 21,  'name': 'Omkar Pathak',  'key': 'Omkar',  'pay': 40000}
    Jagdish => {'age': 50,  'name': 'Jagdish Pathak',  'key': 'Jagdish',  'pay': 50000}
    

**Pickling without a file**

 __

 __  
 __

 __

 __  
 __  
 __

# initializing data to be stored in db

Omkar = {'key' : 'Omkar', 'name' : 'Omkar Pathak', 

'age' : 21, 'pay' : 40000}

Jagdish = {'key' : 'Jagdish', 'name' : 'Jagdish Pathak',

'age' : 50, 'pay' : 50000}

 

# database

db = {}

db['Omkar'] = Omkar

db['Jagdish'] = Jagdish

 

# For storing

b = pickle.dumps(db) # type(b) gives <class 'bytes'>

 

# For loading

myEntry = pickle.loads(b)

print(myEntry)  
  
---  
  
 __

 __

 **Advantages of using Pickle Module:**

  

  

  1.  **Recursive objects (objects containing references to themselves):** Pickle keeps track of the objects it has already serialized, so later references to the same object won’t be serialized again. (The marshal module breaks for this.)
  2.  **Object sharing (references to the same object in different places):** This is similar to self- referencing objects; pickle stores the object once, and ensures that all other references point to the master copy. Shared objects remain shared, which can be very important for mutable objects.
  3.  **User-defined classes and their instances:** Marshal does not support these at all, but pickle can save and restore class instances transparently. The class definition must be importable and live in the same module as when the object was stored.

This article is contributed by **Omkar Pathak**. If you like GeeksforGeeks and
would like to contribute, you can also write an article using
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

