__file__ (A Special variable) in Python



A double underscore variable in Python is usually referred to as a dunder. A
dunder variable is a variable that Python has defined so that it can use it in
a “Special way”. This Special way depends on the variable that is being used.

 **Note:** For more information, refer to Dunder or magic methods in Python

#### __file__ variable

 **__file__** is a variable that contains the path to the module that is
currently being imported. Python creates a __file__ variable for itself when
it is about to import a module. The updating and maintaining of this variable
is the responsibility of the import system. The import system can choose to
leave the variable empty when there is no semantic meaning, that is when the
module/file is imported from the database. This attribute is a String. This
can be used to know the path of the module you are using. To understand the
usage of __file__ consider the following example.

 **Example:** Let’s create a module named JustMyModule and store it as a
.py file.

 __

 __  
 __

 __

 __  
 __  
 __

# Creating a module named

# JustMyModule

 

def hello():

 print("This is imported from JustMyModule")  
  
---  
  
 __

 __

Now let’s create another file named GFG.py that imports the above created
module to show the use of__file__ variable.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Importing the above

# created module

import JustMyModule

 

 

# Calling the method 

# created inside the module

JustMyModule.hello()

 

# printing the __file__

# variable

print(JustMyModule.__file__)  
  
---  
  
 __

 __

 **Output:**

![file__-python](https://media.geeksforgeeks.org/wp-
content/uploads/20200210172315/file__-python.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

