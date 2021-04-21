What is the Python Global Interpreter Lock (GIL)



Python Global Interpreter Lock (GIL) is a type of process lock which is used
by python whenever it deals with processes. Generally, Python only uses only
one thread to execute the set of written statements. This means that in python
only one thread will be executed at a time. The performance of the single-
threaded process and the multi-threaded process will be the same in python and
this is because of GIL in python. We can not achieve multithreading in python
because we have global interpreter lock which restricts the threads and works
as a single thread.

 **What problem did the GIL solve for Python :**

Python has something that no other language has that is a reference counter.
With the help of the reference counter, we can count the total number of
references that are made internally in python to assign a value to a data
object. Due to this counter, we can count the references and when this count
reaches to zero the variable or data object will be released automatically.
For Example

 __

 __  
 __

 __

 __  
 __  
 __

# Python program showing

# use of reference counter

import sys

 

geek_var = "Geek"

print(sys.getrefcount(geek_var))

 

string_gfg = geek_var

print(sys.getrefcount(string_gfg))  
  
---  
  
 __

 __

 **Output:**

    
    
    4
    5
    

This reference counter variable needed to be protected, because sometimes two
threads increase or decrease its value simultaneously by doing that it may
lead to memory leaked so in order to protect thread we add locks to all data
structures that are shared across threads but sometimes by adding locks there
exists a multiple locks which lead to another problem that is deadlock. In
order to avoid memory leaked and deadlocks problem, we used single lock on the
interpreter that is Global Interpreter Lock(GIL).  
  
**Why was the GIL chosen as the solution :**  
Python supports C language in the backend and all the related libraries that
python have are mostly written in C and C++. Due to GIL, Python provides a
better way to deal with thread-safe memory management. Global Interpreter Lock
is easy to implement in python as it only needs to provide a single lock to a
thread for processing in python. The GIL is simple to implement and was easily
added to Python. It provides a performance increase to single-threaded
programs as only one lock needs to be managed.  
  
**Impact on multi-threaded Python programs :**  
When a user writes Python programs or any computer programs then there’s a
difference between those that are CPU-bound in their performance and those
that are I/O-bound. CPU push the program to its limits by performing many
operations simultaneously whereas I/O program had to spend time waiting for
Input/Output. For Example  
 **Code 1: CPU bound program that perform simple countdown**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program showing

# CPU bound program

 

import time

from threading import Thread

 

COUNT = 50000000

 

def countdown(n):

 while n>0:

 n -= 1

 

start = time.time()

countdown(COUNT)

end = time.time()

 

print('Time taken in seconds -', end - start)  
  
---  
  
 __

 __

 **Output:**

    
    
    Time taken in seconds - 2.5236213207244873
    

**Code 2: Two threads running parallel**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program showing

# two threads running parallel

 

import time

from threading import Thread

 

COUNT = 50000000

 

def countdown(n):

 while n>0:

 n -= 1

 

t1 = Thread(target = countdown, args =(COUNT//2, ))

t2 = Thread(target = countdown, args =(COUNT//2, ))

 

start = time.time()

t1.start()

t2.start()

t1.join()

t2.join()

end = time.time()

 

print('Time taken in seconds -', end - start)  
  
---  
  
 __

 __

 **Output:**

    
    
    Time taken in seconds - 2.183610439300537
    

As you can see, In the above code two code where CPU bound process and multi-
threaded process have the same performance because in CPU bound program
because GIL restricts CPU to only work with a single thread. The impact of CPU
bound thread and multi-threading will be the same in python.

 **Why hasn’t the GIL been removed yet :**

GIL is not improved as of now because python 2 having GIL implementation and
if we change this in python 3 then it will create a problem for us. So instead
of removing GIL, we improve the concept of GIL. It’s one of the reasons to not
remove the GIL at yet is python heavily depends on C in the backend and C
extension heavily depends on the implementation methods of GIL. Although there
are many more methods to solve the problems that GIL solve most of them are
difficult to implement and can slow down the system.

 **How to deal with Python’s GIL :**

Most of the time we use the multiprocessing to prevent the program from GIL.
In this implementation, python provide a different interpreter to each process
to run so in this case the single thread is provided to each process in multi-
processing.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program showing

# multiprocessing

 

import multiprocessing 

import time

 

COUNT = 50000000

 

def countdown(n):

 while n>0:

 n -= 1

 

if __name__ == "__main__":

 # creating processes 

 start = time.time()

 p1 = multiprocessing.Process(target = countdown, args
=(COUNT//2, ))

 p2 = multiprocessing.Process(target = countdown, args
=(COUNT//2, ))

 

 # starting process 1 

 p1.start()

 # starting process 2 

 p2.start() 

 

 # wait until process 1 is finished 

 p1.join() 

 # wait until process 2 is finished 

 p2.join()

 end = time.time()

 print('Time taken in seconds -', end - start)  
  
---  
  
 __

 __

 **Output:**

    
    
    Time taken in seconds - 2.5148496627807617
    

As you can see that there is no difference between the time taken by the
multi-threaded system and the multi-processing system. This is because a
multi-processing system has their own problems to solve. So this will not
solve the problem but yes it provides the solution that GIL allows to be
performed by python.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

