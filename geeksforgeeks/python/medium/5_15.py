Handling a thread’s exception in the caller thread in Python



Multithreading in Python can be achieved by using the threading library. For
invoking a thread, the caller thread creates a thread object and calls the
start method on it. Once the join method is called, that initiates its
execution and executes the run method of the class object.

For Exception handling, try-except blocks are used that catch the exceptions
raised across the try block and are handled accordingly in the except block

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Importing the modules

import threading

import sys

 

# Custom Thread Class

class MyThread(threading.Thread):

 def someFunction(self):

 print("Hello World")

 def run(self):

 self.someFunction()

 def join(self):

 threading.Thread.join(self)

 

# Driver function

def main():

 t = MyThread()

 t.start()

 t.join()

 

# Driver code

if __name__ == '__main__':

 main()  
  
---  
  
 __

 __

 **Output:**

    
    
    Hello World
    

For catching and handling a thread’s exception in the caller thread we use a
variable that stores the raised exception (if any) in the called thread, and
when the called thread is joined, the join function checks whether the value
of exc is None, if it is then no exception is generated, otherwise, the
generated exception that is stored in exc is raised again. This happens in the
caller thread and hence can be handled in the caller thread itself.

  

  

 **Example:** The example creates a thread t of type MyThread, the run()
method for the thread calls the someFunction() method, that raises the
MyException, thus whenever the thread is run, it will raise an exception. To
catch the exception in the caller thread we maintain a separate variable exc,
which is set to the exception raised when the called thread raises an
exception. This exc is finally checked in the join() method and if is not
None, then join simply raises the same exception. Thus, the caught exception
is raised in the caller thread, as join returns in the caller thread (Here The
Main Thread) and is thus handled correspondingly.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Importing the modules

import threading

import sys

 

# Custom Exception Class

class MyException(Exception):

 pass

 

# Custom Thread Class

class MyThread(threading.Thread):

 

 # Function that raises the custom exception

 def someFunction(self):

 name = threading.current_thread().name

 raise MyException("An error in thread "+ name)

 

 def run(self):

 

 # Variable that stores the exception, if raised by someFunction

 self.exc = None

 try:

 self.someFunction()

 except BaseException as e:

 self.exc = e

 

 def join(self):

 threading.Thread.join(self)

 # Since join() returns in caller thread

 # we re-raise the caught exception

 # if any was caught

 if self.exc:

 raise self.exc

 

# Driver function

def main():

 

 # Create a new Thread t

 # Here Main is the caller thread

 t = MyThread()

 t.start()

 

 # Exception handled in Caller thread

 try:

 t.join()

 except Exception as e:

 print("Exception Handled in Main, Detials of the Exception:", e)

 

# Driver code

if __name__ == '__main__':

 main()  
  
---  
  
 __

 __

 **Output:**

> Exception Handled in Main, Detials of the Exception: An error in thread
> Thread-1

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

