Python | Ways to concatenate boolean to string



Given a string and a boolean value, write a Python program to concatenate the
string with a boolean value, given below are few methods to solve the task.

 **Method #1: Usingformat()**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# to concatenate boolean value

# with string

 

# Initialising string and boolean value

ini_string = "Facts are"

value = True

 

# Concatenate using format

res = str(ini_string+" {}").format(value)

 

# Printing resultant string

print ("Resultant String : ", res)  
  
---  
  
 __

 __

 **Output:**

    
    
    Resultant String :  Facts are True
    

  
**Method #2: Using str**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# to concatenate boolean value

# with string

 

# Initialising string and boolean value

ini_string = "Facts are"

value = True

 

# Concatenate using str

res = ini_string +" "+str(value)

 

# Printing resultant string

print ("Resultant String : ", res)

 

   
  
---  
  
__

__

**Output:**

  

  

    
    
    Resultant String :  Facts are True
    

