string capitalize() in Python



In Python, the **capitalize()** method returns a copy of the original string
and converts the first character of the string to a capital **(uppercase)**
letter while making all other characters in the string **lowercase** letters.  

**Syntax:**

    
    
    _string_name_.capitalize() 
    
    **string_name** : It is the name of string of
                 whose first character we want
                 to capitalize.

 **Parameter:** The capitalize() function does not takes any parameter.  
**Return value:** The capitalize() function returns a string with the first
character in the capital.  
Below is the python program to illustrate capitalize() function:  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate the

# use of capitalize() function

# capitalize() first letter of string

# and make other letters lowercase

name = "geeks FOR geeks"

print(name.capitalize())

# demonstration of individual words

# capitalization to generate camel case

name1 = "geeks"

name2 = "for"

name3 = "geeks"

print(name1.capitalize() + name2.capitalize()

 + name3.capitalize())  
  
---  
  
 __

 __

 **Output:**  

    
    
    Geeks for geeks
    GeeksForGeeks

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

