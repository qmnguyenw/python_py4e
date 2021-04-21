Python: Difference between Lock and Rlock objects



A thread is an entity within a process that can be scheduled for execution.
Also, it is the smallest unit of processing that can be performed in an OS
(Operating System). In simple words, a thread is a sequence of such
instructions within a program that can be executed independently of other
codes. For simplicity, you can assume that a thread is simply a subset of a
process!

>  **Refer to the below article the get the idea about threads.**
>
>   * Multithreading in Python
>

## Locks

These are the simplest primitive for synchronization in Python. There are two
states of a lock i.e **locked and unlocked**. A lock is a class in the
threading module whose object generated in the unlocked state and has two
primary methods i.e acquire() and release(). When the acquire() method is
called, it locks the execution of the Lock and blocks it’s execution until the
release() method is called in some other thread which sets it to unlock state.
Locks help us in efficiently accessing a shared resource in a program in order
to prevent corruption of data, it follows mutual exclusion as only one thread
can access a particular resource at a time.

Let us look at the below example to understand the use of Locks:

 __

 __  
 __

 __

 __  
 __  
 __

# program to illustrate the use of Locks

 

 

import threading

 

 

# creating a Lock object

lock = threading.Lock()

 

# initializing the shared resource

geek = 0

 

def sumOne():

 global geek

 

 # locking the shared resource

 lock.acquire()

 geek = geek + 1

 

 # unlocking the shared resource

 lock.release()

 

def sumTwo():

 global geek

 

 # locking the shared resource

 lock.acquire()

 geek = geek + 2

 

 # unlocking the shared resource 

 lock.release()

 

 

# calling the functions

sumOne()

sumTwo()

 

# displaying the value of shared resource

print(geek)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    3

In the above program, lock is a Lock object, the global variable geek is a
shared resource and sumOne() and sumTwo() functions act as threads, in
sumOne() function the shared resource geek is first locked and then
incremented by 1 and then geek is released and in sumTwo() function the
variable geek is first locked and then incremented by 2 and then geek is
released.The two functions sumOne() and sumTwo() can not access the shared
resource geek simultaneously, only one of them can access the shared
resource geek at a time.

## RLocks

The default Lock doesn’t recognize which thread the lock currently holds. If
the shared resource is being accessed by any thread then other threads trying
to access the shared resource will get blocked even if it is the same thread
that locked the shared resource. The Re-entrant lock or RLock is used in these
situations to prevent undesired blocking from accessing the shared resource.
If a shared resource is in RLock then it can be called again safely. The
RLocked resource can be accessed repeatedly by various threads, though it
still works correctly when called by different threads.

Let us look at the below example to understand the use of RLocks:

 __

 __  
 __

 __

 __  
 __  
 __

import threading

 

 

# initializing the shared resource

geek = 0

 

# creating a Lock object 

lock = threading.Lock()

 

# the below thread is accessing the

# shared resource

lock.acquire()

geek = geek + 1

 

# This thread will be blocked

lock.acquire() 

geek = geek + 2

lock.release()

 

# displaying the value of shared resource

print(geek)  
  
---  
  
 __

 __

In the above program, two threads are trying to access the shared
resourcegeek simultaneously, here when a thread is currently accessing
shared resource geek the other thread will be prevented from accessing it.
When two or more threads try to access the same resource effectively prevent
each other from accessing the resource this is known as deadlock due to which
the above program generates no output.

However, the above problem in the program can be solved by using RLock.

 __

 __  
 __

 __

 __  
 __  
 __

# program to illustrate the use of RLocks

 

# importing the module

import threading

 

# initializing the shared resource

geek = 0

 

# creating an RLock object instead 

# of Lock object 

lock = threading.RLock()

 

# the below thread is trying to access 

# the shared resource

lock.acquire()

geek = geek + 1

 

# the below thread is trying to access 

# the shared resource 

lock.acquire() 

geek = geek + 2

lock.release()

lock.release()

 

# displaying the value of shared resource

print(geek)  
  
---  
  
 __

 __

 **Output:**

    
    
    3

Here, there is no unwanted prevention of accessing the shared resource geek by
the threads in the program. We need to call release() once for each
acquire() of RLock object lock.

From the numerous programs and explanations mentioned above there are many
differences between a Lock object and an RLock object in Python:Locks| RLocks|
A Lock object can not be acquired again by any thread unless it is released by
the thread which which is accessing the shared resource.| An RLock object can
be acquired numerous times by any thread.| A Lock object can be released by
any thread.| An RLock object can only be released by the thread which acquired
it.| A Lock object can be owned by none| An RLock object can be owned by many
threads| Execution of a Lock object is faster.| Execution of an RLock object
is slower than a Lock object  
---|---  
  
Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

