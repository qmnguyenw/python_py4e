Timer Objects in Python



Timer objects are used to represent actions that needs to be scheduled to run
after a certain instant of time. These objects get scheduled to run on a
separate thread that carries out the action. However, the interval that a
timer is initialized with might not be the actual instant when the action was
actually performed by the interpreter because it is the responsibility of the
thread scheduler to actually schedule the thread corresponding to the timer
object.

Timer is a sub class of Thread class defined in python. It is started by
calling the start() function corresponding to the timer explicitly.

 **Creating a Timer object**

 **Syntax:**

    
    
     **threading.Timer(interval, function, args = None, kwargs = None)** 

Create a timer that will run function with arguments args and keyword
arguments kwargs, after interval seconds have passed. If args is None (the
default) then an empty list will be used. If kwargs is None (the default) then
an empty dict will be used.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Program to demonstrate

# timer objects in python

 

import threading

def gfg():

 print("GeeksforGeeks\n")

 

timer = threading.Timer(2.0, gfg)

timer.start()

print("Exit\n")  
  
---  
  
 __

 __

 **Output:**

    
    
    Exit
    GeeksforGeeks

 **Explanation:** The program above, schedules gfg() function to run after 5
seconds of interval since start() function call.

 **Cancelling a timer**

 **Syntax:**

    
    
     **timer.cancel()**

Stop the timer, and cancel the execution of the timer’s action. This will only
work if the timer is still in its waiting stage.

 __

 __  
 __

 __

 __  
 __  
 __

# Program to cancel the timer

import threading

 

def gfg():

 print("GeeksforGeeks\n")

 

timer = threading.Timer(5.0, gfg)

timer.start()

print("Cancelling timer\n")

timer.cancel()

print("Exit\n")  
  
---  
  
 __

 __

Output:

    
    
    Cancelling timer
    Exit

This article is contributed by **Mayank Kumar**. If you like GeeksforGeeks and
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

