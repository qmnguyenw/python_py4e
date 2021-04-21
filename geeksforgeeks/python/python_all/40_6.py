Python – Case Insensitive string counter



Given a List of Strings, find frequency of strings case insensitive.

>  **Input** : test_list = [“Gfg”, “Best”, “GFG”, “is”, “IS”, “BEST”]  
>  **Output** : {‘gfg’: 2, ‘best’: 2, ‘is’: 2}  
>  **Explanation** : All occur twice.
>
>  **Input** : test_list = [“Gfg”, “gfg”, “GFG”]  
>  **Output** : {‘gfg’: 3}  
>  **Explanation** : Only “gfg” 3 occurrences.

 **Method : Using defaultdict() + lower()**

In this, we perform lower() to all the strings, before mapping in defaultdict.
This ensures case insensitivity while mapping and cumulating frequency.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Strings Frequency (Case Insensitive)

# Using defaultdict() + lower()

from collections import defaultdict

 

# initializing list

test_list = ["Gfg", "Best", "best", "gfg", "GFG",
"is", "IS", "BEST"]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = defaultdict(int)

for ele in test_list:

 

 # lowercasing to cater for Case Insensitivity

 res[ele.lower()] += 1

 

# printing result 

print("Strings Frequency : " + str(dict(res)))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : ['Gfg', 'Best', 'best', 'gfg', 'GFG', 'is', 'IS', 'BEST']
    Strings Frequency : {'gfg': 3, 'best': 3, 'is': 2}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

