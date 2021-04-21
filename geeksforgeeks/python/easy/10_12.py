Create and Import modules in Python



In Python, a module is a self-contained Python file that contains Python
statements and definitions, like a file named GFG.py, can be considered as a
module named GFG which can be imported with the help of import statement.
However, one might get confused about the difference between modules and
packages. A package is a collection of modules in directories that give
structure and hierarchy to the modules.

#### Advantages of modules –

  *  **Reusability** : Working with modules makes the code reusability a reality.
  *  **Simplicity:** Module focuses on a small proportion of the problem, rather than focusing on the entire problem.
  *  **Scoping:** A separate namespace is defined by a module that helps to avoid collisions between identifiers.

## Creating and Importing a module

A module is simply a Python file with a .py extension that can be imported
inside another Python program. The name of the Python file becomes the module
name. The module contains definitions and implementation of classes,
variables, and functions that can be used inside another program.

 **Example:** Let’s create a simple module named GFG.

 __

 __  
 __

 __

 __  
 __  
 __

''' GFG.py '''

 

# Python program to create

# a module

 

 

# Defining a function

def Geeks():

 print("GeeksforGeeks")

 

# Defining a variable

location = "Noida"  
  
---  
  
 __

 __

The above example shows the creation of a simple module named GFG as the name
of the above Python file is GFG.py. When this code is executed it does nothing
because the function created is not invoked.

To use the above created module, create a new Python file in the same
directory and import GFG module using the import statement.

  

  

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# modules

 

 

import GFG

 

# Use the function created

GFG.Geeks()

 

# Print the variable declared

print(GFG.location)  
  
---  
  
 __

 __

 **Output:**

    
    
    GeeksforGeeks
    Noida
    

The above example shows a simple module with only functions and variables. Now
let’s create a little bit complex module with classes, functions, and
variables. Below is the implementation.

 **Example:** Open the above created GFG module and make the following
changes.

 __

 __  
 __

 __

 __  
 __  
 __

''' GFG.py '''

 

# Python program to demonstrate 

# modules

 

 

# Defining a function

def Geeks():

 print("GeeksforGeeks")

 

# Defining a variable

location = "Noida"

 

# Defining a class

class Employee():

 

 def __init__(self, name, position):

 self. name = name

 self.position = position

 

 def show(self):

 print("Employee name:", self.name)

 print("Employee position:", self.position)  
  
---  
  
 __

 __

In this example, a class named employee has been declared with a method show()
to print the details of the employee. Now open the Python script for importing
and using this module.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# modules

 

 

import GFG

 

 

# Use the class created

emp = GFG.Employee("Nikhil", "Developer")

emp.show()  
  
---  
  
 __

 __

 **Output:**

    
    
    Employee name: Nikhil
    Employee position: Developer
    

#### Import all names

All the object from a module can be imported as a variable. This prevents the
usage of the module name as a prefix.

  

  

 **Syntax:**

    
    
    from module_name_ import *
    

**Example:** We will use the above created GFG module.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# modules

 

 

from GFG import *

 

 

# Calling the function

Geeks()

 

# Printing the variable

print(location)

 

# Calling class

emp = Employee("Nikhil", "Developer")

emp.show()  
  
---  
  
 __

 __

 **Output:**

    
    
    GeeksforGeeks
    Noida
    Employee name: Nikhil
    Employee position: Developer
    

#### Import with renaming

A module can be imported with another name, specified by the user.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# modules

 

 

import GFG as g

 

 

# Calling the function

g.Geeks()

 

# Printing the variable

print(g.location)

 

# Calling class

emp = g.Employee("Nikhil", "Developer")

emp.show()  
  
---  
  
 __

 __

 **Output:**

    
    
    GeeksforGeeks
    Noida
    Employee name: Nikhil
    Employee position: Developer
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

