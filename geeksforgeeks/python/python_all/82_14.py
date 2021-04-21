Python | Printing String with double quotes



Many times, while working with Python strings, we have a problem in which we
need to use double quotes in a string and then wish to print it. This kind of
problem occurs in many domains like day-day programming and web-development
domain. Lets discuss certain ways in which this task can be performed.

 **Method #1 : Using backslash (“\”)**  
This is one way to solve this problem. In this, we just employ a backslash
before a double quote and it is escaped.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Printing String with double quotes

# Using backslash

 

# initializing string

# using backslash

test_str = "geeks\"for\"geeks"

 

# printing string

print("The string escaped with backslash : " + test_str)  
  
---  
  
 __

 __

 **Output :**

    
    
    The string escaped with backslash : geeks"for"geeks
    

**Method #2 : Using triple quotes**  
This is one more way in python to print and initialize a string. Apart from
multiline comment, triple quotes are also good way of escaping.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Printing String with double quotes

# Using triple quotes

 

# initializing string

# using triple quotes

test_str = """geeks"for"geeks"""

 

# printing string

print("The string escaped with triple quotes : " + test_str)  
  
---  
  
 __

 __

 **Output :**

    
    
    The string escaped with triple quotes : geeks"for"geeks
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

