Python | Ways to split strings using newline delimiter



Given a string, write a Python program to split strings on the basis of
newline delimiter. Given below are a few methods to solve the given task.

 **Method #1: Usingsplitlines()**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# to split strings

# on newline delimiter

 

# Initialising string

ini_str = 'Geeks\nFor\nGeeks\n'

 

# Printing Initial string

print ("Initial String", ini_str)

 

# Splitting on newline delimiter

res_list = ini_str.splitlines()

 

# Printing result

print("Resultant prefix", str(res_list))  
  
---  
  
 __

 __

 **Output:**

    
    
    Initial String Geeks
    For
    Geeks
    
    Resultant prefix ['Geeks', 'For', 'Geeks']
    

  
**Method #2: Usingsplit() method**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# to split strings

# on newline delimiter

 

# Initialising string

ini_str = 'Geeks\nFor\nGeeks\n'

 

# Printing Initial string

print ("Initial String", ini_str)

 

# Splitting on newline delimiter

res_list = (ini_str.rstrip().split('\n'))

 

# Printing result

print("Resultant prefix", str(res_list))  
  
---  
  
 __

 __

 **Output:**

    
    
    Initial String Geeks
    For
    Geeks
    
    Resultant prefix ['Geeks', 'For', 'Geeks']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

