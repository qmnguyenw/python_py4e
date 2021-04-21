Python – Uppercase Selective Substrings in String



Given a String, perform uppercase of particular Substrings from List.

>  **Input** : test_str = ‘geeksforgeeks is best for cs’, sub_list = [“best”,
> “geeksforgeeks”]  
>  **Output** : GEEKSFORGEEKS is BEST for cs  
>  **Explanation** : geeksforgeeks and best uppercased.
>
>  **Input** : test_str = ‘geeksforgeeks is best for best’, sub_list =
> [“best”, “geeksforgeeks”]  
>  **Output** : GEEKSFORGEEKS is BEST for BEST  
>  **Explanation** : geeksforgeeks and best both occurrences uppercased.

 **Method #1 : Using split() + join() + loop**

In this, we repeatedly split the string by substring and then perform join
operation after joining the String with uppercased version of Substring. This
is success only in cases of 1 occurrence of substring in String.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Uppercase Selective Substrings in String

# Using split() + join() + loop

 

# initializing strings

test_str = 'geeksforgeeks is best for cs'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing substrings

sub_list = ["best", "cs", "geeksforgeeks"]

 

 

for sub in sub_list:

 

 # splitting string

 temp = test_str.split(sub, -1)

 

 # joining after uppercase

 test_str = sub.upper().join(temp)

 

 

# printing result 

print("The String after uppercasing : " + str(test_str))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeksforgeeks is best for cs
    The String after uppercasing : GEEKSFORGEEKS is BEST for CS
    

**Method #2 : Using re.sub() + upper()**

This uses regex to solve this problem. In this, we use appropriate regex, and
perform uppercase of found Strings.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Uppercase Selective Substrings in String

# Using re.sub() + upper()

import re

 

# initializing strings

test_str = 'geeksforgeeks is best for cs'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing substrings

sub_list = ["best", "cs", "geeksforgeeks"]

 

# constructing regex

reg = '|'.join(sub_list)

res = re.sub(reg, lambda ele: ele.group(0).upper(), test_str)

 

# printing result 

print("The String after uppercasing : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeksforgeeks is best for cs
    The String after uppercasing : GEEKSFORGEEKS is BEST for CS
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

