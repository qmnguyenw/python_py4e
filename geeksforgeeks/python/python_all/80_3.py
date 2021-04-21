Python | Replace punctuations with K



Sometimes, while working with Python Strings, we have a problem in which we
need to perform the replace of punctuations in String with specific character.
This can have application in many domains such as day-day programming. Lets
discuss certain ways in which this task can be performed.

 **Method #1 : Usingstring.punctuation + replace()**  
The combination of above functions can be used to solve this problem. In this,
we extract all punctuations using punctuation and perform a replace of
character desired using replace().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Replace punctuations with K

# Using string.punctuation + replace()

from string import punctuation

 

# initializing string

test_str = 'geeksforgeeks, is : best for ; geeks !!'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing replace character

repl_char = '*'

 

# Replace punctuations with K

# Using string.punctuation + replace()

for chr in punctuation:

 test_str = test_str.replace(chr, repl_char)

 

# printing result 

print("The strings after replacement : " + test_str)   
  
---  
  
__

__

**Output :**

    
    
    The original string is : geeksforgeeks, is : best for ; geeks!!
    The strings after replacement : geeksforgeeks* is * best for * geeks**
    

**Method #2 : Using regex**  
This problem can be solved using regex. In this, we employ a regex to
substitute for all punctuations.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Replace punctuations with K

# Using regex

import re

 

# initializing string

test_str = 'geeksforgeeks, is : best for ; geeks !!'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing replace character

repl_char = '*'

 

# Replace punctuations with K

# Using regex

res = re.sub(r'[^\w\s]', repl_char, test_str)

 

# printing result 

print("The strings after replacement : " + res)   
  
---  
  
__

__

**Output :**

    
    
    The original string is : geeksforgeeks, is : best for ; geeks!!
    The strings after replacement : geeksforgeeks* is * best for * geeks**
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

