Python – Swap ith and jth key’s value in dictionary



Given a dictionary, perform swapping of ith and jth index key’s value.

>  **Input** : test_dict = {“Gfg”: 2, “is”: 4, “best”: 7, “for”: 9, “geeks”:
> 10}, i, j = 1, 4  
> **Output** : {‘Gfg’: 2, ‘is’: 10, ‘best’: 7, ‘for’: 9, ‘geeks’: 4}  
> **Explanation** : Values of “is” and “geeks” swapped.
>
>  **Input** : test_dict = {“Gfg”: 2, “is”: 4, “best”: 7, “for”: 9, “geeks”:
> 10}, i, j = 1, 2  
> **Output** : {‘Gfg’: 2, ‘is’: 7, ‘best’: 4, ‘for’: 9, ‘geeks’: 10}  
> **Explanation** : Values of “is” and “best” swapped.

**Method #1 : Using loop + values()**

This is one of the ways in which this task can be performed. In this, we get
the required swap key’s values and perform the required swap in loop, which
creates a new dictionary.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Swap ith and jth key's value in dictionary

# Using loop + values()

 

# initializing dictionary

test_dict = {"Gfg": 2, "is": 4, "best": 7,

 "for": 9, "geeks": 10}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing i, j 

i, j = 1, 3

 

# Extracting keys 

vals = list(test_dict.values())

 

# performing swap 

vals[i], vals[j] = vals[j], vals[i]

 

# setting new values 

res = dict()

for idx, key in enumerate(test_dict):

 res[key] = vals[idx]

 

# printing result 

print("Required dictionary : " + str(res))   
  
---  
  
__

__

**Output:**

> The original dictionary is : {‘Gfg’: 2, ‘is’: 4, ‘best’: 7, ‘for’: 9,
> ‘geeks’: 10}  
> Required dictionary : {‘Gfg’: 2, ‘is’: 9, ‘best’: 7, ‘for’: 4, ‘geeks’: 10}

 **Method #2 : Using values() + dictionary comprehension**

This is one of the ways in which this task can be performed. This is a method
similar to above, the difference being that the dictionary assigning step is
performed using dictionary comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Swap ith and jth key's value in dictionary

# Using values() + dictionary comprehension

 

# initializing dictionary

test_dict = {"Gfg": 2, "is": 4, "best": 7, 

 "for": 9, "geeks": 10}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing i, j 

i, j = 1, 3

 

# Extracting keys 

vals = list(test_dict.values())

 

# performing swap 

vals[i], vals[j] = vals[j], vals[i]

 

# setting new values 

res = {key : vals[idx] for idx, key in enumerate(test_dict)}

 

# printing result 

print("Required dictionary : " + str(res))   
  
---  
  
__

__

**Output:**

> The original dictionary is : {‘Gfg’: 2, ‘is’: 4, ‘best’: 7, ‘for’: 9,
> ‘geeks’: 10}  
> Required dictionary : {‘Gfg’: 2, ‘is’: 9, ‘best’: 7, ‘for’: 4, ‘geeks’: 10}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

