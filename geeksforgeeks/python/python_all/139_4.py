Python | Deleting all occurrences of character



These days string manipulation is very popular in Python, and due to it’s
immutable character, sometimes, it becomes more important to know it’s working
and hacks. This particular article solves the problem of deleting all
occurrences of character from a string. Let’s discuss ways in which this can
be achieved.

 **Method #1 : Usingtranslate()**  
Usually this function is used to convert a particular character to some other
character. By translating the resultant removal character to “None”, this
function can perform this task. This function works only for Python2

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working of

# Deleting all occurrences of character

# Using translate()

 

# initializing string 

test_str = "GeeksforGeeks"

 

# initializing removal character

rem_char = "e"

 

# printing original string 

print("The original string is : " + str(test_str))

 

# Using translate()

# Deleting all occurrences of character

res = test_str.translate(None, rem_char)

 

# printing result 

print("The string after character deletion : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : GeeksforGeeks
    The string after character deletion : GksforGks
    

**Method #2 : Usingreplace()**  
This function works functionally quite similar to the above function, but it
is recommended due to several reasons. It can be used in newer versions of
Python and is more efficient than the above function. We replace the empty
string instead of None as above for using this function to perform this task.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Deleting all occurrences of character

# Using replace()

 

# initializing string 

test_str = "GeeksforGeeks"

 

# initializing removal character

rem_char = "e"

 

# printing original string 

print("The original string is : " + str(test_str))

 

# Using replace()

# Deleting all occurrences of character

res = test_str.replace(rem_char, "")

 

# printing result 

print("The string after character deletion : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : GeeksforGeeks
    The string after character deletion : GksforGks
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

