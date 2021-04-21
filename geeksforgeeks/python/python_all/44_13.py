Python – Character Replacement Combination



Given a String and dictionary with characters mapped to replacement characters
values list, construct all possible strings after replacing present characters
with mapped values.

>  **Input** : test_str = “geeks”, test_dict = {‘s’ : [‘1’, ‘5’], ‘k’ : [‘3’]}  
>  **Output** : [‘gee31’, ‘geek1’, ‘gee35’, ‘geek5’, ‘gee3s’, ‘geeks’]  
>  **Explanation** : All possible replacement of strings, e.g in ‘gee35’, k is
> replaced by ‘3’ and s is replaced by ‘5’.
>
>  **Input** : test_str = “geeks”, test_dict = {‘s’ : [‘1’], ‘k’ : [‘3’]}  
>  **Output** : [‘gee31’, ‘geek1’, ‘gee3s’, ‘geeks’]  
>  **Explanation** : All possible replacement of strings, e.g in ‘gee31’, k is
> replaced by ‘3’ and s is replaced by ‘1’.

 **Method : Using zip() + list comprehension + replace() + product()**

The combination of above functions can be used to solve this problem. In this,
we extract all the combination characters using product and pair one at a time
using zip(), replacement using replace().

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Character Replacement Combination

# Using zip() + list comprehension + replace() + product()

from itertools import product

 

# initializing string

test_str = "geeks"

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing dictionary

test_dict = {'s' : ['1', '2'], 'k' : ['3']}

 

# adding original character to possible characters 

for key in test_dict.keys():

 if key not in test_dict[key]:

 test_dict[key].append(key)

 

res = []

 

# constructing all possible combination of values using product

# mapping using zip()

for sub in [zip(test_dict.keys(), chr) for chr in
product(*test_dict.values())]:

 temp = test_str

 for repls in sub:

 

 # replacing all elements at once using * operator

 temp = temp.replace(*repls)

 res.append(temp)

 

# printing result 

print("All combinations : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeks
    All combinations : ['gee31', 'geek1', 'gee32', 'geek2', 'gee3s', 'geeks']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

