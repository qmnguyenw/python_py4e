ascii_letters in Python



In Python3, _**ascii_letters**_ is a pre-initialized string used as string
constant.  
 _ **ascii_letters**_ is basically concatenation of _**ascii_lowercase**_ and
_**ascii_uppercase**_ string constants. Also, the value generated is not
locale-dependent, hence, doesn’t change.

 **Syntax :**

    
    
    string.ascii_letters

 **Note :** Make sure to import string library function inorder to use
_ascii_letters_.

 **Parameters :**

    
    
     Doesn't take any parameter, since it's not a function. 

**Returns :**

  

  

    
    
     Return all ASCII letters (both lower and upper case)

  
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

result = string.ascii_letters

 

# Printing the value

print(result)  
  
---  
  
 __

 __

 **Output :**

    
    
    abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

**Code #2 :**  
Given code checks if the string input has only ASCII characters or not.

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

# has only ascii letters or not

def check(value):

 for letter in value:

 

 # If anything other than ascii

 # letter is present, then return

 # False, else return True

 if letter not in string.ascii_letters:

 return False

 return True

 

# Driver Code

input1 = "GeeksForGeeks"

print(input1, "--> ", check(input1))

 

input2 = "Geeks for Geeks"

print(input2, "--> ", check(input2))

 

input3 = "Geeks_for_geeks"

print(input3, "--> ", check(input3))  
  
---  
  
 __

 __

 **Output :**

    
    
    GeeksForGeeks -->  True
    Geeks for Geeks -->  False
    Geeks_for_geeks -->  False

  
**Applications :**  
The string constant ascii_letters can be used in many practical applications.  
Let’s see a code explaining how to use ascii_letters to generate strong random
passwords of given size.

 **Code #1 :**

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

 generate_pass = ''.join([random.choice(

 string.ascii_letters + string.digits)

 for n in range(size)])

 

 return generate_pass

 

# Driver Code 

password = rand_pass(10)

print(password)

 

   
  
---  
  
__

__

**Output :**

    
    
    oQjI5MOXQ3

 **Note :** Above given code will print random (different) password everytime,
for the size provided.  
  
**Code #2 :**  
Say if you want to generate random password, but from the set of given string.
Let’s see how can we do this using ascii_letters :

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

 

def rand_pass(size, scope = string.ascii_letters + string.digits):

 

 # Takes random choices from ascii_letters and digits

 generate_pass = ''.join([random.choice(scope)

 for n in range(size)])

 

 return generate_pass

 

# Driver Code 

password = rand_pass(10, 'Geeks3F0rgeeKs')

print(password)  
  
---  
  
 __

 __

 **Output :**

    
    
    kg3g03keG3

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

