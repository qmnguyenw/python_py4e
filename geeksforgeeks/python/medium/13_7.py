Python Main Function



Main function is like the entry point of a program. However, Python
interpreter runs the code right from the first line. The execution of the code
starts from the starting line and goes line by line. It does not matter where
the main function is present or it is present or not.

Since there is no main() function in Python, when the command to run a
Python program is given to the interpreter, the code that is at level 0
indentation is to be executed. However, before doing that, it will define a
few special variables. __name__ is one such special variable. If the source
file is executed as the main program, the interpreter sets the __name__
variable to have a value __main__. If this file is being imported from
another module, __name__ will be set to the module’s name.  
__name__ is a built-in variable which evaluates to the name of the current
module.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# main() function

 

 

print("Hello")

 

# Defining main function

def main():

 print("hey there")

 

 

# Using the special variable 

# __name__

if __name__=="__main__":

 main()  
  
---  
  
 __

 __

 **Output:**

    
    
    Hello
    hey there
    

When above program is executed, the interpreter declares the initial value of
name as “main”. When the interpreter reaches the if statement it checks for
the value of name and when the value of if is true it runs the main function
else the main function is not executed.

  

  

#### Main function as Module

Now when we import a Python script as module the __name__ variable gets the
value same as the name of the python script imported.

 **Example:** Let’s consider there are two Files(File1.py and File2.py). File1
is as follow.

 __

 __  
 __

 __

 __  
 __  
 __

# File1.py

 

print("File1 __name__ = %s" %__name__)

 

if __name__ == "__main__": 

 print("File1 is being run directly")

else: 

 print("File1 is being imported")  
  
---  
  
 __

 __

 **Output:**

    
    
    File1 __name__ = __main__
    File1 is being run directly
    

Now, when the File1.py is imported into File2.py, the value of __name__
changes.

 __

 __  
 __

 __

 __  
 __  
 __

# File2.py

 

import File1 

 

print("File2 __name__ = %s" %__name__)

 

if __name__ == "__main__":

 print("File2 is being run directly")

else: 

 print("File2 is being imported")  
  
---  
  
 __

 __

 **Output:**

    
    
    File1 __name__ = File1
    File1 is being imported
    File2 __name__ = __main__
    File2 is being run directly
    

As seen above, when File1.py is run directly, the interpreter sets the
__name__ variable as __main__ and when it is run through File2.py by
importing, the __name__ variable is set as the name of the python script, i.e.
File1. Thus, it can be said that if __name__ == “__main__” is the part of the
program that runs when the script is run from the command line using a command
like Python File1.py.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

