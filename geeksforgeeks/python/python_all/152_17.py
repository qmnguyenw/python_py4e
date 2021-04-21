Python | Get the numeric prefix of given string



Given a string. the task is to print numeric prefix in string (if it is
present in string). Given below are few methods to solve the task.

 **Method #1: Using Naive Method**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# to get numeric prefix in string

# if present

 

# initialising string

ini_string = "123abcjw"

ini_string2 = "abceddfgh"

 

# printing string and its length

print ("initial string : ", ini_string, ini_string2)

 

# code to find numeric prefix in string

res1 = ''.join(c for c in ini_string if c in '0123456789')

res2 = ''.join(c for c in ini_string2 if c in '0123456789')

 

 

# printing resultant string

print ("first string result: ", str(res1))

print ("second string result: ", str(res2))  
  
---  
  
 __

 __

 **Output:**

    
    
    initial string :  123abcjw abceddfgh
    first string result:  123
    second string result:
    

**Method #2: Usingtakewhile**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# to get numeric prefix in string

# if present

from itertools import takewhile

 

# initialising string

ini_string = "123abcjw"

ini_string2 = "abceddfgh"

 

# printing string and its length

print ("initial string : ", ini_string, ini_string2)

 

# code to find numeric prefix in string

res1 = ''.join(takewhile(str.isdigit, ini_string))

res2 = ''.join(takewhile(str.isdigit, ini_string2))

 

# printing resultant string

print ("first string result: ", res1)

print ("second string result: ", res2)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    initial string :  123abcjw abceddfgh
    first string result:  123
    second string result:
    

