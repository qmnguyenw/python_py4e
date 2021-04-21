Python program to sort Dictionary by Key Lengths



Given Dictionary, sort by its key lengths.

>  **Input** : test_dict = {“Gfg” : 4, “is” : 1, “best” : 0, “for” : 3,
> “geeks” : 3}  
> **Output** : {‘is’: 1, ‘Gfg’: 4, ‘for’: 3, ‘best’: 0, ‘geeks’: 3}  
> **Explanation** : 2 < 3 = 3 < 4 < 5, are sorted lengths in order.
>
>  **Input** : test_dict = {“Gfg” : 4, “for” : 3, “geeks” : 3}  
> **Output** : {‘Gfg’: 4, ‘for’: 3, ‘geeks’: 3}  
> **Explanation** : 3 = 3 < 5, are sorted lengths in order.  
>

**Method #1 : Using len() + sort() + dictionary comprehension + items()**

In this, we perform the task of sorting using sort(), items() is used to get
tuple pair from the dictionary, len() gets the keys lengths. Then dictionary
comprehension performs the task of converting back to dictionary.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Dictionary by Key Lengths

# Using len() + sort() + dictionary comprehension + items()

 

def get_len(key):

 return len(key[0])

 

# initializing dictionary

test_dict = {"Gfg" : 4, "is" : 1, "best" : 0,
"for" : 3, "geeks" : 3}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# sorting using sort()

# external to render logic 

test_dict_list = list(test_dict.items())

test_dict_list.sort(key = get_len)

 

# reordering to dictionary

res = {ele[0] : ele[1] for ele in test_dict_list}

 

# printing result 

print("The sorted dictionary : " + str(res))   
  
---  
  
__

__

**Output:**

> The original dictionary is : {‘Gfg’: 4, ‘is’: 1, ‘best’: 0, ‘for’: 3,
> ‘geeks’: 3}  
> The sorted dictionary : {‘is’: 1, ‘Gfg’: 4, ‘for’: 3, ‘best’: 0, ‘geeks’: 3}

 **Method #2 : Using sorted() + lambda function + items() + dictionary
comprehension**

In this, we perform the task of sorting using sorted(), lambda function is
used to provide the logic of getting key lengths.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Dictionary by Key Lengths

# Using sorted() + lambda function + items() + dictionary comprehension

 

# initializing dictionary

test_dict = {"Gfg" : 4, "is" : 1, "best" : 0,
"for" : 3, "geeks" : 3}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# sorting using sorted()

# lambda fnc. to render logic 

test_dict_list = sorted(list(test_dict.items()), key = lambda
key : len(key[0]))

 

# reordering to dictionary

res = {ele[0] : ele[1] for ele in test_dict_list}

 

# printing result 

print("The sorted dictionary : " + str(res))   
  
---  
  
__

__

**Output:**

> The original dictionary is : {‘Gfg’: 4, ‘is’: 1, ‘best’: 0, ‘for’: 3,
> ‘geeks’: 3}  
> The sorted dictionary : {‘is’: 1, ‘Gfg’: 4, ‘for’: 3, ‘best’: 0, ‘geeks’: 3}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

