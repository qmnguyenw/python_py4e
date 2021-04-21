Python – Remove digits from Dictionary String Values List



Given list of dictionaries with string list values, remove all the numerics
from all strings.

>  **Input** : test_dict = {‘Gfg’ : [“G4G is Best 4”, “4 ALL geeks”], ‘best’ :
> [“Gfg Heaven”, “for 7 CS”]}  
>  **Output** : {‘Gfg’: [‘GG is Best ‘, ‘ ALL geeks’], ‘best’: [‘Gfg Heaven’,
> ‘for CS’]}  
>  **Explanation** : All the numeric strings are removed.
>
>  **Input** : test_dict = {‘Gfg’ : [“G4G is Best 4”, “4 ALL geeks”]}  
>  **Output** : {‘Gfg’: [‘GG is Best ‘, ‘ ALL geeks’]}  
>  **Explanation** : All the numeric strings are removed.

 **Method : Using regex + dictionary comprehension**

This problem can be solved using combination of both functionalities. In this,
we apply regex to replace each digit with empty string and compile the result
using dictionary comprehension.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove digits from Dictionary String Values List

# Using loop + regex() + dictionary comprehension 

import re

 

# initializing dictionary

test_dict = {'Gfg' : ["G4G is Best 4", "4 ALL geeks"],

 'is' : ["5 6 Good"], 

 'best' : ["Gfg Heaven", "for 7 CS"]} 

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# using dictionary comprehension to go through all keys

res = {key: [re.sub('\d', '', ele) for ele in val]

 for key, val in test_dict.items()}

 

# printing result 

print("The filtered dictionary : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': ['G4G is Best 4', '4 ALL geeks'], 'is': ['5 6 Good'], 'best': ['Gfg Heaven', 'for 7 CS']}
    The filtered dictionary : {'Gfg': ['GG is Best ', ' ALL geeks'], 'is': ['  Good'], 'best': ['Gfg Heaven', 'for  CS']}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

