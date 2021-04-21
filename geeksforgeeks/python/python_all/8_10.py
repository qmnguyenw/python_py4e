Python – Unique values count of each Key



Given a Dictionaries list, the task is to write a Python program to count the
unique values of each key.

 **Example:**

>  **Input :** test_list = [{“gfg” : 1, “is” : 3, “best”: 2}, {“gfg” : 1, “is”
> : 3, “best” : 6},
>
> {“gfg” : 7, “is” : 3, “best” : 10}]
>
>  **Output :** {‘gfg’: 2, ‘is’: 1, ‘best’: 3}
>
>  
>
>
>  
>
>
>  **Explanation :** gfg has 1 and 7 as unique elements, hence 2.
>
>  **Input :** test_list = [{“gfg” : 1, “is” : 3, “best”: 2}, {“gfg” : 1, “is”
> : 3, “best” : 6},
>
> {“gfg” : 1, “is” : 3, “best” : 10}]
>
>  **Output :** {‘gfg’: 1, ‘is’: 1, ‘best’: 3}
>
>  **Explanation :** gfg has only 1 as unique element, hence 1.

 **Method #1 : Using** **len()** **+** **set()** **\+ loop**

In this, unique values is extracted using set(), len() is used to get its
count, and then the result is mapped to each key extracted using keys().
Iterating over keys occur in loop.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Unique values count of each Key

# Using len() + set()

 

# initializing lists

test_list = [{"gfg": 1, "is": 3, "best": 2}, {

 "gfg": 1, "is": 3, "best": 6}, {"gfg": 7,
"is": 3, "best": 10}]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = dict()

for key in test_list[0].keys():

 

 # mapping unique values.

 res[key] = len(set([sub[key] for sub in test_list]))

 

# printing result

print("Unique count of keys : " + str(res))  
  
---  
  
 __

 __

 **Output:**

  

  

> The original list is : [{‘gfg’: 1, ‘is’: 3, ‘best’: 2}, {‘gfg’: 1, ‘is’: 3,
> ‘best’: 6},
>
> {‘gfg’: 7, ‘is’: 3, ‘best’: 10}]
>
> Unique count of keys : {‘gfg’: 2, ‘is’: 1, ‘best’: 3}

 **Method #2 : Using dictionary comprehension + len() +** **set()**

Similar to above method, difference being dictionary comprehension is used as
one liner alternative for shorthand.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Unique values count of each Key

# Using len() + set() + dictionary comprehension

 

# initializing lists

test_list = [{"gfg": 1, "is": 3, "best": 2}, {

 "gfg": 1, "is": 3, "best": 6}, {"gfg": 7,
"is": 3, "best": 10}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# dictionary comprehension for compact solution

res = {key: len(set([sub[key] for sub in test_list]))

 for key in test_list[0].keys()}

 

# printing result

print("Unique count of keys : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [{‘gfg’: 1, ‘is’: 3, ‘best’: 2}, {‘gfg’: 1, ‘is’: 3,
> ‘best’: 6},
>
> {‘gfg’: 7, ‘is’: 3, ‘best’: 10}]
>
> Unique count of keys : {‘gfg’: 2, ‘is’: 1, ‘best’: 3}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

