Python program to create dynamically named variables from user input



Given a string input, the task is to write a Python program to create a
variable from that input (as a variable name) and to assign it some value.
Below are the methods to create dynamically named variables from user input:

**Method 1:** Using globals() method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Dynamic_Variable_Name can be

# anything the user wants

Dynamic_Variable_Name = "geek"

 

# The value 2020 is assigned

# to "geek" variable

globals()[Dynamic_Variable_Name] = 2020

 

# Display varaible

print(geek)  
  
---  
  
 __

 __

 **Output:**

    
    
    2020

 **Method 2:** Using locals() method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Dynamic_Variable_Name can be

# anything the user wants.

Dynamic_Variable_Name = "geek"

 

# The value 2020 is assigned

# to "geek" variable

locals()[Dynamic_Variable_Name] = 2020

 

# Display variable

print(geek)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    2020

 **Method 3:** Using exec() method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Dynamic_Variable_Name can be

# anything the user wants.

Dynamic_Variable_Name = "geek"

 

# The value 2020 is assigned

# to "geek" variable

exec("%s = %d" % (Dynamic_Variable_Name, 2020))

 

# Display variable

print(geek)  
  
---  
  
 __

 __

 **Output:**

    
    
    2020

 **Method 4:** Using vars() method

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Dynamic_Variable_Name can be

# anything the user wants.

Dynamic_Variable_Name = "geek"

 

# The value 2020 is assigned

# to "geek" variable

vars()[Dynamic_Variable_Name] = 2020

 

# Display variable

print(geek)  
  
---  
  
 __

 __

 **Output:**

    
    
    2020

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

