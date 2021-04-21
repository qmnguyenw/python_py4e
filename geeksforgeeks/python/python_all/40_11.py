Python – Column-wise elements in Dictionary value list



Given dictionary with value list, extract elements columnwise.

>  **Input** : test_dict = {‘Gfg’ : [3, 6], ‘is’ : [4, 2], ‘best’ :[9, 1]}  
>  **Output** : [3, 4, 9, 6, 2, 1]  
>  **Explanation** : 3, 4, 9 from col1 and then 6, 2, 1 from 2 are extracted
> in order.
>
>  **Input** : test_dict = {‘Gfg’ : [3], ‘is’ : [4], ‘best’ :[9]}  
>  **Output** : [3, 4, 9]  
>  **Explanation** : 3, 4, 9 from col1 in order.

 **Method #1 : Using generator expression + zip() + * operator**

In this, we perform task of extracting columnwise using zip() and * operator
is used to unpack values to be further flattened in generator expression.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Column-wise elements in Dictionary value list

# Using generator expression + zip() + * operator

 

# initializing dictionary

test_dict = {'Gfg' : [3, 6, 7],

 'is' : [4, 2, 6], 

 'best' :[9, 1, 3]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# values() gets all values at on

res = list(a for b in zip(*test_dict.values()) for a
in b)

 

# printing result 

print("The extracted values : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': [3, 6, 7], 'is': [4, 2, 6], 'best': [9, 1, 3]}
    The extracted values : [3, 4, 9, 6, 2, 1, 7, 6, 3]
    

**Method #2 : Using chain.from_iterable() + zip() + * operator**

In this, task of flattening is done using chain.from_iterable(). Rest all
functionalities are similar to above method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Column-wise elements in Dictionary value list

# Using chain.from_iterable() + zip() + * operator

from itertools import chain

 

# initializing dictionary

test_dict = {'Gfg' : [3, 6, 7],

 'is' : [4, 2, 6], 

 'best' :[9, 1, 3]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# values() gets all values at on

res = list(chain.from_iterable(zip(*test_dict.values())))

 

# printing result 

print("The extracted values : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': [3, 6, 7], 'is': [4, 2, 6], 'best': [9, 1, 3]}
    The extracted values : [3, 4, 9, 6, 2, 1, 7, 6, 3]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

