Communication between Parent and Child process using pipe in Python



Prerequisite – Creating child process in Python  
As there are many processes running simultaneously on the computer so it is
very necessary to have proper communication between them as one process may be
dependent on other processes.There are various methods to communicate between
processes. Here is a simple Python program to demonstrate communication
between the parent process and child process using the pipe method.

 **Library Used –**  
OS Module in Python : The OS module in Python provides a way of using
operating system dependent functionality. The functions that the OS module
provides allows you to interface with the underlying operating system that
Python is running on; be that Windows, Mac or Linux. It can be imported as –

    
    
    import os
    

**System Call Used –**  
 **pipe() System call : **The method pipe() creates a pipe and returns a pair
of file descriptors (r, w) usable for reading and writing, respectively. This
method **returns** a pair of file descriptor.

 **Syntax –** Following is the syntax for pipe() method –

    
    
    os.pipe()
    

**Note –** Pipe is one-way communication only i.e we can use a pipe such that
One process write to the pipe, and the other process reads from the pipe.

  

  

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate communication

# between parent and child process using 

# python.

 

import os

 

def communication(child_writes):

 # file descriptors r, w for reading and writing

 r, w = os.pipe()

 

 #Creating child process using fork

 processid = os.fork()

 if processid:

 # This is the parent process

 # Closes file descriptor w

 os.close(w)

 r = os.fdopen(r)

 print ("Parent reading")

 str = r.read()

 print( "Parent reads =", str)

 else:

 # This is the child process

 os.close(r)

 w = os.fdopen(w, 'w')

 print ("Child writing")

 w.write(child_writes)

 print("Child writes = ",child_writes)

 w.close()

 

# Driver code 

child_writes = "Hello geeks"

communication(child_writes)

 

# Contributed by "Sharad_Bhardwaj".  
  
---  
  
 __

 __

 **Output :**

    
    
    Child writing
    Child writes =  Hello geeks
    Parent reading
    Parent reads = Hello geeks
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

