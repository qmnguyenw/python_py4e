Python | Ways to convert Boolean values to integer



Given a boolean value(s), write a Python program to convert them into an
integer value or list respectively. Given below are a few methods to solve the
above task.

 **Method #1: Using int() method**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# to convert boolean value to integer

 

# Initialsing Values

bool_val = True

 

# Printing initial Values

print("Initial value", bool_val)

 

# Converting boolean to integer

bool_val = int(bool_val == True)

 

# Printing result

print("Resultant value", bool_val)

   
  
---  
  
__

__

**Output:**

    
    
    Initial value True
    Resultant value 1
    

  
**Method #2: Using Naive Approach**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# to convert boolean

# value to integer

 

# Initialsing Values

bool_val = True

 

# Printing initial Values

print("Initial value", bool_val)

 

# Converting boolean to integer

if bool_val:

 bool_val = 1

else:

 bool_val = 0

# Printing result

print("Resultant value", bool_val)

   
  
---  
  
__

__

**Output:**

  

  

    
    
    Initial value True
    Resultant value 1
    

