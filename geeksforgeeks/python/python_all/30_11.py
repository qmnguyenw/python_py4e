Python – Extract String after Nth occurrence of K character



Given a String, extract the string after Nth occurrence of a character.

> **Input** : test_str = ‘geekforgeeks’, K = “e”, N = 2  
>  **Output** : kforgeeks  
>  **Explanation** : After 2nd occur. of “e” string is extracted.
>
>  **Input** : test_str = ‘geekforgeeks’, K = “e”, N = 4  
>  **Output** : ks  
>  **Explanation** : After 4th occur. of “e” string is extracted.

 **Method #1 : Using split()**

This is one of the ways in which this task can be performed. In this we
customize split() to split on Nth occurrence and then print the rear extracted
string using “-1”.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract String after Nth occurrence of K character 

# Using split()

 

# initializing string

test_str = 'geekforgeeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing K 

K = "e"

 

# initializing N 

N = 3

 

# using split() to perform required string split

# "-1" to extract required part

res = test_str.split(K, N)[-1]

 

# printing result 

print("The extracted string : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geekforgeeks
    The extracted string : eks
    

**Method #2 : Using re.split()**

This is yet another way to solve this problem. Similar to above function, we
perform split() to perform task of splitting but from regex library which also
provides flexibility to split on Nth occurrence.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract String after Nth occurrence of K character 

# Using re.split()

import re

 

# initializing string

test_str = 'geekforgeeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing K 

K = "e"

 

# initializing N 

N = 3

 

# using split() to perform required string split

# "-1" to extract required part

res = re.split(K, test_str, N)[-1]

 

# printing result 

print("The extracted string : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geekforgeeks
    The extracted string : eks
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

