What is the difference between Python’s Module, Package and Library?



 **Module:** The **module** is a simple Python file that contains collections
of functions and global variables and with having a .py extension file. It
is an executable file and to organize all the modules we have the concept
called Package in Python.

 **Example:** Save the code in file called demo_module.py

 __

 __  
 __

 __

 __  
 __  
 __

def myModule(name):

 print("This is My Module : "+ name)  
  
---  
  
 __

 __

Import module named demo_module and call myModule function inside it.

 __

 __  
 __

 __

 __  
 __  
 __

import demo_module

 

demo_module.myModule("Math")  
  
---  
  
 __

 __

 **Output:**

    
    
    This is My Module : Math

 **Package:** The **package** is a simple directory having collections of
modules. This directory contains Python modules and also having __init__.py
file by which the interpreter interprets it as a Package. The package is
simply a namespace. The package also contains sub-packages inside it.

  

  

 **Example:**

    
    
    Student(Package)
    | __init__.py (Constructor)
    | details.py (Module)
    | marks.py (Module)
    | collegeDetails.py (Module)

 **Library:** The **library** is having a collection of related functionality
of codes that allows you to perform many tasks without writing your code. It
is a reusable chunk of code that we can use by importing it in our program, we
can just use it by importing that library and calling the method of that
library with period(.).

 **Example:** Importing pandas library and call read_csv method using alias of
pandas i.e. pd.

 __

 __  
 __

 __

 __  
 __  
 __

import pandas as pd

 

df = pd.read_csv("file_name.csv")  
  
---  
  
 __

 __

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

