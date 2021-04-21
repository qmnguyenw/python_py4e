Python string | digits



In Python3, **string.digits** is a pre-initialized string used as string
constant. In Python, string.digits will give the lowercase letters
‘0123456789’.

>  **Syntax :** string.digits
>
>  **Parameters :** Doesn’t take any parameter, since it’s not a function.
>
>  **Returns :** Return all digit letters.

 **Note :** Make sure to import string library function inorder to use
string.digits

  

  

 **Code #1 :**

 __

 __  
 __

 __

 __  
 __  
 __

# import string library function

import string 

 

# Storing the value in variable result 

result = string.digits 

 

# Printing the value 

print(result)   
  
---  
  
__

__

**Output :**

    
    
    0123456789

  
**Code #2 :** Given code checks if the string input has only digit letters

 __

 __  
 __

 __

 __  
 __  
 __

# importing string library function

import string 

 

# Function checks if input string 

# har only digits or not 

def check(value): 

 for letter in value: 

 

 # If anything other than digit 

 # letter is present, then return 

 # False, else return True 

 if letter not in string.digits: 

 return False

 return True

 

# Driver Code 

input1 = "0123 456 789"

print(input1, "--> ", check(input1)) 

 

input2 = "12.0124"

print(input2, "--> ", check(input2)) 

 

input3 = "12345"

print(input3, "--> ", check(input3))   
  
---  
  
__

__

**Output:**

    
    
    0123 456 789 -->  False
    12.0124 -->  False
    12345 -->  True

 **Applications :**  
The string constant **digits** can be used in many practical applications.
Let’s see a code explaining how to use digits to generate strong random
passwords of given size.

 __

 __  
 __

 __

 __  
 __  
 __

# Importing random to generate

# random string sequence 

import random 

 

# Importing string library function 

import string 

 

def rand_pass(size): 

 

 # Takes random choices from 

 # ascii_letters and digits 

 generate_pass = ''.join([random.choice( string.ascii_uppercase +

 string.ascii_lowercase +

 string.digits) 

 for n in range(size)]) 

 

 return generate_pass 

 

# Driver Code 

password = rand_pass(10) 

print(password) 

   
  
---  
  
__

__

**Output:**

    
    
    2R8gaoDKqn

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

