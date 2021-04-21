Python – Test if element is part of dictionary



Given a dictionary, test if K is part of keys or values of dictionary.

>  **Input** : test_dict = {“Gfg” : 1, “is” : 3, “Best” : 2}, K = “Best”  
>  **Output** : True  
>  **Explanation** : “Best” is present in Dictionary as Key.
>
>  **Input** : test_dict = {“Gfg” : 1, “is” : 3, “Best” : 2}, K = “Geeks”  
>  **Output** : False  
>  **Explanation** : “Geeks” is not present in Dictionary as Key.

 **Method #1 : Using any() + items() + generator expression**

The combination of above functions can be used to solve this problem. In this,
we check for any element using any() and items() is used to extract all the
keys and values of dictionary.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if element is part of dictionary

# Using any() + generator expression + items()

 

# initializing dictionary

test_dict = {"Gfg" : 1, "is" : 3, "Best" : 2}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing K 

K = "Gfg"

 

# using any() to check for both keys and values 

res = any(K == key or K == val for key, val in
test_dict.items())

 

# printing result 

print("Is K present in dictionary? : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': 1, 'is': 3, 'Best': 2}
    Is K present in dictionary? : True
    

**Method #2 : Using chain.from_iterables() + items()**

The combination of above functions can be used to solve this problem. In this,
we flatten all the items and then check if K is present is any of the items().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if element is part of dictionary

# Using chain.from_iterables() + items()

from itertools import chain

 

# initializing dictionary

test_dict = {"Gfg" : 1, "is" : 3, "Best" : 2}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing K 

K = "Gfg"

 

# flattening key-values and then checking

# using in operator

res = K in chain.from_iterable(test_dict.items())

 

# printing result 

print("Is K present in dictionary? : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': 1, 'is': 3, 'Best': 2}
    Is K present in dictionary? : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

