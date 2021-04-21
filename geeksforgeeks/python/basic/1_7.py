How to generate a random letter in Python?



In this article, let’s discuss how to generate a random letter. Python
provides rich module support and some of these modules can help us to generate
random numbers and letters. There are multiple ways we can do that using
various Python modules.

 **Method 1: Using string and random module**

The string module has a special function ascii_letters which returns a string
containing all the alphabets from a-z and A-Z, i.e. all the lowercase and
uppercase alphabets. Using **random.choice()** we can choose any of the
particular characters from that string.

 **Code:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Import string and random module

import string

import random

 

# Randomly choose a letter from all the ascii_letters

randomLetter = random.choice(string.ascii_letters)

print(randomLetter)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    w

 **Method 2: Using the** **only random module**

Using random.randint(x,y) we can generate random integers from x to y. So we
can randomly generate ASCII value of one of the alphabets and then typecast
them to char using chr() function.

 **Code:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Import string and random module

import random

 

# Randomly generate a ascii value

# from 'a' to 'z' and 'A' to 'Z'

randomLowerLetter = chr(random.randint(ord('a'),
ord('z')))

randomUpperLetter = chr(random.randint(ord('A'),
ord('Z')))

print(randomLowerLetter, randomUpperLetter)  
  
---  
  
 __

 __

 **Output:**

    
    
    n M

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

