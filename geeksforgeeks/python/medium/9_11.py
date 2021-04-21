How to create a new thread in Python



 **Threads**in python is an entity within a process that can be scheduled for
execution. In simpler words, a thread is a computation process that is to be
performed by a computer. It is a sequence of such instructions within a
program that can be executed independently of other codes.

In python there are two ways to create a new Thread. In this article we will
also be making use of the **threading module** in Python. Below is a detailed
list of those processes:

 **1\. Creating python threads using class:**

Below has a coding example followed by the code explanation for creating new
threads using class in python.

 __

 __  
 __

 __

 __  
 __  
 __

# import the threading module

import threading 

 

class thread(threading.Thread): 

 def __init__(self, thread_name, thread_ID): 

 threading.Thread.__init__(self) 

 self.thread_name = thread_name 

 self.thread_ID = thread_ID 

 

 # helper function to execute the threads

 def run(self): 

 print(str(self.thread_name) +" "+
str(self.thread_ID)); 

 

thread1 = thread("GFG", 1000) 

thread2 = thread("GeeksforGeeks", 2000); 

 

thread1.start() 

thread2.start() 

 

print("Exit")   
  
---  
  
__

__

**Output:**

  

  

    
    
    GFG 1000
    GeeksforGeeks 2000
    Exit

Now let’s look into what we did up there in the code.

  1. We created a sub-class of the thread class.
  2. Then we overrode the __init__ function of the thread class.
  3. then we overrode the run method to define the behavior of the thread.
  4. The start() method starts a Python thread.

 **1\. Creating python threads using function:**

The below code shows the creation of new thread using a function:

 __

 __  
 __

 __

 __  
 __  
 __

from threading import Thread

from time import sleep

 

# function to create threads

def threaded_function(arg):

 for i in range(arg):

 print("running")

 

 # wait 1 sec in between each thread

 sleep(1)

 

 

if __name__ == "__main__":

 thread = Thread(target = threaded_function, args = (10,
))

 thread.start()

 thread.join()

 print("thread finished...exiting")  
  
---  
  
 __

 __

 **Output:**

    
    
    running
    running
    running
    running
    running
    running
    running
    running
    running
    running
    thread finished...exiting

So what we did in the above code,

  1. We defined a function to create a thread.
  2. Then we used the threading module to create a thread that invoked the function as its target.
  3. Then we used start() method to start the Python thread.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

