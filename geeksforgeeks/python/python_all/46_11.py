Python program to verify that a string only contains letters, numbers,
underscores and dashes



 **Prerequisite:** Regular Expression in Python

Given a string, we have to find whether the string contains any letters,
numbers, underscores, and dashes or not. It is usually used for verifying
username and password validity. **For example,** the user has a string for the
username of a person and the user doesn’t want the username to have any
special characters such as @, $, etc.

Let’s see the different methods for solving this task:

 **Method 1:** Using **Regular Expression.**

There is a function in the regular expression library( **re** ) that compares
two string for us. **re.match(pattern, string)** is a function that returns an
object, to find whether a match is find or not we have to typecast it into
boolean.

  

  

> **Syntax:** re.match(pattern, string)
>
> **Parameters:**
>
>   *  **pattern:** the pattern against which you want to check
>   * **string:** the string you want to check for the pattern
>

>
> **Return:** Match object

Let’s see an example:

 **Example 1:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import library

import re

 

# make a pattern

pattern = "^[A-Za-z0-9_-]*$"

 

# input

string = "G33ks_F0r_Geeks"

 

# convert match object 

# into boolean values

state = bool(re.match(pattern, string))

 

print(state)  
  
---  
  
 __

 __

 **Output:**

    
    
    True

 **Example 2:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import library

import re

 

print(bool(re.match("^[A-Za-z0-9_-]*$",

 'ValidString12-_')))

 

print(bool(re.match("^[A-Za-z0-9_-]*$", 

 'inv@lidstring')))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    True
    False

 **Method 2:** Using **Set.**

Set is built-in data-type in Python. We are using ******issubset()** ****
function of set that returns True if all characters of a set are present in a
given set Otherwise False.

>  **Syntax:** set_name.issubset(set)  
>  **Parameters:**
>
>   *  **set:** Represents that set in which the subset has to be searched
>

>
> **Return:** boolean value

Let’s see an example:  
 **Example 1:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# create a set of allowed characters

allowed_chars =
set(("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-"))

 

# input string

string = "inv@lid"

 

# convert string into set of characters

validation = set((string))

 

# check condition

if validation.issubset(allowed_chars):

 print("True")

 

else:

 print ("False")  
  
---  
  
 __

 __

 **Output:**

    
    
    False

 **Example 2:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

allowed_chars=
set("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-")

 

string = "__Val1d__"

 

validation = set((string))

 

if validation.issubset(allowed_chars):

 print("True")

 

else:

 print ("False")  
  
---  
  
 __

 __

 **Output:**

    
    
    True

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

