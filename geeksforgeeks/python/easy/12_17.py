Python | Replace multiple characters at once



The replacement of one character with another is a common problem that every
python programmer would have worked with in the past. But sometimes, we
require a simple one line solution which can perform this particular task.
Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Using nestedreplace()**  
This problem can be solved using the nested replace method, which internally
would create a temp. variable to hold the intermediate replacement state.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Replace multiple characters at once

# Using nested replace()

 

# initializing string 

test_str = "abbabba"

 

# printing original string 

print("The original string is : " + str(test_str))

 

# Using nested replace()

# Replace multiple characters at once

res = test_str.replace('a', '%temp%').replace('b',
'a').replace('%temp%', 'b')

 

# printing result 

print("The string after replacement of positions : " + res)  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : abbabba
    The string after replacement of positions : baabaab
    

**Method #2 : Usingtranslate() + maketrans()**  
There is also a dedication function which can perform this type of replacement
task in a single line hence this is a recommended way to solve this particular
problem. Works only in Python2.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working of

# Replace multiple characters at once

# Using translate() + maketrans()

import string

 

# initializing string 

test_str = "abbabba"

 

# printing original string 

print("The original string is : " + str(test_str))

 

# Using translate() + maketrans()

# Replace multiple characters at once

res = test_str.translate(string.maketrans("ab", "ba"))

 

# printing result 

print("The string after replacement of positions : " + res)  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : abbabba
    The string after replacement of positions : baabaab
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

