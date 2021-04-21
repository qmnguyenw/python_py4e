Python | Remove spaces from a string



Given a string, write a Python program to remove all spaces from it.

 **Examples:**

    
    
    **Input :**  g e e k
    **Output :** geek
    
    **Input :** Hello World
    **Output :** HelloWorld
    

There are various approaches to remove whitespaces in a string. The first one
is the Naive approach, which has been discussed in this article. But here we
will discuss all the approaches which are specific to Python.

 **Approach#1 :** Using replace()

Using replace() function, we replace all whitespace with no space(“”).

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to remove whitespace

def remove(string):

 return string.replace(" ", "")

 

# Driver Program

string = ' g e e k '

print(remove(string))  
  
---  
  
 __

 __

 **Output:**

    
    
    geek
    

**Approach #2 :** Using split() and join()

First we use split() function to return a list of the words in the string,
using _sep_ as the delimiter string. Then, we use join() to concatenate the
iterable.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to remove whitespace

def remove(string):

 return "".join(string.split())

 

# Driver Program

string = ' g e e k '

print(remove(string))  
  
---  
  
 __

 __

 **Output:**

    
    
    geek
    

  
**Approach #3 :** Using Python regex

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to remove whitespace

import re

 

def remove(string):

 pattern = re.compile(r'\s+')

 return re.sub(pattern, '', string)

 

# Driver Program

string = ' g e e k '

print(remove(string))  
  
---  
  
 __

 __

 **Output:**

    
    
    geek
    

**Approach #4 :** Using translate()

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to remove whitespace

import string

 

def remove(string):

 return string.translate(None, ' \n\t\r')

 

# Driver Program

string = ' g e e k '

print(remove(string))  
  
---  
  
 __

 __

 **Output:**

    
    
    geek
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

