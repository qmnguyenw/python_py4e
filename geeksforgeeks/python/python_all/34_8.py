Python – Split strings ignoring the space formatting characters



Given a String, Split into words ignoring space formatting characters like \n,
\t etc.

>  **Input** : test_str = ‘geeksforgeeks\n\r\\\nt\t\n\t\tbest\r\tfor\f\vgeeks’  
> **Output** : [‘geeksforgeeks’, ‘best’, ‘for’, ‘geeks’]  
> **Explanation** : All space characters are used as parameter to join.
>
>  **Input** : test_str = ‘geeksforgeeks\n\r\\\nt\t\n\t\tbest’  
> **Output** : [‘geeksforgeeks’, ‘best’]  
> **Explanation** : All space characters are used as parameter to join.  
>

**Method 1: Using re.split()**

In this, we employ appropriate regex composed of space characters and use
split() to perform split on set of regex characters.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Split Strings igoring Space charaters

# Using re.split()

import re

 

# initializing string

test_str = 'geeksforgeeks\n\r\t\t\nis\t\tbest\r\tfor geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# space regex with split returns the result

res = re.split(r'[\n\t\f\v\r ]+', test_str)

 

# printing result 

print("The split string : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original string is : geeksforgeeks
    
            
    is        best
        for geeks
    The split string : ['geeksforgeeks', 'is', 'best', 'for', 'geeks']
    

**Method 2: Using split()**

The split() function by-default splits the string on white-spaces.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Split Strings igoring Space charaters

# Using split()

 

# initializing string

test_str = 'geeksforgeeks\n\r\t\t\nis\t\tbest\r\tfor geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# printing result 

print("The split string : " + str(test_str.split()))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original string is : geeksforgeeks
    
            
    is        best
        for geeks
    The split string : ['geeksforgeeks', 'is', 'best', 'for', 'geeks']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

