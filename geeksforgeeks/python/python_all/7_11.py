Python – Minimum value key assignment



Given two dictionaries, the task is to write a Python program to assign
minimum values for matching keys from both dictionaries.

 **Examples:**

>  **Input :** test_dict1 = {“gfg” : 1, “is” : 7, “best” : 8}, test_dict2 =
> {“gfg” : 2, “is” : 2, “best” : 10}
>
>  **Output :** {“gfg” : 1, “is” : 2, “best” : 8}
>
>  **Explanation :** Minimum of 1 and 2 is 1, hence, gfg is assigned with 1
> and so on.
>
>  
>
>
>  
>
>
>  **Input :** test_dict1 = {“gfg” : 1, “is” : 7, “best” : 12}, test_dict2 =
> {“gfg” : 2, “is” : 2, “best” : 10}
>
>  **Output :** {“gfg” : 1, “is” : 2, “best” : 10}
>
>  **Explanation :** Minimum of 10 and 12 is 10, hence, best is assigned with
> 10 and so on.

 **Method #1 : Using** **dictionary comprehension** **+** **min()** **+**
**items()**

In this, minimum of keys’ values are extracted using min(). Dictionary
comprehension is used to reconstruct the dictionary with modified values.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Minimum value key assignment

# Using dictionary comprehension + min() + items()

 

# initializing dictionaries

test_dict1 = {"gfg": 1, "is": 7, "best": 8}

test_dict2 = {"gfg": 2, "is": 2, "best": 10}

 

# printing original dictionaries

print("The original dictionary 1 is : " + str(test_dict1))

print("The original dictionary 2 is : " + str(test_dict2))

 

# using min() to assign min values

res = {key: min(val, test_dict2[key]) for key, val in
test_dict1.items()}

 

# printing result

print("The minimum value keys : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original dictionary 1 is : {'gfg': 1, 'is': 7, 'best': 8}
    The original dictionary 2 is : {'gfg': 2, 'is': 2, 'best': 10}
    The minimum value keys : {'gfg': 1, 'is': 2, 'best': 8}

 **Method #2 : Using** **dict()** **+** **min()** **+** **zip()**

In this, for better comparison, _zip()_ is used for getting values to compare,
_min()_ is used to get minimum values of keys. Then _dict()_ is used to
conversion of result to dictionary.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Minimum value key assignment

# Using dict() + min() + zip()

 

# initializing dictionaries

test_dict1 = {"gfg": 1, "is": 7, "best": 8}

test_dict2 = {"gfg": 2, "is": 2, "best": 10}

 

# printing original dictionaries

print("The original dictionary 1 is : " + str(test_dict1))

print("The original dictionary 2 is : " + str(test_dict2))

 

# using min() to assign min values

# dict() for conversion of result to dictionary

res = dict([min(i, j) for i, j in zip(test_dict1.items(),
test_dict2.items())])

 

# printing result

print("The minimum value keys : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original dictionary 1 is : {'gfg': 1, 'is': 7, 'best': 8}
    The original dictionary 2 is : {'gfg': 2, 'is': 2, 'best': 10}
    The minimum value keys : {'gfg': 1, 'is': 2, 'best': 8}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

