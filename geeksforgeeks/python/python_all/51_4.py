Python – Append Dictionary Keys and Values ( In order ) in dictionary



Given a dictionary, perform append of keys followed by values in list.

>  **Input** : test_dict = {“Gfg” : 1, “is” : 2, “Best” : 3}  
>  **Output** : [‘Gfg’, ‘is’, ‘Best’, 1, 2, 3]  
>  **Explanation** : All the keys before all the values in list.
>
>  **Input** : test_dict = {“Gfg” : 1, “Best” : 3}  
>  **Output** : [‘Gfg’, ‘Best’, 1, 3]  
>  **Explanation** : All the keys before all the values in list.

 **Method #1 : Using list() + keys() + values()**

This is one of the ways in which this task can be performed. In this, we
extract keys and values using keys() and values(), convert then to list using
list() and perform append in order.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Append Dictionary Keys and Values ( In order ) in dictionary

# Using values() + keys() + list()

 

# initializing dictionary

test_dict = {"Gfg" : 1, "is" : 3, "Best" : 2}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# + operator is used to perform adding keys and values

res = list(test_dict.keys()) + list(test_dict.values())

 

# printing result 

print("The ordered keys and values : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': 1, 'is': 3, 'Best': 2}
    The ordered keys and values : ['Gfg', 'is', 'Best', 1, 3, 2]
    

**Method #2 : Using chain() + keys() + values()**

This is one of the ways in which this task can be performed. In this, we bind
keys with values together in order using chain().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Append Dictionary Keys and Values ( In order ) in dictionary

# Using chain() + keys() + values()

from itertools import chain

 

# initializing dictionary

test_dict = {"Gfg" : 1, "is" : 3, "Best" : 2}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# chain() is used for concatenation

res = list(chain(test_dict.keys(), test_dict.values()))

 

# printing result 

print("The ordered keys and values : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': 1, 'is': 3, 'Best': 2}
    The ordered keys and values : ['Gfg', 'is', 'Best', 1, 3, 2]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

