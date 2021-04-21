Python – Remove N characters after K



Given a String, remove N characters after K character.

>  **Input** : test_str = ‘ge@987eksfor@123geeks is best@212 for cs’, N = 3, K
> = ‘@’  
>  **Output** : ‘geeksforgeeks is best for cs’  
>  **Explanation** : All 3 required occurrences removed.
>
>  **Input** : test_str = ‘geeksfor@123geeks is best for cs’, N = 3, K = ‘@’  
>  **Output** : ‘geeksforgeeks is best for cs’  
>  **Explanation** : @123 is removed.

 **Method #1 : Using re.sub()**

In this, we specify appropriate regex to capture the element and to remove
next N occurrences from String. The sub() is used to perform replacement.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove N characters after K

# Using re.sub()

import re

 

# initializing strings

test_str = 'geeksfor@123geeks is best@212 for cs'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing N 

N = 3

 

# initializing K 

K = '@'

 

# using re.sub() to perform task 

res = re.sub(r'\@...', '', test_str)

 

# printing result 

print("The String after removal : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeksfor@123geeks is best@212 for cs
    The String after removal : geeksforgeeks is best for cs
    

**Method #2 : Using re.sub() + occurrence option**

This is similar to above, just using 4th argument of re.sub() to control the
occurrence counts we wish to perform replace.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove N characters after K

# Using re.sub() + occurrence option

import re

 

# initializing strings

test_str = 'geeksfor@123geeks is best@212 for cs'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing N 

N = 3

 

# initializing K 

K = '@'

 

# using re.sub() to perform task 

# controlling occurrence using 4th arg.

# removes just 1st occurrence

res = re.sub(r'\@...', '', test_str, 1)

 

# printing result 

print("The String after removal : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeksfor@123geeks is best@212 for cs
    The String after removal : geeksforgeeks is best@212 for cs
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

