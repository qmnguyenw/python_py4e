Python – Assign keys with Maximum element index



Given Dictionary with value lists, the task is to write a Python program to
assign each key with an index of the maximum value in the value list.

 **Examples:**

>  **Input :** test_dict = {“gfg” : [5, 3, 6, 3], “is” : [1, 7, 5, 3], “best”
> : [9, 1, 3, 5]}
>
>  **Output :** {‘gfg’: 2, ‘is’: 1, ‘best’: 0}
>
>  **Explanation :** Max element in “gfg”‘s value is 6 at 2nd index, hence
> assigned 2.
>
>  
>
>
>  
>
>
>  **Input :** test_dict = {“gfg” : [9, 3, 6, 3], “is” : [1, 7, 5, 3], “best”
> : [9, 1, 3, 5]}
>
>  **Output :** {‘gfg’: 0, ‘is’: 1, ‘best’: 0}
>
>  **Explanation :** Max element in “gfg”‘s value is 9 at 0th index, hence
> assigned 0.

 **Method #1 : Using** **max()** **\+ loop +** **index()**

In this, we get the index of the maximum element from the value list using
max() and index(). Loop is used for the task of iteration of keys in the
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

# Assign keys with Maximum element index

# Using max() + index() + loop

 

# initializing dictionary

test_dict = {"gfg": [5, 3, 6, 3], "is": [1,
7, 5, 3], "best": [9, 1, 3, 5]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

res = dict()

for key in test_dict:

 

 # using index() to get required value

 res[key] = test_dict[key].index(max(test_dict[key]))

 

# printing result

print("The maximum index assigned dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original dictionary is : {‘gfg’: [5, 3, 6, 3], ‘is’: [1, 7, 5, 3],
> ‘best’: [9, 1, 3, 5]}
>
> The maximum index assigned dictionary : {‘gfg’: 2, ‘is’: 1, ‘best’: 0}
>
>  
>
>
>  
>

 **Method #2 : Using dictionary comprehension + max() + index()**

In this, we perform task of getting result using dictionary comprehension
shorthand variation of above method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Assign keys with Maximum element index

# Using dictionary comprehension + max() + index()

 

# initializing dictionary

test_dict = {"gfg": [5, 3, 6, 3], "is": [1,
7, 5, 3], "best": [9, 1, 3, 5]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# using dictionary comprehension as one liner alternative

res = {key: test_dict[key].index(max(test_dict[key])) for key
in test_dict}

 

# printing result

print("The maximum index assigned dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original dictionary is : {‘gfg’: [5, 3, 6, 3], ‘is’: [1, 7, 5, 3],
> ‘best’: [9, 1, 3, 5]}
>
> The maximum index assigned dictionary : {‘gfg’: 2, ‘is’: 1, ‘best’: 0}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

