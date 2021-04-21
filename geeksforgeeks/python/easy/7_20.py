Python – sys.stdout.flush()



A data buffer is a region of physical memory storage used to temporarily store
data while it is being moved from one place to another. The data is stored in
a buffer as it is retrieved from an input device or just before it is sent to
an output device or when moving data between processes within a computer.
Python’s standard out is buffered. This means that it collects some data
before it is written to standard out and when the buffer gets filled, then it
is written on the terminal or any other output stream.

Let’s look at the code below :

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program demonstrating working

# of flush during output 

 

import sys

import time

 

for i in range(10):

 print(i)

 time.sleep(1)  
  
---  
  
 __

 __

 **Output:**

    
    
    0
    1
    2
    3
    4
    5
    6
    7
    8
    9

When the above program is executed, then the numbers from 0 to 9 are printed
after every second on a new line, i.e., the output is automatically flushed
out. This is because, by default end parameter of print statement is set to
‘\n’ which flushes the output.

Now let’s look at the code below :

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program demonstrating working

# of flush during output

 

import sys

import time

 

for i in range(10):

 print(i, end =' ')

 time.sleep(1)  
  
---  
  
 __

 __

 **Output:**

    
    
    0 1 2 3 4 5 6 7 8 9

When the above program is executed, then there is no output for the first 9
seconds, then at the 10th, all the 10 numbers from 0 to 9 appear
simultaneously in a line separated by spaces. This is because the output is
buffered and it is not flushed by any means.

Now, look at the code below :

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program demonstrating working

# of flush during output and usage of

# sys.stdout.flush() function

 

import sys

import time

 

for i in range(10):

 print(i, end =' ')

 sys.stdout.flush()

 time.sleep(1)  
  
---  
  
 __

 __

 **Output:**

    
    
    0 1 2 3 4 5 6 7 8 9

When the above program is executed, the numbers from 0 to 9 are printed every
second on the same line separated by spaces. This is because calling
sys.stdout.flush() forces it to “flush” the buffer, meaning that it will
write everything in the buffer to the terminal, even if normally it would wait
before doing so. The sys module provides functions and variables used to
manipulate different parts of the Python runtime environment. It lets us
access system-specific parameters and functions.

Another way of achieving the same functionality as above is setting the flush
parameter of the print statement to true.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program demonstrating working

# of flush during output and usage of

# flush parameter of print statement

 

import sys

import time

 

for i in range(10):

 print(i, end =' ', flush = True)

 time.sleep(1)  
  
---  
  
 __

 __

 **Output:**

    
    
    0 1 2 3 4 5 6 7 8 9 

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

