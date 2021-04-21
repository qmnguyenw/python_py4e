Python | os.system() method



The OS module in python provides functions for interacting with the operating
system. OS, comes under Python’s standard utility modules. This module
provides a portable way of using operating system dependent functionality.

os.system() method execute the command (a string) in a subshell. This method
is implemented by calling the **Standard C function system()** , and has the
same limitations. If command generates any output, it is sent to the
interpreter standard output stream. Whenever this method is used then the
respective shell of the Operating system is opened and the command is executed
on it.

>  **Syntax:** os.system(command)
>
>  **Parameter:**  
>  **command:** It is of string type that tells which command to execute.
>
>  **Return Value:** On Unix, the return value is the exit status of the
> process and on Windows, the return value is the value returned by the system
> shell after running command.
>
>  
>
>
>  
>

 **Example #1 :**  
Using os.system() method to get current date of computer

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to explain os.system() method

 

# importing os module 

import os 

 

# Command to execute

# Using Windows OS command

cmd = 'date'

 

# Using os.system() method

os.system(cmd)  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190619004826/Annotation-2019-06-19-004523.png)

 **Example #2 :**  
Using os.system() method to run **Notepad**.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to explain os.system() method

 

# importing os module 

import os 

 

# Command to execute

# Using Windows OS command

cmd = 'notepad'

 

# Using os.system() method

os.system(cmd)  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190619120113/Annotation-2019-06-19-120037-1024x285.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

