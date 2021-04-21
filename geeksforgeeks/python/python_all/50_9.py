Python – Convert List to key-value list by prefix grouping



Given a list, convert it to consecutive key-value lists, grouping by prefix.

>  **Input** : test_list = [“GFG-1”, 4, 6, “GFG-2”, 3, “GFG-3”, 9, 2], temp =
> “GF”  
>  **Output** : {‘GFG-1’: [4, 6], ‘GFG-2’: [3], ‘GFG-3’: [9, 2]}  
>  **Explanation** : All grouped till next prefix.
>
>  **Input** : test_list = [“MRK-1”, 4, 6, “MRK-2”, 3, “MRK-3”, 9, 2], temp =
> “MR”  
>  **Output** : {‘MRK-1’: [4, 6], ‘MRK-2’: [3], ‘MRK-3’: [9, 2]}  
>  **Explanation** : All grouped till next prefix, “MR”.

 **Method : Using groupby() + startswith() + lambda**

The combination of above functions can be used to solve this problem. In this,
we employ grouping of all elements by prefix using groupby() and lambda
functions assists in performing segregation of prefix for grouping.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert List to key-value list by prefic grouping

# Using groupby() + startswith() + lambda

from itertools import groupby

 

# initializing list

test_list = ["GFG-1", 4, 6, 7, "GFG-2", 2, 3,
"GFG-3", 9, 2, 4, 6]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing prefix 

temp = "GFG"

 

res = {}

# extracting result from grouped by prefix

for key, val in groupby(test_list, lambda ele:
str(ele).startswith(temp)):

 

 # checking for existing key 

 if key:

 k = next(val)

 else:

 res[k] = list(val)

 

# printing result 

print("The constructed dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : ['GFG-1', 4, 6, 7, 'GFG-2', 2, 3, 'GFG-3', 9, 2, 4, 6]
    The constructed dictionary : {'GFG-1': [4, 6, 7], 'GFG-2': [2, 3], 'GFG-3': [9, 2, 4, 6]}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

