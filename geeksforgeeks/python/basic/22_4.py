Python string | isalnum()



isalnum() function in Python programming language checks whether all the
characters in a given string is alphanumeric or not.

 **Alphanumeric** : _A character that is either a letter or a number_

 **Syntax:**

> string_name.isalnum()  
> string_name is the name of the string

 **Parameter:** isalnum() method takes no parameters

  

  

 **Return:**

>  **True:** If all the characters are alphanumeric  
>  **False:** If one or more characters are not alphanumeric

 _Below is the Python implementation of the isalnum() method_

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate the use of

# isalnum() method 

 

# here a,b and c are characters and 1,2 and 3

# are numbers

string = "abc123"

print(string.isalnum())

 

# here a,b and c are characters and 1,2 and 3 

# are numbers but space is not a alphanumeric 

# character

string = "abc 123"

print(string.isalnum())   
  
---  
  
__

__

Output:

    
    
    True
    False
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

