with statement in Python



 **with** statement in Python is used in exception handling to make the code
cleaner and much more readable. It simplifies the management of common
resources like file streams. Observe the following code example on how the use
of with statement makes code cleaner.

 __

 __  
 __

 __

 __  
 __  
 __

# file handling

 

# 1) without using with statement

file = open('file_path', 'w')

file.write('hello world !')

file.close()

 

# 2) without using with statement

file = open('file_path', 'w')

try:

 file.write('hello world')

finally:

 file.close()  
  
---  
  
 __

 __

__

__  
__

__

__  
__  
__

# using with statement

with open('file_path', 'w') as file:

 file.write('hello world !')  
  
---  
  
 __

 __

Notice that unlike the first two implementations, there is no need to
callfile.close() when using with statement. The with statement itself
ensures proper acquisition and release of resources. An exception during the
file.write() call in the first implementation can prevent the file from
closing properly which may introduce several bugs in the code, i.e. many
changes in files do not go into effect until the file is properly closed.

The second approach in the above example takes care of all the exceptions but
using the with statement makes the code compact and much more readable.
Thus, with statement helps avoiding bugs and leaks by ensuring that a
resource is properly released when the code using the resource is completely
executed. The with statement is popularly used with file streams, as shown
above and with Locks, sockets, subprocesses and telnets etc.

### Supporting the “with” statement in user defined objects

There is nothing special in open() which makes it usable with the with
statement and the same functionality can be provided in user defined objects.
Supporting with statement in your objects will ensure that you never leave
any resource open.  
To use with statement in user defined objects you only need to add the
methods __enter__() and __exit__() in the object methods. Consider the
following example for further clarification.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# a simple file writer object

 

class MessageWriter(object):

 def __init__(self, file_name):

 self.file_name = file_name

 

 def __enter__(self):

 self.file = open(self.file_name, 'w')

 return self.file

 

 def __exit__(self):

 self.file.close()

 

# using with statement with MessageWriter

 

with MessageWriter('my_file.txt') as xfile:

 xfile.write('hello world')  
  
---  
  
 __

 __

Let’s examine the above code. If you notice, what follows thewith keyword is
the constructor of MessageWriter. As soon as the execution enters the
context of the with statement a MessageWriter object is created and python
then calls the __enter__() method. In this __enter__() method, initialize
the resource you wish to use in the object. This __enter__() method should
always return a descriptor of the acquired resource.

 **What are resource descriptors?**  
These are the handles provided by the operating system to access the requested
resources. In the following code block, file is a descriptor of the file
stream resource.

 __

 __  
 __

 __

 __  
 __  
 __

file = open('hello.txt')  
  
---  
  
 __

 __

In theMessageWriter example provided above, the __enter__() method creates
a file descriptor and returns it. The name xfile here is used to refer to
the file descriptor returned by the __enter__() method. The block of code
which uses the acquired resource is placed inside the block of the with
statement. As soon as the code inside the with block is executed, the
__exit__() method is called. All the acquired resources are released in the
__exit__() method. This is how we use the with statement with user defined
objects.

This interface of __enter__() and __exit__() methods which provides the
support of with statement in user defined objects is called _**Context
Manager**_.

### The contextlib module

A class based context manager as shown above is not the only way to support
the with statement in user defined objects. The contextlib module provides
a few more abstractions built upon the basic context manager interface. Here
is how we can rewrite the context manager for the MessageWriter object using
the contextlib module.

 __

 __  
 __

 __

 __  
 __  
 __

from contextlib import contextmanager

 

class MessageWriter(object):

 def __init__(self, filename):

 self.file_name = filename

 

 @contextmanager

 def open_file(self):

 try:

 file = open(self.file_name, 'w')

 yield file

 finally:

 file.close()

 

# usage

message_writer = MessageWriter('hello.txt')

with message_writer.open_file() as my_file:

 my_file.write('hello world')  
  
---  
  
 __

 __

In this code example, because of theyield statement in its definition, the
function open_file() is a generator function.  
When this open_file() function is called, it creates a resource descriptor
named file. This resource descriptor is then passed to the caller and is
represented here by the variable my_file. After the code inside the with
block is executed the program control returns back to the open_file()
function. The open_file() function resumes its execution and executes the
code following the yield statement. This part of code which appears after
the yield statement releases the acquired resources. The @contextmanager
here is a decorator.

The previous class-based implementation and this generator-based
implementation of context managers is internally the same. While the later
seems more readable, it requires the knowledge of generators, decorators and
yield.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

