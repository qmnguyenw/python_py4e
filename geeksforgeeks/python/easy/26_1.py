Ways to print escape characters in Python



Escape characters are characters that are generally used to perform certain
tasks and their usage in code directs the compiler to take a suitable action
mapped to that character.

Example :

    
    
    '\n'  -->  Leaves a line
    '\t'  -->  Leaves a space 
    

__

__  
__

__

__  
__  
__

# Python code to demonstrate escape character

# string 

 

ch = "I\nLove\tGeeksforgeeks"

 

print ("The string after resolving escape character is : ")

print (ch)  
  
---  
  
 __

 __

Output :

    
    
    The string after resolving escape character is : 
    I
    Love    Geeksforgeeks
    

But in certain cases it is desired not to resolve escapes, i.e the entire
unresolved string has  
to be printed. These are achieved by following ways.

 **Using repr()**

This function returns a string in its printable format, i.e doesn’t resolve
the escape sequences.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate printing

# escape characters from repr()

 

# initializing target string 

ch = "I\nLove\tGeeksforgeeks"

 

print ("The string without repr() is : ")

print (ch)

 

print ("\r")

 

print ("The string after using repr() is : ")

print (repr(ch))  
  
---  
  
 __

 __

Output :

    
    
    The string without repr() is : 
    I
    Love    Geeksforgeeks
    
    
    The string after using repr() is : 
    'I\nLove\tGeeksforgeeks'
    

**Using “r/R”**

Adding “r” or “R” to the target string triggers a repr() to the string
internally and stops from the resolution of escape characters.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate printing

# escape characters from "r" or "R"

 

# initializing target string 

ch = "I\nLove\tGeeksforgeeks"

 

print ("The string without r / R is : ")

print (ch)

 

print ("\r")

 

# using "r" to prevent resolution

ch1 = r"I\nLove\tGeeksforgeeks"

 

print ("The string after using r is : ")

print (ch1)

 

print ("\r")

 

# using "R" to prevent resolution

ch2 = R"I\nLove\tGeeksforgeeks"

 

print ("The string after using R is : ")

print (ch2)  
  
---  
  
 __

 __

Output :

    
    
    The string without r/R is : 
    I
    Love    Geeksforgeeks
    
    
    The string after using r is : 
    I\nLove\tGeeksforgeeks
    
    
    The string after using R is : 
    I\nLove\tGeeksforgeeks
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

