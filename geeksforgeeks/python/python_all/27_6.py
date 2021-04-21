Python program to update a dictionary with the values from a dictionary list



Given a dictionary and dictionary list, update the dictionary with dictionary
list values.

>  **Input** : test_dict = {“Gfg” : 2, “is” : 1, “Best” : 3}, dict_list =
> [{‘for’ : 3, ‘all’ : 7}, {‘and’ : 1, ‘CS’ : 9}]  
> **Output** : {‘Gfg’: 2, ‘is’: 1, ‘Best’: 3, ‘for’: 3, ‘all’: 7, ‘and’: 1,
> ‘CS’: 9}  
> **Explanation** : All dictionary keys updated in single dictionary.  
>  **Input** : test_dict = {“Gfg” : 2, “is” : 1, “Best” : 3}, dict_list =
> [{‘for’ : 3, ‘all’ : 7}]  
> **Output** : {‘Gfg’: 2, ‘is’: 1, ‘Best’: 3, ‘for’: 3, ‘all’: 7}  
> **Explanation** : All dictionary keys updated in single dictionary.

**Method #1 : Using** **update()** **\+ loop**

In this, we iterate through all the elements in loop, and perform update to
update all the keys in dictionary to original dictionary.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Update dictonary with dictionary list

# Using update() + loop

 

# initializing dictionary

test_dict = {"Gfg" : 2, "is" : 1, "Best" : 3}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing dictionary list 

dict_list = [{'for' : 3, 'all' : 7}, {'geeks' :
10}, {'and' : 1, 'CS' : 9}]

 

for dicts in dict_list:

 

 # updating using update()

 test_dict.update(dicts)

 

# printing result 

print("The updated dictionary : " + str(test_dict))  
  
---  
  
 __

 __

 **Output:**

  

  

> The original dictionary is : {‘Gfg’: 2, ‘is’: 1, ‘Best’: 3}
>
> The updated dictionary : {‘Gfg’: 2, ‘is’: 1, ‘Best’: 3, ‘for’: 3, ‘all’: 7,
> ‘geeks’: 10, ‘and’: 1, ‘CS’: 9}

 **Method #2 : Using** **ChainMap** **+** ****** **operator**

In this, we perform task of merging all list dictionaries into 1 using
ChainMap and ** operator is used to merge target dictionary to merged
dictionary.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Update dictonary with dictionary list

# Using ChainMap + ** operator

from collections import ChainMap

 

# initializing dictionary

test_dict = {"Gfg" : 2, "is" : 1, "Best" : 3}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing dictionary list 

dict_list = [{'for' : 3, 'all' : 7}, {'geeks' :
10}, {'and' : 1, 'CS' : 9}]

 

# ** operator extacts keys and re initiates.

# ChainMap is used to merge dictionary list

res = {**test_dict, **dict(ChainMap(*dict_list))}

 

# printing result 

print("The updated dictionary : " + str(res))   
  
---  
  
__

__

**Output:**

> The original dictionary is : {‘Gfg’: 2, ‘is’: 1, ‘Best’: 3}
>
> The updated dictionary : {‘Gfg’: 2, ‘is’: 1, ‘Best’: 3, ‘for’: 3, ‘all’: 7,
> ‘geeks’: 10, ‘and’: 1, ‘CS’: 9}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

