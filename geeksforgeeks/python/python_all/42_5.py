Python – Remove after substring in String



Given a String, remove all characters after particular substring.

>  **Input** : test_str = ‘geeksforgeeks is best for geeks’, sub_str = “for”  
>  **Output** : geeksforgeeks is best for  
>  **Explanation** : everything removed after for.
>
>  **Input** : test_str = ‘geeksforgeeks is best for geeks’, sub_str = “is”  
>  **Output** : geeksforgeeks is  
>  **Explanation** : everything removed after is.

 **Method #1 : Using index() + len() + slicing**

In this, we first get the index of substring to perform removal after, add to
that its length using len() and then slice off elements after that string
using slicing.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove after substring in String

# Using index() + len() + slicing

 

# initializing strings

test_str = 'geeksforgeeks is best for geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing sub string 

sub_str = "best"

 

# slicing off after length computation

res = test_str[:test_str.index(sub_str) + len(sub_str)]

 

# printing result 

print("The string after removal : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeksforgeeks is best for geeks
    The string after removal : geeksforgeeks is best
    

**Method #2 : Using regex() ( for stripping off after numeric occurrence)**

This is solution to a slightly different problem in which the string removal
is required after numeric occurrence. We employ match operation and it retains
all before match is found.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove after substring in String

# Using regex() ( for stripping off after numeric occurrence)

import re

 

# initializing strings

test_str = 'geeksforgeeks is best 4 geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# slicing after the numeric occurrence

res = re.match(r"(.*\d+)", test_str).group()

 

# printing result 

print("The string after removal : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeksforgeeks is best 4 geeks
    The string after removal : geeksforgeeks is best 4
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

