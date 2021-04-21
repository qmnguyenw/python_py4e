How to make a Python program wait?



 **Prerequisites:**

  * time module
  * keyboard module
  * os module

Some requirements require a Python program to wait before it goes on. We might
need another function to complete or a file to load to give the user a better
experience. Discussed below are some ways by which this can be achieved.

## Different methods and approaches

### 1\. Python time module

 **1(A) General sleep function**

Python has a module named _time **.**_ **** This module gives several useful
functions to control time-related tasks. sleep() is one such function that
suspends the execution of the calling thread for a given number of seconds and
returns void. The argument may be a floating-point number to indicate more
precise sleep time. This is the most common method used because of its ease of
use and the fact that it is platform independent. The implementation is given
below:

 **Example:**

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# First import time module.

import time

 

# immediately prints the following.

print("GFG printed immediately.")

time.sleep(5.5)

 

# delays the execution

# for 5.5 secs.

print("GFG printed after 5.5 secs.")  
  
---  
  
 __

 __

 **Output:**

https://media.geeksforgeeks.org/wp-content/uploads/20201201130155/py1.mp4

 **1(B) Sleep in multithreaded programming**

For multithreaded python programs, the _sleep() ****_ function suspends the
current thread for a given number of seconds rather than the whole process.
But for single-threaded programs _sleep()_ function suspends the thread and
the whole process. The implementation is given below:

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import threading and time module.

import threading

import time

 

def print_GFG():

 for i in range(5):

 # suspend the current thread.

 time.sleep(1)

 print("GFG")

 

def print_Geeksforgeeks():

 for i in range(5):

 # suspend the current thread.

 time.sleep(1.5)

 print("Geeksforgeeks")

 

# two threads are available in this program.

t1 = threading.Thread(target=print_GFG)

t2 = threading.Thread(target=print_Geeksforgeeks)

t1.start()

t2.start()  
  
---  
  
 __

 __

 **Output:**

https://media.geeksforgeeks.org/wp-content/uploads/20201201131540/py2.mp4

####

### **2\. Using simple input()**

We all know that the **input()** function helps to take data from users. But
with the help of this function, we can also pause a python script until a
certain key is pressed, like in the following code:

  

  

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

print("GFG immediately")

i = input("Press Enter to continue: ")

 

# pauses the script here

# until the user press any key.

print("GFG after the input.")  
  
---  
  
 __

 __

 **Output:**

https://media.geeksforgeeks.org/wp-content/uploads/20201201131853/py3.mp4

### 3\. Using keyboard module

Using this module, we can resume the program by pressing the key that is
specified in the python script (In this program the key is the ‘space _ **‘**_
key). Keyboard module doesn’t come in-built with python, thus needs to be
installed explicitly using the following command:

    
    
    pip install keyboard

The implementation is given below:

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import keyboard module.

import keyboard

 

# pause() function definition.

def pause():

 while True:

 if keyboard.read_key() == 'space':

 # If you put 'space' key

 # the program will resume.

 break

 

 

print("GeeksforGeeks printed before pause function")

pause()

print("GeeksforGeeks printed after pause function")  
  
---  
  
 __

 __

 **Output:**

https://media.geeksforgeeks.org/wp-content/uploads/20201201133620/py4.mp4

###  **4\. Using code module**

This module contains a function called interact(). Some non-programmers may
like this simple method. This creates an interpreter that acts almost exactly
like a real interpreter. This creates a new instance of Interactive Console
and sets readfunc to be used as the InteractiveConsole.raw_input() method if
provided.

 **Example:**

For the program given below press (Ctrl+D) to resume.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import code

import code

 

print("GeeksforGeeks printed immediately.")

 

# implementation of code.interact().

code.interact(banner='Paused. Press ^D (Ctrl+D) to continue.',
local=globals())

print("GeeksforGeeks.")  
  
---  
  
 __

 __

 **Output:**

https://media.geeksforgeeks.org/wp-content/uploads/20201201134239/py5.mp4

###  **5\. Using os module**

Os module contains a method called system(“pause”). Using this method we can
make a python program wait until some key is pressed. But this method is
platform dependent i.e. only works on windows. So, it is not widely used.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import os

 

print("GeeksforGeeks printed immediately.")

os.system("pause")

print("GeeksforGeeks.")  
  
---  
  
 __

 __

 **Output:**

https://media.geeksforgeeks.org/wp-content/uploads/20201201135021/py6.mp4

####

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

