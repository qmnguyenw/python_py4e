Python – Split String on vowels



Given a String, perform split on vowels.

> **Input** : test_str = ‘GFGaBst’  
>  **Output** : [‘GFG’, ‘Bst’]  
>  **Explanation** : a is vowel and split happens on that.
>
>  **Input** : test_str = ‘GFGaBstuforigeeks’  
>  **Output** : [‘GFG’, ‘Bst’, ‘for’, ‘geeks’]  
>  **Explanation** : a, u, i are vowels and split happens on that.

 **Method : Using regex() + split()**

In this, we use regex split() which accepts multiple characters to perform
split, passing list of vowels, performs split operation over string.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Split String on vowels

# Using split() + regex

import re

 

# initializing strings

test_str = 'GFGaBste4oCS'

 

# printing original string

print("The original string is : " + str(test_str))

 

# splitting on vowels 

# constructing vowels list

# and seperating using | operator

res = re.split('a|e|i|o|u', test_str)

 

# printing result 

print("The splitted string : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : GFGaBste4oCS
    The splitted string : ['GFG', 'Bst', '4', 'CS']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

