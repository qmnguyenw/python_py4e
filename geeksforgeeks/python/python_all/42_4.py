Python – Add space between Numbers and Alphabets in String



Given a string consisting of numbers and Strings, add space between them.

>  **Input** : test_str = ‘ge3eks4geeks is1for10geeks’  
>  **Output** : ge 3 eks 4 geeks is 1 for 10 geeks  
>  **Explanation** : Numbers separated from Characters.
>
>  **Input** : test_str = ‘ge3eks4geeks’  
>  **Output** : ge 3 eks 4 geeks  
>  **Explanation** : Numbers separated from Characters by space.

 **Method #1 : Using regex + sub() + lambda**

In this, we perform the task of finding alphabets by appropriate regex and
then sub() is used to do replacements, lambda does the task of adding spaces
in between.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Add space between Numbers and Alphabets in String

# using regex + sub() + lambda

import re

 

# initializing string

test_str = 'geeks4geeks is1for10geeks'

 

# printing original String

print("The original string is : " + str(test_str))

 

# using sub() to solve the problem, lambda used tp add spaces 

res = re.sub("[A-Za-z]+", lambda ele: " " + ele[0] +
" ", test_str)

 

# printing result 

print("The space added string : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeks4geeks is1for10geeks
    The space added string :  geeks 4 geeks   is 1 for 10 geeks 
    

**Method #2 : Using regex + sub()**

This is one of ways to solve. In this, we look for numerics rather than
alphabets to perform task of segregation, similar approach by use numerics are
search criteria to add spaces.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Add space between Numbers and Alphabets in String

# using regex + sub()

import re

 

# initializing string

test_str = 'geeks4geeks is1for10geeks'

 

# printing original String

print("The original string is : " + str(test_str))

 

# using sub() to solve the problem, lambda used tp add spaces 

res = re.sub('(\d+(\.\d+)?)', r' \1 ', test_str)

 

# printing result 

print("The space added string : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeks4geeks is1for10geeks
    The space added string : geeks 4 geeks is 1 for 10 geeks
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

