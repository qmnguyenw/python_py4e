Context Manager in Python



 **Managing Resources :** In any programming language, the usage of resources
like file operations or database connections is very common. But these
resources are limited in supply. Therefore, the main problem lies in making
sure to release these resources after usage. If they are not released then it
will lead to resource leakage and may cause the system to either slow down or
crash. It would be very helpful if user have a mechanism for the automatic
setup and teardown of resources.In Python, it can be achieved by the usage of
context managers which facilitate the proper handling of resources. The most
common way of performing file operations is by using the _with_ keyword as
shown below:

 __

 __  
 __

 __

 __  
 __  
 __

# Python program showing

# a use of with keyword

 

with open("test.txt") as f: 

 data = f.read()  
  
---  
  
 __

 __

Let’s take the example of file management. When a file is opened, a file
descriptor is consumed which is a limited resource. Only a certain number of
files can be opened by a process at a time. The following program demonstrates
it.

 __

 __  
 __

 __

 __  
 __  
 __

file_descriptors= []

for x in range(100000):

 file_descriptors.append(open('test.txt', 'w'))  
  
---  
  
 __

 __

 **Output:**

    
    
    Traceback (most recent call last):
      File "context.py", line 3, in 
    OSError: [Errno 24] Too many open files: 'test.txt'
    

An error message saying that too many files are open. The above example is a
case of file descriptor leakage. It happens because there are too many open
files and they are not closed. There might be chances where a programmer may
forget to close an opened file.

 **Managing Resources using context manager :**

  

  

Suppose a block of code raises an exception or if it has a complex algorithm
with multiple return paths, it becomes cumbersome to close a file in all the
places.  
Generally in other languages when working with files _try-except-finall_ y is
used to ensure that the file resource is closed after usage even if there is
an exception.Python provides an easy way to manage resources: _Context
Managers_. The _with_ keyword is used. When it gets evaluated it should result
in an object that performs context management. Context managers can be written
using classes or functions(with decorators).

 **Creating a Context Manager :**

When creating context managers using classes, user need to ensure that the
class has the methods: ___enter__()_ and ___exit__()_. The __enter__() returns
the resource that needs to be managed and the __exit__() does not return
anything but performs the cleanup operations.  
First, lets create a simple class called _ContextManager_ to understand the
basic structure of creating context managers using classes, as shown below:

 __

 __  
 __

 __

 __  
 __  
 __

# Python program creating a

# context manager

 

class ContextManager():

 def __init__(self):

 print('init method called')

 

 def __enter__(self):

 print('enter method called')

 return self

 

 def __exit__(self, exc_type, exc_value, exc_traceback):

 print('exit method called')

 

 

with ContextManager() as manager:

 print('with statement block')  
  
---  
  
 __

 __

 **Output:**

    
    
    init method called
    enter method called
    with statement block
    exit method called
    

In this case a ContextManager object is created. This is assigned to the
variable after the _as_ keyword i.e _manager_. On running the above program,
the following get executed in sequence:

  * __init__()

  * __enter__()

  * statement body (code inside the _with_ block)

  * __exit__()[the parameters in this method are used to manage exceptions]

 **File management using context manager :**

Let’s apply the above concept to create a class that helps in file resource
management.The FileManager class helps in opening a file, writing/reading
contents and then closing it.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program showing

# file management using 

# context manager

 

class FileManager():

 def __init__(self, filename, mode):

 self.filename = filename

 self.mode = mode

 self.file = None

 

 def __enter__(self):

 self.file = open(self.filename, self.mode)

 return self.file

 

 def __exit__(self, exc_type, exc_value, exc_traceback):

 self.file.close()

 

# loading a file 

with FileManager('test.txt', 'w') as f:

 f.write('Test')

 

print(f.closed)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    True
    

  
**File management using context manager and with statement :**

On executing the _with_ block, the following operations happen in sequence:

  * A _FileManager_ object is created with _test.txt_ as the filename and _w_ (write) as the mode when __init__ method is executed.

  * The __enter__ method opens the _test.txt_ file in write mode(setup operation) and returns the _FileManager_ object to variable _f_.

  * The text ‘Test’ is written into the file.

  * The __exit__ method takes care of closing the file on exiting the _with_ block(teardown operation).  
When _print(f.closed)_ is run, the output is _True_ as the _FileManager_ has
already taken care of closing the file which otherwise needed to be explicitly
done.

 **Database connection management using context manager :**

Let’s create a simple database connection management system. The number of
database connections that can be opened at a time is also limited(just like
file descriptors). Therefore context managers are helpful in managing
connections to the database as there could be chances that the programmer may
forget to close the connection.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program shows the

# connection management 

# for MongoDB

 

from pymongo import MongoClient

 

class MongoDBConnectionManager():

 def __init__(self, hostname, port):

 self.hostname = hostname

 self.port = port

 self.connection = None

 

 def __enter__(self):

 self.connection = MongoClient(self.hostname, self.port)

 return self

 

 def __exit__(self, exc_type, exc_value, exc_traceback):

 self.connection.close()

 

# connecting with a localhost

with MongoDBConnectionManager('localhost', '27017') as mongo:

 collection = mongo.connection.SampleDb.test

 data = collection.find({'_id': 1})

 print(data.get('name'))  
  
---  
  
 __

 __

  
**Database connection management using context manager and with statement :**

On executing the _with_ block, the following operations happen in sequence:

  * A _MongoDBConnectionManager_ object is created with _localhost_ as the hostnamename and _27017_ as the port when __init__ method is executed.

  * The __enter__ method opens the mongodb connection and returns the _MongoDBConnectionManager_ object to variable _mongo_.

  * The test collection in SampleDb database is accessed and the document with __id_ =1 is retrieved. The name field of the document is printed.

  * The __exit__ method takes care of closing the connection on exiting the _with_ block(teardown operation).

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

