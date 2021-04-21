Python – Split String on all punctuations



Given a String, Split the String on all the punctuations.

>  **Input** : test_str = ‘geeksforgeeks! is-best’  
>  **Output** : [‘geeksforgeeks’, ‘!’, ‘is’, ‘-‘, ‘best’]  
>  **Explanation** : Splits on ‘!’ and ‘-‘.
>
>  **Input** : test_str = ‘geek-sfo, rgeeks! is-best’  
>  **Output** : [‘geek’, ‘-‘, ‘sfo’, ‘, ‘, ‘rgeeks’, ‘!’, ‘is’, ‘-‘, ‘best’]  
>  **Explanation** : Splits on ‘!’, ‘, ‘ and ‘-‘.

 **Method : Using regex + findall()**

This is one way in which this problem can be solved. In this, we construct
appropriate regex and task of segregating and split is done by findall().

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Split String on all punctuations

# using regex + findall()

import re

 

# initializing string

test_str = 'geeksforgeeks ! is-best, for @geeks'

 

# printing original String

print("The original string is : " + str(test_str))

 

# using findall() to get all regex matches. 

res = re.findall( r'\w+|[^\s\w]+', test_str)

 

# printing result 

print("The converted string : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeksforgeeks! is-best, for @geeks
    The converted string : ['geeksforgeeks', '!', 'is', '-', 'best', ', ', 'for', '@', 'geeks']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

