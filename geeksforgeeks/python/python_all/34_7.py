Python program to split a string by the given list of strings



Given a list of strings. The task is to split the string by the given list of
strings.

> **Input** : test_str = ‘geekforgeeksbestforgeeks’, sub_list = [“best”]  
> **Output** : [‘geekforgeeks’, ‘best’, ‘forgeeks’]  
> **Explanation** : “best” is extracted as different list element.
>
>  **Input** : test_str = ‘geekforgeeksbestforgeeksCS’, sub_list = [“best”,
> “CS”]  
> **Output** : [‘geekforgeeks’, ‘best’, ‘forgeeks’, “CS”]  
> **Explanation** : “best” and “CS” are extracted as different list element.  
>

**Method : Using re.split() + | operator**

In this, we perform the task of split using regex split() with | operator to
check for all the words that need to be put separately.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Separate specific Strings

# Using re.split() + | operator

import re

 

# initializing string

test_str = 'geekforgeeksisbestforgeeks'

 

# printing original String

print("The original string is : " + str(test_str))

 

# initializing list words 

sub_list = ["best"]

 

# regex to for splits()

# | operator to include all strings 

temp = re.split(rf"({'|'.join(sub_list)})", test_str)

res = [ele for ele in temp if ele] 

 

# printing result 

print("The segmented String : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geekforgeeksisbestforgeeks
    The segmented String : ['geekforgeeksis', 'best', 'forgeeks']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

