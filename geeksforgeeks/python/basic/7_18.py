Collections.UserString in Python



 **Strings** are the arrays of bytes representing Unicode characters. However,
Python does not support the character data type. A character is a string of
length one.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# string

 

# Creating a String 

# with single Quotes 

String1 = 'Welcome to the Geeks World'

print("String with the use of Single Quotes: ") 

print(String1) 

 

# Creating a String 

# with double Quotes 

String1 = "I'm a Geek"

print("\nString with the use of Double Quotes: ") 

print(String1)   
  
---  
  
__

__

**Output:**

    
    
    String with the use of Single Quotes: 
    Welcome to the Geeks World
    
    String with the use of Double Quotes: 
    I'm a Geek
    

**Note:** For more information, refer to Python String

## Collections.UserString

Python supports a String like a container called **UserString** present in the
collections module. This class acts as a wrapper class around the string
objects. This class is useful when one wants to create a string of their own
with some modified functionality or with some new functionality. It can be
considered as a way of adding new behaviors for the string. This class takes
any argument that can be converted to string and simulates a string whose
content is kept in a regular string. The string is accessible by the data
attribute of this class.

  

  

 **Syntax:**

    
    
    collections.UserString(seq)
    

**Example 1:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# userstring

 

 

from collections import UserString

 

 

d = 12344

 

# Creating an UserDict

userS = UserString(d)

print(userS.data)

 

 

# Creating an empty UserDict

userS = UserString("")

print(userS.data)  
  
---  
  
 __

 __

 **Output:**

    
    
    12344
    
    

**Example 2:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# userstring

 

 

from collections import UserString

 

 

# Creating a Mutable String

class Mystring(UserString):

 

 # Function to append to

 # string

 def append(self, s):

 self.data += s

 

 # Function to rmeove from 

 # string

 def remove(self, s):

 self.data = self.data.replace(s, "")

 

# Driver's code

s1 = Mystring("Geeks")

print("Original String:", s1.data)

 

# Appending to string

s1.append("s")

print("String After Appending:", s1.data)

 

# Removing from string

s1.remove("e")

print("String after Removing:", s1.data)  
  
---  
  
 __

 __

 **Output:**

    
    
    Original String: Geeks
    String After Appending: Geekss
    String after Removing: Gkss

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

